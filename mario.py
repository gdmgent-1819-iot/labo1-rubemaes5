from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

r = (255, 0, 0)
bl = (0, 0, 255)
br = (80, 40, 10)
s = (255, 237, 198)
e = (0,0,0)

scene1 = [
    e, e, r, r, r, r, e, e,
    e, e, r, r, r, r, r, e,
    e, e, s, bl, s, bl, e, e,
    e, e, s, s, br, br, e, e,
    s, r, bl, r, r, bl, r, s,
    e, e, bl, bl, bl, bl, e, e,
    e, e, bl, bl, bl, bl, e, e,
    e, e, br, e, e, br, e, e, 
    ]
scene2 = [
    
    e, e, r, r, r, r, r, e,
    e, e, s, bl, s, bl, e, e,
    e, e, s, s, br, br, e, e,
    s, r, bl, r, r, bl, r, s,
    e, e, bl, bl, bl, bl, e, e,
    e, e, bl, bl, bl, bl, e, e,
    e, e, br, e, e, br, e, e,
    e, e, e, e, e, e, e, e, 
    ]
scene3 = [
    e, e, s, bl, s, bl, e, e,
    e, e, s, s, br, br, e, e,
    s, r, bl, r, r, bl, r, s,
    e, e, bl, bl, bl, bl, e, e,
    e, e, bl, bl, bl, bl, e, e,
    e, e, br, e, e, br, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e, 
    ]
scene4 = [
    e, e, s, s, br, br, e, e,
    s, r, bl, r, r, bl, r, s,
    e, e, bl, bl, bl, bl, e, e,
    e, e, bl, bl, bl, bl, e, e,
    e, e, br, e, e, br, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e, 
    ]
sense.clear()
while True:
    sense.set_pixels(scene1)
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                sense.set_pixels(scene1)
                sleep(0.1)
                sense.set_pixels(scene2)
                sleep(0.1)
                sense.set_pixels(scene3)
                sleep(0.1)
                sense.set_pixels(scene4)
                sleep(0.1)
                sense.set_pixels(scene3)
                sleep(0.1)
                sense.set_pixels(scene2)
                sleep(0.1)
                sense.set_pixels(scene1)
                sleep(0.1)
            
