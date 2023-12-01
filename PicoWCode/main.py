import network, socket
from time import sleep
import json

AP_NAME = "Hex Clock"
AP_PASSWORD = "password123"
AP_DOMAIN = "hexclock.com"
PAGES_PATH = "pages"
CONFIG_FILE_PATH = 'config.json'



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
def updateValuesInConfig(**kwargs):
    with open(CONFIG_FILE_PATH, "r+") as f:
        # Read file contents into variable for editing
        data = json.load(f)
        # Augment the keys with new values
        data.update(**kwargs)
        # Delete the contents of the file
        f.truncate(0)
        # Make sure our cursor is at the beginning of the file
        f.seek(0)
        # Write the new contents to the file
        json.dump(data, f, indent=4)
    


# Return the file as a string so it can be streamed to the connecting socket
# Takes kwargs and can format the file with them
def render(other, **kwargs):
    file_requested = ''
    # Read the passed-in file to a variable
    with open(other, 'r') as file:
        file_requested = file.read()
    # If kwargs have been passed in, augment the file to include them
    if kwargs:
        file_requested = file_requested.format(**kwargs)
    return file_requested


def styles():
    return render(f'{PAGES_PATH}/styles.css')

def javascript():
    # The reason I don't pass the variables from main() directly into the JS file here is that format doesn't work the same because of all the other {} in it
    # TODO: Need to add "Content-Type: text/javascript" to a header somewhere
    return render(f'{PAGES_PATH}/script.js')

def login():
    return render(f'{PAGES_PATH}/login.html')

def main():
    return render(f'{PAGES_PATH}/main.html', **getValuesFromConfig('time', 'off_color', 'on_color', 'colon_color'))



# Available routes the AP will respond to
routes = {
    '/': login(),
    '/main': main(),
    '/styles.css': styles(),
    '/script.js': javascript()
}

# Setup a custom AP
ap = network.WLAN(network.AP_IF)
ap.config(essid=AP_NAME, password=AP_PASSWORD)
ap.active(True)

# Wait till it's active to do anything
while ap.active() == False:
    pass
print('AP is active. You can now connect')
print('IP address to connect to: ' + ap.ifconfig()[0])

# Once active, listen for connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: Put a try/catch around this
s.bind(('', 80))
s.listen(3)

# Connection loop (wait around, accept connections, respond to appropriate routes with the right content, etc)
while True:
    conn, addr = s.accept()
    print('Got a connection from: %s' % str(addr))
    request = conn.recv(1024)
    print('request', request)

    # print('Content = %s' % str(request))

    # Decode our request string and only get the route
    # Looks like: "GET /index HTTP/1.1 ......"
    route = request.decode().split()[1]
    if route == '/main':
        # Request has the values at the end like this, so we isolate them off with split() magic
        #       pt-Language: en-US,en;q=0.9\r\n\r\nusername=myusername&password=mypassword'
        username, password = request.decode().split('\r\n')[-1].split('&')
        # Save these values to the config file so they can be read later by the main.html handler
        updateValuesInConfig(username=username.split('=')[-1], password=password.split('=')[-1])

    # Only respond to routes that are specified
    if route == '' or route == b'' or route is None or route not in routes.keys():
        continue

    # Send the connected thing the appropriate page for the route they requested
    conn.sendall(routes[route])

    # Counter-intuitively, this has to be here to make things work
    conn.close()


# Start the web server...
# server.run()