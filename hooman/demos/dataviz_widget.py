"""
Author: Kherin Bundhoo
Github: https://github.com/kherin
"""

from hooman import Hooman
import itertools
import pygame

hapi = Hooman(500, 500)
size = 50

import random
import math

candy_red = (255, 110, 135)
candy_orange = (255, 185, 105)
candy_blue = (0, 240, 225)
candy_purple = (125, 25, 250)
candy_gray = (240, 240, 255)

candy_colors = itertools.cycle([candy_red, candy_orange, 
    candy_blue, candy_purple])



class ConcentricCircleGraph:
    def __init__(self, x, y, size, data: list, val_range: list):
        self.x = x 
        self.y = y 
        self.size = size 
        self.data = data
        self.val_range = val_range
        self.cols = []

        for i in self.data:
            col = next(candy_colors)
            self.cols.append(col)

    def draw(self):
        hapi.stroke_size(10)
        arc_wid_s = self.size
        arc_wid_x = self.x
        arc_wid_y = self.y

        i = -1
        for key in self.data:
            i += 1
            d = self.data[key]
            
            hapi.stroke_size(5)

            end_rad = (d/self.val_range) * (hapi.PI * 2)

            a_size = arc_wid_s - (i*30)
            pad = (arc_wid_s-a_size)//2

            hapi.stroke(candy_gray)
            hapi.arc(arc_wid_x+pad, arc_wid_y+pad, a_size, a_size, 0+(1.5*hapi.PI), hapi.PI *2+(1.5*hapi.PI))

            
            hapi.stroke(self.cols[i])
            hapi.arc(arc_wid_x+pad, arc_wid_y+pad, a_size, a_size, 0+(1.5*hapi.PI), end_rad+(1.5*hapi.PI))



data = {'x':10, 'y':20, 'z': 30, 'a': 40, 'b':50, 'c':60, 'd':70, 'e':80}
cs = ConcentricCircleGraph(80, 10, 300, data, 100)
sliders = []

for i, d in enumerate(cs.data):
    s = hapi.slider(10, 300+(i*25), 100, 5, 
        {'curve':1,
        'background_color': cs.cols[i],
        'range': [0, cs.val_range]
        })
    s.set_value(cs.data[d])
    sliders.append([s, d])

def sketch_pad():
    # add your code below
    global cs, sliders
    hapi.background((255, 255, 255))

    hapi.fill(hapi.color['black'])
    hapi.font_size(40)

    

    cs.draw()
    
    for i, s in enumerate(sliders):

        s[0].update()
        cs.data[s[1]] = s[0].value()

        t = s[1] + ' ' + str(s[0].value()) + '/'+str(round(cs.val_range, 2))
        hapi.font_size(15)
        
        hapi.text(t, s[0].x+s[0].w, s[0].y+10)

    

    hapi.flip_display()
    hapi.event_loop()


# entry point
if __name__ == "__main__":
    while hapi.is_running:
        sketch_pad()
else:
    print(__name__)
