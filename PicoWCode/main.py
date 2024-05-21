import json, re, network, socket, machine, gc
from time import sleep
import utils

# Highly recommended to set a lowish garbage collection threshold to minimise memory fragmentation as we sometimes want to
#       allocate relatively large blocks of RAM
gc.threshold(50000)

PAGES_PATH = "pages"
CONFIG_FILE_PATH = 'config.json'
IS_AUTHENTICATED = False

login_error_status = 'none'

# Returns the desired values from the config file as a dictionary
def getValuesFromConfig(*args):
    with open(CONFIG_FILE_PATH, 'r') as file:
        data = json.load(file)

    # Create an object composed of the desired keys from the config file
    results = {}    
    for key in args:
        results[key] = data.get(key)

    return results



# Updates the specified keys in the config file with their new values
# Can't do the fancy truncate hack since Micropython doesn't have truncate() at time of writing
def updateValuesInConfig(**kwargs):
    data = ''
    # Read file contents into variable for editing
    with open(CONFIG_FILE_PATH, "r") as f:
        data = json.load(f)

    # Augment the keys with new values
    data.update(**kwargs)

    # Write the new contents to the file
    with open(CONFIG_FILE_PATH, 'w') as f:
        try:
            json.dump(data, f)
            print('Values in config file have been successfully updated')
            return True
        except:
            return False



# Sends a page to the client ("renders" it). Will augment it with any passed-in kwargs where applicable
def render(filepath, **kwargs):
    file_requested = ''
    # Read the passed-in file to a variable
    with open(filepath, 'r') as file:
        file_requested = file.read()
    # If kwargs have been passed in, augment the file to include them
    if kwargs:
        pattern = r"~~(\w+)~~"

        # Use a lambda function for replacement
        return re.sub(pattern, lambda m: kwargs.get(m.group(1), m.group(0)), file_requested)
    return file_requested



##############################################
################## PAGES #####################
##############################################
# These methods return various things to the client when requested. The reason these are in separate methods is to 
#       allow for more logic once we start integrating the clock (or we want to add other stuff)
def mainStyles():
    return render(f'{PAGES_PATH}/main-styles.css')

def mainJavascript():
    # TODO: Need to add "Content-Type: text/javascript" to a header somewhere
    return render(f'{PAGES_PATH}/main-script.js', **getValuesFromConfig('time', 'off_color', 'on_color', 'colon_color'))

def loginStyles():
    return render(f'{PAGES_PATH}/login-styles.css')

def index():
    return render(f'{PAGES_PATH}/login.html', errorStatus = login_error_status)

def main():
    return render(f'{PAGES_PATH}/main.html')
##############################################
##############################################
##############################################


# Setup a custom AP
ap = network.WLAN(network.AP_IF)
# Create an open AP (i.e. no password needed to connect)
ap.config(essid=getValuesFromConfig('ap_ssid')['ap_ssid'], security=0)



# Activate the AP and respond to routes
def activateAP():
    global IS_AUTHENTICATED
    global login_error_status

    # Available routes the AP will respond to
    # It's important to make these callbacks and not function calls because - while it will still work - it saves the render in this dictionary and never calls it again
    #       This means that if a page updates, we never call render() again (because we never call these functions again)
    #       Making these callbacks makes it so that we actually call each function every time
    routes = {
        '/': index,
        '/main': main,
        '/login-styles.css': loginStyles,
        '/main-styles.css': mainStyles,
        '/main-script.js': mainJavascript,
        '/leave': '' # We don't need anything here because the loop breaks before we try and hit this. But the entry still needs to be here
    }

    # Activate AP
    ap.active(True)

    # Wait till it's active before we do anything
    while ap.active() == False:
        pass
    print('AP is active. You can now connect')
    print('IP address to connect to: ' + ap.ifconfig()[0])

    # Once active, listen for connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # This helps with this error: OSError: [Errno 98] EADDRINUSE
    # TODO: Very rarely you will get this error anyway. Add some retry logic to do this a few times if it fails
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 80))
    s.listen(5) # Allows 5 connections. We could change this, but 5 is fine for now

    # Connection loop (wait around, accept connections, respond to appropriate routes with the right content, etc)
    while True:
        # Accept the connection
        conn, _ = s.accept()
        # print('Got a connection from: %s' % str(addr))

        # Get the request it sent
        request = conn.recv(1024)
        print('request', request)

        # print('Content = %s' % str(request))

        # Rare, but does happen from time to time (never found out why)    
        if request == b'':
            conn.close()
            continue

        # Decode our request string and only get the route
        # Looks like: "GET /index HTTP/1.1 ......"
        # Will save route as: /index
        route = request.decode().split()[1]


        if route == '/main':
            # Only respond if the username/password are in the request
            if IS_AUTHENTICATED or 'username' in request and 'password' in request:
                # But, in the case this is from a bad actor that doesn't know the scheme, route them back to the login
                #       Otherwise, the unpacking that happens will break and halt the AP
                try:
                    # Get the username/password that was attached to the request
                    username, password = request.decode().split('\r\n')[-1].split('&')
                    username = username.split('=')[-1]
                    password = password.split('=')[-1]

                    # Get the username/password from our config file
                    credentials = getValuesFromConfig('username', 'password')

                    # If username/password matches the config file, let them in
                    if username == credentials['username'] and password == credentials['password']:
                        IS_AUTHENTICATED = True
                        login_error_status = 'none'
                    # Otherwise, set the error block on the login page and change the route back to the login
                    else:
                        route = '/'
                        login_error_status = 'block'
                except:
                    route = '/'
            else:
                print('username/password not in request')

        # Change the login credentials
        elif route == '/change-login':
            # Only let them do this if they're authenticated
            if IS_AUTHENTICATED:
                print('change login request')
                # Get the username/password that was attached to the request
                new_username, new_password = request.decode().split('\r\n')[-1].split('&')

                # Save these values to the config file so they can be read later
                updateValuesInConfig(username = new_username.split('=')[-1], password = new_password.split('=')[-1])

                # Take them to /main. This will trigger a re-render
                route = '/main'

        # Change the time (both in the web so it shows the correct time and on the clock itself)
        elif route == '/change-time':
            # Only let them do this if they're authenticated
            if IS_AUTHENTICATED:
                print('change time request')
                new_time = request.decode().split('\r\n')[-1]
                # At this point, new_time looks like this: time=08%3A32
                # This line will convert it to this: 08:32
                new_time = ':'.join(new_time.split('=')[-1].split('%3A'))
                updateValuesInConfig(time = new_time)
                # TODO: Change the time on the clock here
                route = '/main'

        # Change the date
        elif route == '/change-date':
            # Only let them do this if they're authenticated
            if IS_AUTHENTICATED:
                print('change date request')
                print(request.decode().split('\r\n')[-1])
                # updateValuesInConfig(date = new_time)
                route = '/main'

        # When they exit the webpage
        # This will break out of our while loop and hit our outer function to shutdown the AP and run the clock code
        elif route == '/leave':
            # Only let them do this if they're authenticated
            if IS_AUTHENTICATED:
                print('in leave')
                updateValuesInConfig(start_ap = 'False')
                break


        # Only respond to routes that are specified
        if route == '' or route == b'' or route is None or route not in routes.keys():
            conn.close()
            continue

        # Don't let them get anything for the main page unless they're authenticated
        if route == '/main-styles.css' or route == '/main-script.js':
            if not IS_AUTHENTICATED:
                print('not authenticated')
                conn.close()
                continue

        print(route)
        # Send the connected thing the appropriate page for the route they requested
        conn.sendall(routes[route]())

        # Counter-intuitively, this has to be here to make things work
        conn.close()

        gc.collect()



# Shutdown the AP and do some garbage collection
def deactivateAP():
    global IS_AUTHENTICATED
    IS_AUTHENTICATED = False
    ap.active(False)
    gc.collect()



# This will run whatever clock code we have (W.I.P.)
def runClockCode():
    while True:
        # Check for interrupts here so we can break?
        print('hello')
        print(getValuesFromConfig('time')['time'])
        print(rtc.datetime())
        sleep(15)
    # TODO: If we do break, clean up
    gc.collect()







rtc = machine.RTC()


# Main loop
while True:
    # Start AP until we need to shut it down
    if getValuesFromConfig('start_ap')['start_ap'] == 'True':
        activateAP()
        # deactivateAP()
    # Otherwise run clock code
    else:
        runClockCode()



