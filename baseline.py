from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()


while 1:
    

    def pick_color():
        r = randint(180,255)
        g = randint(180,255)
        b = randint(180,255)
        return(r,g,b)
    def pick_color_text():
        r = randint(0,180)
        g = randint(0,180)
        b = randint(0,180)
        return(r,g,b)
    
    sense.show_message("Hello! We are New Media Development :)", text_colour=pick_color_text(), back_colour=pick_color())
    sleep(1)
