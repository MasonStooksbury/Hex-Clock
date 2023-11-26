from phew import access_point, dns, server
from phew.template import renderPage, renderCSS
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
    def index(request):
        if request.headers.get("host").lower() != AP_DOMAIN.lower():
            return renderPage(f"{PAGES_PATH}/redirect.html", domain = AP_DOMAIN.lower())

        return renderPage(f"{PAGES_PATH}/login.html")

    def configure(request):
        # print("Saving wifi credentials...")

        # with open(WIFI_FILE, "w") as f:
        #     json.dump(request.form, f)
        #     f.close()
        print('username', request.form["username"])
        print('password', request.form["password"])
        print(request)

        return renderPage(f"{PAGES_PATH}/main.html")
        
    def catch_all(request):
        if request.headers.get("host") != AP_DOMAIN:
            return renderPage(f"{PAGES_PATH}/redirect.html", domain = AP_DOMAIN)

        return "Not found.", 404

    def styles(request):
        return renderCSS(f"{PAGES_PATH}/styles.css")

    server.add_route("/", handler = index, methods = ["GET"])
    server.add_route("/configure", handler = configure, methods = ["POST"])
    server.add_route("/styles.css", handler = styles, methods = ["GET"]) # This captures requests for /styles.css and handles them
    server.set_callback(catch_all)

    ap = access_point(AP_NAME)
    ip = ap.ifconfig()[0]
    dns.run_catchall(ip)





# MAIN 
setupMode()

# Start the web server...
server.run()