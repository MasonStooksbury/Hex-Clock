import json
CONFIG_FILE_PATH = './config.json'

# # Updates the specified keys in the config file with their new values
# def updateValuesInConfig(**kwargs):
#     data = ''
#     with open(CONFIG_FILE_PATH, "r") as f:
#         # Read file contents into variable for editing
#         data = json.load(f)

#     # Augment the keys with new values
#     data.update(**kwargs)

#     with open(CONFIG_FILE_PATH, 'w') as f:
#         # Write the new contents to the file
#         json.dump(data, f)


# #updateValuesInConfig(username='fuckme')
deet = ''
with open(CONFIG_FILE_PATH, 'r') as f:
    deet = json.load(f)
print(deet)





# import network, socket, json

# # Returns the desired values from the config file as a dictionary
# def getValuesFromConfig(*args):
#     with open('config.json', 'r') as file:
#         data = json.load(file)

#     # Create an object composed of the desired keys from the config file
#     results = {}
#     for key in args:
#         results[key] = data.get(key)

#     return results


# # Setup a custom AP
# ap = network.WLAN(network.AP_IF)
# ap_credentials = getValuesFromConfig('ap_ssid', 'ap_password')
# # Create an open AP
# ap.config(essid=ap_credentials['ap_ssid'], security=0)
# ap.active(True)

# # Wait till it's active before we do anything
# while ap.active() == False:
#     pass
# print('AP is active. You can now connect')
# print('IP address to connect to: ' + ap.ifconfig()[0])

# # Once active, listen for connections
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(('', 80))
# s.listen(5)

# while True:
#     conn, addr = s.accept()
#     print('Got a connection from: %s' % str(addr))
#     request = conn.recv(1024)
#     print('request', request)

#     # print('Content = %s' % str(request))

#     # Rare, but does happen from time to time (never found out why)    
#     if request == b'':
#         conn.close()
#         continue

#     # Decode our request string and only get the route
#     # Looks like: "GET /index HTTP/1.1 ......"
#     route = request.decode().split()[1]




#     if route == '/main':
#         # Only respond if the username/password are in the request
#         if IS_AUTHENTICATED or 'username' in request and 'password' in request:
#             # But, in the case this is from a bad actor that doesn't know the scheme, route them back to the login
#             #       Otherwise, the unpacking that happens will break and halt the AP
#             try:
#                 # Get the username/password that was attached to the request
#                 username, password = request.decode().split('\r\n')[-1].split('&')
#                 username = username.split('=')[-1]
#                 password = password.split('=')[-1]

#                 # Get the username/password from our config file
#                 credentials = getValuesFromConfig('username', 'password')

#                 # Technically the login page itself is equipped to accurately authenticate someone, but we do it here in case
#                 #       some bad actor hits the /main route. Otherwise, we could not have this block and assume anything hitting
#                 #       the /main route is already authenticated
#                 if username == credentials['username'] and password == credentials['password']:
#                     IS_AUTHENTICATED = True
#                 print('returning main route')
#             except:
#                 route = '/'
#         else:
#             print('username/password not in request')

#     elif route == '/change-login':
#         if IS_AUTHENTICATED:
#             print('change login request')
#             # Get the username/password that was attached to the request
#             new_username, new_password = request.decode().split('\r\n')[-1].split('&')

#             # Save these values to the config file so they can be read later
#             updateValuesInConfig(username = new_username.split('=')[-1], password = new_password.split('=')[-1])

#             # Take them to /main. This will trigger a re-render so that the JavaScript file has the updated values
#             route = '/main'

#     elif route == '/change-time':
#         if IS_AUTHENTICATED:
#             print('change time request')
#             new_time = request.decode().split('\r\n')[-1]
#             # At this point, new_time looks like this: time=08%3A32
#             # This line will convert it to this: 08:32
#             new_time = ':'.join(new_time.split('=')[-1].split('%3A'))
#             updateValuesInConfig(time = new_time)
#             route = '/main'

#     elif route == '/quit':
#         updateValuesInConfig(start_ap = 'False')
#         break














#     # Only respond to routes that are specified
#     if route == '' or route == b'' or route is None or route not in routes.keys():
#         conn.close()
#         continue

#     # Don't let them get anything for the main page unless they're authenticated
#     # if route == '/main-styles.css' or route == '/main-script.js':
#     #     if not IS_AUTHENTICATED:
#     #         print('not authenticated')
#     #         conn.close()
#     #         continue

#     print(route)
#     # Send the connected thing the appropriate page for the route they requested
#     conn.sendall(routes[route]())

#     # Counter-intuitively, this has to be here to make things work
#     conn.close()

#     # Free up some memory
#     # gc.collect()
