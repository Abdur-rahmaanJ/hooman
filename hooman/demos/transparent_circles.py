

import pygame
from hooman import Hooman
pygame.init()

hapi = Hooman(800, 600)


while hapi.is_running:
    hapi.background(hapi.color['white'])


    hapi.set_alpha(100)
    hapi.fill(hapi.color['red'])
    hapi.alpha_ellipse(100, 100, hapi.mouseX()//2, hapi.mouseX()//2)
    hapi.fill(hapi.color['yellow'])
    hapi.alpha_ellipse(100, 100, 100, 100)
    hapi.fill(hapi.color['green'])
    hapi.alpha_ellipse(150, 100, 100, 100)
    pygame.display.flip()

    hapi.event_loop()

pygame.quit()