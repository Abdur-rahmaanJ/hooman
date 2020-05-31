import pygame
from math import cos
from math import sin
from math import radians
import numpy

def star(hapi, x, y, r1, r2, npoints):
    '''
    https://processing.org/examples/star.html
    '''
    if npoints < 2:
        npoints = 2
    angle = hapi.PI*2 / npoints
    half_angle = angle / 2
    hapi.begin_shape()
    for a in numpy.arange(0, hapi.PI*2, angle):
        sx = x + cos(a) * r2
        sy = y + sin(a) * r2
        hapi.vertex((sx, sy))
        sx = x + cos(a+half_angle) * r1
        sy = y + sin(a+half_angle) * r1
        hapi.vertex((sx, sy))
    hapi.end_shape()


def alpha_ellipse(hapi, x, y, w, h):
    # https://github.com/furas
    # https://stackoverflow.com/questions/59293057/how-to-make-transparent-pygame-draw-circle/
    surface1 = hapi.screen.convert_alpha()
    # surface1.fill([0,0,0,0])
    shape_fill = hapi._fill + (hapi._alpha,)
    pygame.draw.ellipse(surface1, shape_fill, (x, y, w, h))
    hapi.screen.blit(surface1, (0,0))

def curve_rect(hapi, x, y, width, height, curve):
    curve /= 200
    curve = min(max(curve, 0), 1)
    curve *= min(width, height)
    curve = int(curve)
    shape_fill = hapi._fill + (hapi._alpha,)
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(surf, shape_fill, (0, curve, width, height - 2 * curve))
    pygame.draw.rect(surf, shape_fill, (curve, 0, width - 2 * curve, height))
    pygame.draw.circle(surf, shape_fill, (curve, curve), curve)
    pygame.draw.circle(surf, shape_fill, (width - curve, curve), curve)
    pygame.draw.circle(surf, shape_fill, (curve, height - curve), curve)
    pygame.draw.circle(surf, shape_fill, (width - curve, height - curve), curve)
    hapi.screen.blit(surf,(x,y))


def arrow(hapi, x, y, size, angle):
    '''
    https://www.reddit.com/r/pygame/comments/glomfa/drawing_polygons/fr0ig8y/?context=3
    '''
    start = pygame.Vector2(x, y)
    left = pygame.Vector2(-1, -2)
    top = pygame.Vector2(0, -1)
    right = pygame.Vector2(1, -2)
    hapi.begin_shape()
    hapi.vertex(start + left.rotate(angle) * size)
    hapi.vertex(start + top.rotate(angle) * size)
    hapi.vertex(start + right.rotate(angle) * size)
    hapi.vertex(start)
    hapi.end_shape()


def heart(hapi, x, y, w, h):
    '''
    http://www.mathematische-basteleien.de/heart.htm
    '''
    step_size = 1000 / (hapi.PI / 2)
    curve_h = max(int(h*0.6), 1)
    circle_h = max(int(h*0.4), 1)
    wr = max(w//2, 1)
    hr = max(curve_h//2, 1)

    hapi.begin_shape()
    for i in range(-1000, 1000, 1):
        if i == 0:
            continue
        hapi.vertex((int(x + wr + (sin(i/step_size)*wr)), y + circle_h//2 + hr + i//(1000/hr)))
    hapi.vertex((x+w, y+circle_h//2))
    hapi.end_shape()

    hapi.begin_shape()
    for i in range(-1000, 1000, 1):
        if i == 0:
            continue
        hapi.vertex((int(x + w*2 - wr - (sin(i/step_size)*wr)), y + circle_h//2 + hr + i//(1000/hr)))
    hapi.vertex((x+w, y + circle_h//2))
    hapi.end_shape()

    hapi.ellipse(x, y, w, circle_h)
    hapi.ellipse(x + w, y, w, circle_h)   


def regular_polygon(hapi, x, y, w, h, n, rotation):
    if n < 3:
        n = 3
    
    midpoint = pygame.Vector2(x + w//2, y + h//2)
    
    hapi.begin_shape()
    
    for angle in range(0, 360, 360//n):
        angle = radians(angle)
        d = pygame.Vector2(-2*sin(angle)*w, -2*cos(angle)*h).rotate(rotation)
        
        hapi.vertex(midpoint + d)
    
    hapi.end_shape()
