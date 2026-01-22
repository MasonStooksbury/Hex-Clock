[![License: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware_License-CERN--OHL--P--2.0-blue)](https://opensource.org/license/cern-ohl-p/)
[![License: MIT](https://img.shields.io/badge/Software_License-MIT-red.svg)](https://opensource.org/licenses/MIT)


# Hex Clock | KiCad 9.0

From the mind of my good friend and inventor Johnathan Wood comes: the *Hex Clock*. A novel timepiece combining two of his favorite things: technology and hexagons. The Hex Clock uses two hexagons to represent sexigesimal, 24-hour time using two 6-bit binary numbers wrapped around hexagons. Let's see a picture that will hopefully make more sense. (And yes, the left-most bit of the hours hex will never be illuminated except during animations)

<br>

![Visual description of how the clock works](https://github.com/MasonStooksbury/Hex-Clock/blob/main/pictures/clock-explanation.png?raw=true)

<br><br><br>

# Pre-setup Instructions
### Download these things (if you don't already have them)
- Download VSCode: [link](https://code.visualstudio.com/download)
- Install VSCode Extension `MicroPico` by paulober
- Download firmware for RaspberryPi PicoW (if you haven't already done this): [latest](https://rpf.io/pico-w-firmware)
- Download/Clone the code from this repo

<br><br><br>

# Developer Setup
- Open just the `PicoWCode` folder in VSCode; it should look something like this:
  - This is really important for a later step. Doing this wrong could have weird effects or just not work
  - ![How the file explorer should look in VSCode](https://github.com/MasonStooksbury/Hex-Clock/blob/main/pictures/folder.png?raw=true)
- Plug in your PicoW (`pico` from now on)
- Under the `View` tab, click on `Command Palette...` or do `Ctrl + Shift + P` if that shortcut is enabled
- Click `MicroPico: Connect` to attempt a connection to the pico
- Once connected, you will see options appear in the footer bar of VSCode (you'll use these mostly):
  - ![What the footer options look like](https://github.com/MasonStooksbury/Hex-Clock/blob/main/pictures/footer-options.png?raw=true)
- If all is good, you should see that checkmark with "Pico Connected" next to it
  - If this doesn't work, try replugging it, getting a different cable, or trying a different USB port
- Finally, open up the `test.py` file and make sure that you are on that tab (when we hit the `Run` footer button, MicroPico will attempt to run whatever tab we currently have focused)
- Click the `Run` footer button
- If you see "Everything is awesome!" in the terminal, then you're ready to start developing!

<br><br><br>

# Developing and Testing
### This will put all of your code onto the pico, and allow you to start testing
- Click the `All commands` footer button
- Click `MicroPico: Upload project to Pico`. This will put all of the files in the lefthand explorer onto the pico (this is why we need to open *only* the `PicoWCode` folder in VSCode)
- Once finished, it's often good to do a soft reset (no idea why, I've just noticed it help sometimes) simply click the `Reset` footer button
- Make sure that the `main.py` (or whatever `.py` file you are currently testing) is open and focused
- Click the `Run` footer button

<br>

## Quick and Dirty Testing
### If you just want to test code in a singular file (and don't really need everything else) you can simply focus the relevant file and hit the `Run` footer button. This is particularly helpful when developing new animations or random bits of code

### NOTE: If you're trying to test a file that imports another file (and you're changing both files regularly), this won't work and you'll have to follow the above instructions where you upload the code to the pico. 
  
<br><br><br>

# Connecting to the Pico and Using the Web App
### These instructions will help you connect to the Pico with your phone or other device and use the webapp that allows you to set the clock colors, change the time, or change the login credentials
- Either plug in the pico to an external power source or - if developing with VSCode open - connect the pico, open the main.py file, and click the `Run` footer button
- Once you see the `AP is active. You can now connect` message, the pico wifi access point (AP) is ready to receive connections
- Take note of the IP address listed just below this as you will need it in a moment (NOTE: In final version, this will hopefully be replaced with a domain name that you can connect to)
- On a wifi-enabled device, look for the `Hex Clock` network and connect to it (this is the default name and can be changed in the `main.py` script if desired)
- Once connected, open your web browser and type in the IP address from the previous step into the address bar
- At this point, you should see the Hex Clock login screen
- Login with these default credentials:
  - Username: `flump`
  - Password: `doople`

<br><br><br>

# Changing the Access Point SSID
- Changing the AP SSID is as simple as changing the line towards the top of `main.py`. However, the tricky part is in getting it propagate
- The steps below are about the only sure-fire way I've found to get it to work
  - Make sure the pico isn't currently running (if it is, click the `Stop` footer button to do so)
  - Click the `All commands` footer button
  - Click the `MicroPico: Delete all files from board` option
  - Click the `Reset` footer button
  - Physically unplug the pico from the computer
  - Plug the pico back in
  - Reconnect MicroPico manually or wait a second (it's usually pretty good about reconnecting automatically)
  - Click the `All commands` footer button
  - Click the `MicroPico: Upload project to Pico` option
  - Click the `Reset` footer button
  - On your wifi-enabled device that you are going to connect, go into your wifi settings and forget the network you previously attached to (this is critical as sometimes it will not show the SSID change on your device)
  - Click the `Run` footer button
  - At this point you should see the new SSID being broadcast under the available networks

<br><br><br>

# Troubleshooting
### These are some things I've run into and how to fix them
- Every now and then when you try to run `main.py` and the AP attempts to start up you might see this error: `OSError: [Errno 98] EADDRINUSE`. Follow these steps to mitigate it
  - If running, click the `Stop` footer button
  - Click the `Reset` footer button to perform a soft reset of the pico
  - Click the `Run` footer button again
  - If the above steps do not work, you can also just try click `Run` over and over again. Usually after 3-5 attempts it will work
- Sometimes when trying to hit the `Run` footer button you will see: `SyntaxError: invalid syntax`. Typically this just means that you have the wrong script focused. Make sure you are on the `main.py` script (or whatever script you're working on)
