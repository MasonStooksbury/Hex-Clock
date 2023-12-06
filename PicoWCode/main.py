import neopixel
from machine import Pin
from time import sleep

DATA_PIN = 21
NUM_LEDS = 18
BLANK = (0,0,0,0)

pcb = neopixel.NeoPixel(Pin(DATA_PIN), NUM_LEDS, bpp=4) # bpp=4 tells it that I'm using RGBW LEDs

# color = (0, 0, 255, 0)
# neoRing.fill(color)
# neoRing.write()

# neoRing.fill((0,0,0,0))
# neoRing.write()

tris = [[0,1,2],
[3,4,5],
[6,7,8],
[9,10,11],
[12,13,14],
[15,16,17]]

print(tris)



def setLed(index, color):
    pcb.__setitem__(index, color)

def setTri(tri, color):
    for led in tri:
        setLed(led, color)
    pcb.write()

def clear():
    for led in range(NUM_LEDS):
        setLed(led, BLANK)
        pcb.write()


def testLoop1():
    colors = [(255,0,0,0), (0,255,0,0), (0,0,255,0)]
    for color in colors:
        for led in range(18):
            setLed(led, color)
            pcb.write()
            sleep(0.1)

def testLoop2():
    colors = [(255,0,0,0), (0,255,0,0), (0,0,255,0)]
    for color in colors:
        for tri in tris:
            setTri(tri, color)
            pcb.write()
            sleep(0.4)

#clear()
#testLoop2()
#sleep(1)


clear()