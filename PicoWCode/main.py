import neopixel
from machine import Pin
from time import sleep

HOURS_HEX_DATA_PIN = 21
MINUTES_HEX_DATA_PIN = 22
# How many LEDs are on the PCB
NUM_LEDS = 18
BLANK = (0,0,0,0)

pcb = neopixel.NeoPixel(Pin(HOURS_HEX_DATA_PIN), NUM_LEDS, bpp=4) # bpp=4 tells it that I'm using RGBW LEDs


# This layout matches how the PCB is currently wired
tris = [[0,1,2],
[3,4,5],
[6,7,8],
[9,10,11],
[12,13,14],
[15,16,17]]

# Represents the color that will show when the bit in the time is 1
ON_COLOR = (255,0,0,0)
# Represents the color that will show when the bit in the time is 0
OFF_COLOR = (0,0,0,0)




# NOTE: I do not recommend putting "pcb.write()" in any of the set methods as it can cause artifacts for faster animations



# This will set a particular LED in our "strip" to the specified color
def setLed(index, color):
    pcb.__setitem__(index, color)

# Set an entire tri of LEDs to the specified color
def setTri(tri, color):
    for led in tri:
        setLed(led, color)

# Sets the necessary LEDs to match the binary string representing a decimal number
def binaryToClock(time_in_binary):
    # You can either loop through the tris in reverse, or reverse the string. Either one makes it a little easier to assign
    for index, bit in enumerate(''.join(list(reversed(time_in_binary)))):
        setTri(tris[index], ON_COLOR if bit == '1' else OFF_COLOR)

    


# Clear the PCB by setting everyting to a color of (0,0,0,0)
def clear():
    for led in range(NUM_LEDS):
        setLed(led, BLANK)
        pcb.write()

            
# binaryToClock('101010')
# pcb.write()
# sleep(5)

# clear()