'''
Kareena
https://github.com/kareena14
'''

from hooman import Hooman

import pygame

hapi = Hooman(500, 500)

len = 20
wid = 10

while hapi.is_running:
    hapi.background((0,0,0))

    hapi.fill(255, 0, 0)
    hapi.rect(250, 250,len, wid)
    hapi.flip_display()
    hapi.event_loop()

pygame.quit()

