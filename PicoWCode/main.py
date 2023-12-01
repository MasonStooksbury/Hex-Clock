from phew import access_point, dns, server
from phew.template import renderPage, renderOther
from phew.server import redirect
import network, time, socket
from time import sleep
import machine
import json
import os
import utime

AP_NAME = "Hex Clock"
AP_PASSWORD = "passwordfuck"
AP_DOMAIN = "hexclock.com"
PAGES_PATH = "pages"
# WIFI_MAX_ATTEMPTS = 3
CONFIG_FILE_PATH = 'config.json'




# def machine_reset():
#     utime.sleep(1)
#     print("Resetting...")
#     machine.reset()

# def getValueFromConfig(value):
#     with open(CONFIG_FILE_PATH, "r") as f:
#         data = json.load(f)
#     return data[value]







# # # microsoft windows redirects
# # @server.route("/ncsi.txt", methods=["GET"])
# # def hotspot(request):
# #     print(request)
# #     print("ncsi.txt")
# #     return "", 200


# # @server.route("/connecttest.txt", methods=["GET"])
# # def hotspot(request):
# #     print(request)
# #     print("connecttest.txt")
# #     return "", 200


# @server.route("/redirect", methods=["GET"])
# def hotspot(request):
#     print(request)
#     print("****************ms redir*********************")
#     return redirect(f"http://{AP_DOMAIN}/", 302)

# # # android redirects
# # @server.route("/generate_204", methods=["GET"])
# # def hotspot(request):
# #     print(request)
# #     print("******generate_204********")
# #     return redirect(f"http://{AP_DOMAIN}/", 302)

# # # apple redir
# # @server.route("/hotspot-detect.html", methods=["GET"])
# # def hotspot(request):
# #     print(request)
# #     """ Redirect to the Index Page """
# #     return renderPage("index.html")


# # @server.route("/wrong-host-redirect", methods=["GET"])
# # def wrong_host_redirect(request):
# #     print("******wrong host redirect********")
# #     return "<!DOCTYPE html><head><meta http-equiv=\"refresh\" content=\"0;URL='http://" + AP_DOMAIN + "'/ /></head>"
#     # return redirect(f"http://{AP_DOMAIN}/", 302)

# # @server.route("/favicon.ico", methods=["GET"])
# # def unnecessary(request):
# #     return 'Not found', 404














# @server.catchall()
# def catch_all(request):
#     if request.headers.get("host").lower() != AP_DOMAIN.lower():
#         # return redirect("http://" + AP_DOMAIN + "/redirect")
#         return renderPage(f"{PAGES_PATH}/redirect.html", domain = AP_DOMAIN)
#     return 'Not found', 404

# # Serves the CSS file
# def styles(request):
#     return renderOther(f"{PAGES_PATH}/styles.css")

# # Serves the JS file
# def script(request):
#     return renderOther(f"{PAGES_PATH}/script.js")

# # Serves the JSON file
# def config(request):
#     return renderOther(f"./config.json")

# def other(request):
#     return renderOther(f"{PAGES_PATH}/random.html")

# # This is where we start, which almost immediately takes us to the Login page
# # def index(request):
# #     print('in index')
# #     print(request.headers.get("host"))
# #     if request.headers.get("host").lower() != AP_DOMAIN.lower():
# #         return renderPage(f"{PAGES_PATH}/redirect.html", domain = AP_DOMAIN.lower())

# #     return renderPage(f"{PAGES_PATH}/login.html")
# @server.route('/', methods = ['GET'])
# def index(request):
#     if request.headers.get("host").lower() != AP_DOMAIN.lower():
#         return renderPage(f"{PAGES_PATH}/redirect.html", domain = AP_DOMAIN.lower())
#     return renderPage(f"{PAGES_PATH}/login.html")

# # Called when the user hits 'Login' on the Login page
# @server.route('/login', methods = ['POST'])
# def login(request):
#     # with open(WIFI_FILE, "w") as f:
#     #     json.dump(request.form, f)
#     #     f.close()
#     username = request.form['username']
#     password = request.form['password']

#     print('in login')

#     # return renderPage(f"{PAGES_PATH}/main.html")
#     return renderPage(f"{PAGES_PATH}/main.html",
#                       time = getValueFromConfig('time'),
#                       off_color = getValueFromConfig('off_color'),
#                       on_color = getValueFromConfig('on_color'),
#                       colon_color = getValueFromConfig('colon_color')
#                       )

# # Called when the user hits 'Submit' on the 'Change Colors' tab
# def changeColors(request):
#     off_color = request.form['offColorPicker']
#     on_color = request.form['onColorPicker']
#     colon_color = request.form['colonColorPicker']

#     # Drop back to the Login page
#     return renderPage(f"{PAGES_PATH}/login.html")

# # Called when the user hits 'Submit' on the 'Set Time' tab
# def changeTime(request):
#     time = request.form['time']

#     # Drop back to the Login page
#     return renderPage(f"{PAGES_PATH}/login.html")

# # Called when the user hits 'Change' on the 'Configure Login' tab
# def changeLogin(request):
#     new_username = request.form['newUsername']
#     new_password = request.form['newPassword']

#     # Drop back to the Login page
#     return renderPage(f"{PAGES_PATH}/login.html")



# # server.add_route("/", handler = index, methods = ["GET"])
# # server.add_route("/login", handler = login, methods = ["POST"])
# server.add_route("/change-colors", handler = changeColors, methods = ["POST"])
# server.add_route("/change-time", handler = changeTime, methods = ["POST"])
# server.add_route("/change-login", handler = changeLogin, methods = ["POST"])
# server.add_route("/styles.css", handler = styles, methods = ["GET"]) # This captures requests for /styles.css and handles them
# server.add_route("/script.js", handler = script, methods = ["GET"])
# server.add_route("/config.json", handler = config, methods = ["GET"])
# server.add_route("/favicon.ico", handler = unnecessary, methods = ["GET"])
# server.add_route("/generate204", handler = catch_all, methods = ["GET"])
# server.add_route("/generate_204", handler = catch_all, methods = ["GET"])
# server.set_callback(catch_all)

# ap = access_point(AP_NAME)
# ip = ap.ifconfig()[0]
# dns.run_catchall(ip)





def getValueFromConfig(value):
    with open(CONFIG_FILE_PATH, "r") as f:
        data = json.load(f)
    return data[value]


def render(other, **kwargs):
    file_requested = ''
    # Read the passed-in file to a variable
    with open(other, 'r') as file:
        file_requested = file.read()
    # If kwargs have been passed in, augment the file to include them
    if kwargs:
        file_requested.format(**kwargs)
    return file_requested


def new_styles():
    print('in new_styles')
    return render(f'{PAGES_PATH}/styles.css')

def new_javascript():
    print('in new_script')
    # Just pass the variables directly into here using your fancy, custom renderer
    return render(f'{PAGES_PATH}/script.js')

def new_main():
    print('in new_main')
    return render(f'{PAGES_PATH}/main.html',
                  	time = getValueFromConfig('time'),
                    off_color = getValueFromConfig('off_color'),
                    on_color = getValueFromConfig('on_color'),
                    colon_color = getValueFromConfig('colon_color'))




# Available routes the AP will respond to
routes = {
    '/': new_main(),
    '/styles.css': new_styles(),
    '/script.js': new_javascript()
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
s.bind(('', 80))
s.listen(5)

# Connection loop (wait around, accept connections, respond to appropriate routes with the right content, etc)
while True:
    conn, addr = s.accept()
    print('Got a connection from: %s' % str(addr))
    request = conn.recv(1024)

    print('Content = %s' % str(request))
    if str(request) == b'':
        print('weird shit')
        continue
    # Decode our request string and only get the route
    # Looks like: "GET / HTTP/1.1 ......"
    route = request.decode().split()[1]
    print('route', route)

    # Only respond to routes that are specified
    if route == '' or route is None or route not in routes.keys():
        continue

    # Send the connected thing the appropriate page for the route they requested
    conn.send(routes[route])

    # TODO: Should we close the connection?
    # conn.close()



























# Start the web server...
# server.run()