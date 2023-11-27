from phew import access_point, dns, server
from phew.template import renderPage, renderOther
import machine
import json
import os
import utime

AP_NAME = "Hex Clock"
AP_DOMAIN = "hexclock.com"
PAGES_PATH = "pages"
WIFI_FILE = "wifi.json"
WIFI_MAX_ATTEMPTS = 3

def machine_reset():
    utime.sleep(1)
    print("Resetting...")
    machine.reset()

def setupMode():
    def catch_all(request):
        if request.headers.get("host") != AP_DOMAIN:
            return renderPage(f"{PAGES_PATH}/redirect.html", domain = AP_DOMAIN)

        return "Not found.", 404
    
    # Serves the CSS file
    def styles(request):
        return renderOther(f"{PAGES_PATH}/styles.css")
    
    # Serves the JS file
    def script(request):
        return renderOther(f"{PAGES_PATH}/script.js")
    
    # This is where we start, which almost immediately takes us to the Login page
    def index(request):
        if request.headers.get("host").lower() != AP_DOMAIN.lower():
            return renderPage(f"{PAGES_PATH}/redirect.html", domain = AP_DOMAIN.lower())

        return renderPage(f"{PAGES_PATH}/login.html")

    # Called when the user hits 'Login' on the Login page
    def login(request):
        # with open(WIFI_FILE, "w") as f:
        #     json.dump(request.form, f)
        #     f.close()
        username = request.form['username']
        password = request.form['password']

        return renderPage(f"{PAGES_PATH}/main.html")
    
    # Called when the user hits 'Submit' on the 'Change Colors' tab
    def changeColors(request):
        off_color = request.form['offColorPicker']
        on_color = request.form['onColorPicker']
        colon_color = request.form['colonColorPicker']

        # Drop back to the Login page
        return renderPage(f"{PAGES_PATH}/login.html")

    # Called when the user hits 'Submit' on the 'Set Time' tab
    def changeTime(request):
        time = request.form['time']

        # Drop back to the Login page
        return renderPage(f"{PAGES_PATH}/login.html")
    
    # Called when the user hits 'Change' on the 'Configure Login' tab
    def changeLogin(request):
        new_username = request.form['newUsername']
        new_password = request.form['newPassword']

        # Drop back to the Login page
        return renderPage(f"{PAGES_PATH}/login.html")

    server.add_route("/", handler = index, methods = ["GET"])
    server.add_route("/login", handler = login, methods = ["POST"])
    server.add_route("/change-colors", handler = changeColors, methods = ["POST"])
    server.add_route("/change-time", handler = changeTime, methods = ["POST"])
    server.add_route("/change-login", handler = changeLogin, methods = ["POST"])
    server.add_route("/styles.css", handler = styles, methods = ["GET"]) # This captures requests for /styles.css and handles them
    server.add_route("/script.js", handler = script, methods = ["GET"])
    server.set_callback(catch_all)

    ap = access_point(AP_NAME)
    ip = ap.ifconfig()[0]
    dns.run_catchall(ip)





# MAIN 
setupMode()

# Start the web server...
server.run()