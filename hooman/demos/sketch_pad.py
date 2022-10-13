"""
Author: Kherin Bundhoo
Github: https://github.com/kherin
"""

from hooman import Hooman

import pygame

hapi = Hooman(500, 500)
size = 50


def sketch_pad():
    # add your code below
    hapi.background((255, 255, 255))

    hapi.fill(hapi.color['black'])
    hapi.font_size(40)
    hapi.text('Hello Hooman!', 150, 200)

    hapi.flip_display()
    hapi.event_loop()


# entry point
if __name__ == "__main__":
    print("entry point")
    while hapi.is_running:
        sketch_pad()
else:
    print(__name__)
