from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()
sense.clear()
while True:
    sense.clear()
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    nocolor = (0,0,0)

    for x in range (1,7):
        for y in range (1, 7):
            g = randint(0,1)
            if g == 1:
                sense.set_pixel (y, x, color)
            elif g == 0:
                sense.set_pixel (x, y, nocolor)
    sleep(10)
