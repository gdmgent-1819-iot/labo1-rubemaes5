from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()


while 1:
    

    def pick_color():
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return(r,g,b)
    
    sense.show_letter("N", pick_color())
    sleep(1)
    sense.show_letter("M", pick_color())
    sleep(1)
    sense.show_letter("D", pick_color())
    sleep(1)
