# Hex Clock

From the mind of inventor Johnathan Wood comes the: *Hex Clock*. A novel timepiece combining two of Johnathan's favorite things: technology and hexagons. The Hex Clock uses two hexagons to represent sexigesimal time using two 6-bit numbers wrapped around hexagons. Let's see a picture that will hopefully make more sense.
![Description of how the clock works](https://github.com/MasonStooksbury/Hex-Clock/blob/main/Pictures/clock-explanation.png?raw=true)

<br><br><br>

# Setup Instructions
### Download these things (if you don't already have them)
- Install VSCode: [link](https://code.visualstudio.com/download)
- Install VSCode Extension `MicroPico` by paulober
- Firmware for RaspberryPi PicoW (if you haven't already done this): [latest](https://rpf.io/pico-w-firmware)
- Download/Clone the code from this repo

<br><br><br>

# Developer Setup
- Open just the `PicoWCode` folder in VSCode; it should look something like this:
  - This is really important for a later step. Doing this wrong could have weird effects or just not work
  - ![How the file explorer should look in VSCode](https://github.com/MasonStooksbury/Hex-Clock/blob/main/Pictures/folder.png?raw=true)
- Plug in your PicoW (`pico` from now on)
- Under the `View` tab, click on `Command Palette...` or do `Ctrl + Shift + P` if that shortcut is enabled
- Click `MicroPico: Connect` to attempt a connection to the pico
- Once connected, you will see options appear in the footer bar of VSCode (you'll use these mostly):
  - ![What the footer options look like](https://github.com/MasonStooksbury/Hex-Clock/blob/main/Pictures/footer-options.png?raw=true)
- If all is good, you should see that checkmark with "Pico Connected" next to it
  - If this doesn't work, try replugging it, getting a different cable, or trying a different USB port
- Finally, open up the `test.py` file and make sure that you are on that tab (when we hit the `Run` footer button, MicroPico will attempt to run whatever tab we currently have focused)
- Click the `Run` footer button
- If you see "Everything is awesome!" in the terminal, then you're ready to start developing!

<br><br><br>

# Developing and Testing
### This will put all of your code onto the pico, and allow you to start testing
- Once you've written some code, let's put it on the pico
- Click the `All commands` footer button
- Click `MicroPico: Upload project to Pico`. This will put all of the files in the lefthand explorer onto the pico (this is why we need to open *only* the `PicoWCode` folder in VSCode)
- Once finished, it's often good to do a soft reset (no idea why, I've just noticed it help sometimes) simply click the `Reset` footer button
- Make sure that the `main.py` (or whatever `.py` file you are currently testing) is open and focused
- Click the `Run` footer button
