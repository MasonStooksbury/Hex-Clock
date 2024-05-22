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
tris = [
    [0,1,2],    # Least significant bit
    [3,4,5],    #          |
    [6,7,8],    #          |
    [9,10,11],  #          |
    [12,13,14], #          |
    [15,16,17]  # Most significant bit
]




# NOTE: I do not recommend putting "pcb.write()" in any of the set methods as it can cause artifacts for faster animations


# This will set a particular LED in our "strip" to the specified color
def setLed(index, color):
    pcb.__setitem__(index, color)

# Set an entire tri of LEDs to the specified color
def setTri(tri, color):
    for led in tri:
        setLed(led, color)

# Converts the time as string "14:59" and returns a tuple of binary strings ("001110", "111011")
def timeToBinary(time):
    hours, minutes = time.split(':')
    return '{:0>{w}}'.format(f'{int(hours):b}', w=6), '{:0>{w}}'.format(f'{int(minutes):b}', w=6)

# Sets the necessary LEDs to match the binary string representing a decimal number
def binaryToClock(time_in_binary, on_color, off_color):
    # You can either loop through the tris in reverse, or reverse the string. Either one makes it a little easier to assign
    for index, bit in enumerate(''.join(list(reversed(time_in_binary)))):
        setTri(tris[index], on_color if bit == '1' else off_color)

# Clear the PCB by setting everyting to a color of (0,0,0,0)
def clear():
    for led in range(NUM_LEDS):
        setLed(led, BLANK)
        pcb.write()



def animation1():
    inner = [17, 14, 11, 8, 5, 2, 17, 14, 11, 8, 5, 2]
    outer = [1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 0]

    head = 0
    tail = 1

    while True:

        setLed(inner[head], (255, 0, 0, 0))
        setLed(inner[tail], BLANK)

        setLed(outer[head], (0,0,255,0))
        setLed(outer[tail], BLANK)

        head += 1
        tail += 1

        head = 0 if head > len(inner) - 1 else head
        tail = 0 if tail > len(inner) - 1 else tail

        pcb.write()
        sleep(0.3)


def animation2():
    lines = [(16, 17, 8, 7), (15, 17, 8, 6), (13, 14, 5, 4), (12, 14, 5, 3), (10, 11, 2, 1), (9, 11, 2, 0)] 

    while True:
        for line in lines:
            clear()
            for pixel in line:
                setLed(pixel, (0, 255, 0, 0))
            pcb.write()
            sleep(0.1)

def animation3():
    pixels = [0,1,2,5,3,4,6,8,7,9,11,10,12,14,13,15,17,16]
    head = 0
    tail = 5

    while True:
        setLed(pixels[head], (128, 128, 0, 0))
        setLed(pixels[tail], BLANK)

        head += 1
        tail += 1

        head = 0 if head > len(pixels) - 1 else head
        tail = 0 if tail > len(pixels) - 1 else tail

        pcb.write()
        sleep(0.2)


if __name__ == '__main__':
    # hours, minutes = timeToBinary('14:59')

    clear()

    # animation1a()

    # binaryToClock(minutes, (255,0,0,0), (0,0,0,0))
    # pcb.write()
    # sleep(3)

    clear()