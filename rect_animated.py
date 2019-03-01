from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

while True:


    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    c = (r, g, b)
    e = (0 ,0 ,0)

    scene0 = [
        c, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        ]
    scene1 = [
        c, c, e, e, e, e, e, e,
        c, c, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        ]
    scene2 = [
        c, c, c, e, e, e, e, e,
        c, e, c, e, e, e, e, e,
        c, c, c, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        ]
    scene3 = [
        c, c, c, c, e, e, e, e,
        c, e, e, c, e, e, e, e,
        c, e, e, c, e, e, e, e,
        c, c, c, c, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        ]
    scene4 = [
        c, c, c, c, c, e, e, e,
        c, e, e, e, c, e, e, e,
        c, e, e, e, c, e, e, e,
        c, e, e, e, c, e, e, e,
        c, c, c, c, c, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        ]
    scene5 = [
        c, c, c, c, c, c, e, e,
        c, e, e, e, e, c, e, e,
        c, e, e, e, e, c, e, e,
        c, e, e, e, e, c, e, e,
        c, e, e, e, e, c, e, e,
        c, c, c, c, c, c, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        ]
    scene6 = [
        c, c, c, c, c, c, c, e,
        c, e, e, e, e, e, c, e,
        c, e, e, e, e, e, c, e,
        c, e, e, e, e, e, c, e,
        c, e, e, e, e, e, c, e,
        c, e, e, e, e, e, c, e,
        c, c, c, c, c, c, c, e,
        e, e, e, e, e, e, e, e,
        ]
    scene7 = [
        c, c, c, c, c, c, c, c,
        c, e, e, e, e, e, e, c,
        c, e, e, e, e, e, e, c,
        c, e, e, e, e, e, e, c,
        c, e, e, e, e, e, e, c,
        c, e, e, e, e, e, e, c,
        c, e, e, e, e, e, e, c,
        c, c, c, c, c, c, c, c, 
        ]
    sense.set_pixels(scene0)
    sleep(0.1)
    sense.set_pixels(scene1)
    sleep(0.1)
    sense.set_pixels(scene2)
    sleep(0.1)
    sense.set_pixels(scene3)
    sleep(0.1)
    sense.set_pixels(scene4)
    sleep(0.1)
    sense.set_pixels(scene5)
    sleep(0.1)
    sense.set_pixels(scene6)
    sleep(0.1)
    sense.set_pixels(scene7)
    sleep(0.1)
    sense.set_pixels(scene6)
    sleep(0.1)
    sense.set_pixels(scene5)
    sleep(0.1)
    sense.set_pixels(scene4)
    sleep(0.1)
    sense.set_pixels(scene3)
    sleep(0.1)
    sense.set_pixels(scene2)
    sleep(0.1)
    sense.set_pixels(scene1)
    sleep(0.1)
    sense.set_pixels(scene0)
    sleep(0.1)
