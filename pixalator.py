from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()
sense.clear();

        
while 1:    
    for x in range(0,8):
        for y in range(0,8):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            color = (r, g, b)
            sense.set_pixel(x, y, color)
            sleep(0.1)
            sense.clear()
            sleep(0.1)
