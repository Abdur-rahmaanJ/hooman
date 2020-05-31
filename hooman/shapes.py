import pygame
import numpy

from math import pi
from math import cos
from math import sin
from math import radians


def star(hapi, x, y, r1, r2, npoints, rotation):
    '''
    https://processing.org/examples/star.html
    '''
    if npoints < 2:
        npoints = 2
    angle = hapi.PI*2 / npoints
    half_angle = angle / 2
    hapi.begin_shape()
    rotation = radians(rotation)
    for a in numpy.arange(0+rotation, hapi.PI*2 + rotation, angle):
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

def curve_rect(hapi, x, y, width, height, curve, rotation):
    curve /= 200
    curve = min(max(curve, 0), 1)
    curve *= min(width, height)
    curve = int(curve)
    
    print(curve)
    
    shape_fill = hapi._fill + (hapi._alpha,)
    '''
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(surf, shape_fill, (0, curve, width, height - 2 * curve))
    pygame.draw.rect(surf, shape_fill, (curve, 0, width - 2 * curve, height))
    pygame.draw.circle(surf, shape_fill, (curve, curve), curve)
    pygame.draw.circle(surf, shape_fill, (width - curve, curve), curve)
    pygame.draw.circle(surf, shape_fill, (curve, height - curve), curve)
    pygame.draw.circle(surf, shape_fill, (width - curve, height - curve), curve)
    hapi.screen.blit(surf,(x,y))
    '''
    regular_polygon(hapi, x + width//2, y + height//2, width, height - 2*curve, 4, rotation, 0)
    regular_polygon(hapi, x + width//2, y + height//2, width - 2*curve, height, 4, rotation, 0)
    top_left = pygame.Vector2(-width//2,-height//2).rotate(rotation)
    top_right = pygame.Vector2(width//2,-height//2).rotate(rotation)
    bot_right = pygame.Vector2(width//2,height//2).rotate(rotation)
    bot_left = pygame.Vector2(-width//2,height//2).rotate(rotation)
    #pygame.draw.circle(hapi.screen,shape_fill, (x + curve, 
                                                #y + curve), curve//2)
    #pygame.draw.circle(hapi.screen,shape_fill, (int(top_right[0]) + x + width//2, 
                                                #int(top_right[1]) + y + height//2), curve)
    #pygame.draw.circle(hapi.screen,shape_fill, (int(bot_left[0]) + x + width//2, 
                                                #int(bot_left[1]) + y + height//2), curve)
    #pygame.draw.circle(hapi.screen,shape_fill, (int(bot_right[0]) + x + width//2, 
                                                #int(bot_right[1]) + y + height//2), curve)
    
    


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


def regular_polygon(hapi, x, y, w, h, n, rotation, angle_offset = 0):
    if n < 3:
        n = 3
    
    midpoint = pygame.Vector2(x, y)
    #print(midpoint[0] - w//2, midpoint[1] - h//2)
    
    print("before:",w)
    w = (sin(angle_offset)*w//2)//(hapi.PI/2)
    h = h * cos(angle_offset)
    print("after:",w)
    
    hapi.begin_shape()
    
    for angle in range(0, 360, 360//n):
        angle = radians(angle + angle_offset)
        d = pygame.Vector2(-sin(angle)*w//2, -cos(angle)*h//2).rotate(rotation)
        
        hapi.vertex(midpoint + d)
    
    for angle in range(0, 360, 1):
        angle = radians(angle + angle_offset)
        d = pygame.Vector2(-sin(angle)*w//2, -cos(angle)*h//2).rotate(rotation)
        pygame.draw.rect(hapi.screen, (0,255,0), (midpoint[0] + d[0], midpoint[1] + d[1], 5, 5))
    
    hapi.end_shape()




#
# Supershapes from http://paulbourke.net/geometry/supershape/
# With help from Daniel Shiefman
#

def r_val(theta, n1, n2, n3, m, a, b):
    if n1 == 0:
        n1 = 0.1
    part1 =  (1/a) * cos(theta * m/4) 
    part1 = abs(part1)
    part1 = pow(part1, n2)

    part2 =  (1/b) * sin(theta * m/4) 
    part2 = abs(part2)
    part2 = pow(part2, n3)

    part3 = pow(part1 + part2, 1/n1)

    # returning r

    if part3 == 0:
        return 0

    return 1/part3


def supershape(hapi, x_coord, y_coord, size_x, size_y, param_options, fill=False):
    options = {
        'n1':0.20,
        'n2':1.7,
        'n3':1.7,
        'm': 5,
        'a':1,
        'b':1,
        'phi':2
    }

    
    pivot_x = x_coord
    pivot_y = y_coord

    options.update(param_options)

    n1 = options['n1']
    n2 = options['n2']
    n3 = options['n3']
    m = options['m']
    a = options['a']
    b = options['b']
    phi = options['phi']
    
    
    hapi.begin_shape()
    for angle in numpy.arange(0, hapi.PI*phi, 0.01):
        r = r_val(angle, n1, n2, n3, m, a, b)
        x = pivot_x + size_x * r * hapi.cos(angle)
        y = pivot_y + size_y * r * hapi.sin(angle)

        hapi.vertex((x, y))
    hapi.end_shape(fill=fill)


def smooth_star(hapi, x_coord, y_coord, size_x, size_y, n1=0.20, fill=False):
    '''
    n1 between 0 and 1
    '''
    smooth_star_options = {
        'n1':0.20,
        'n2':1.7,
        'n3':1.7,
        'm': 5,
        'a':1,
        'b':1,
        'phi':2
    }
    smooth_star_options['n1'] = n1
    supershape(hapi, x_coord, y_coord, size_x, size_y, smooth_star_options, fill=fill)

def oil_drop(hapi, x_coord, y_coord, size_x, size_y, fill=False):
    '''
    n1 between 0 and 1
    '''
    oil_drop_options = {
        'n1':0.3,
        'n2':0.3,
        'n3':0.3,
        'm': 1/6,
        'a':1,
        'b':1,
        'phi':12
    }
    supershape(hapi, x_coord, y_coord, size_x, size_y, oil_drop_options, fill=fill)



def flowing_star(hapi, x_coord, y_coord, size_x, size_y, fill=False):
    flowing_star_options = {
        'n1':0.3,
        'n2':0.3,
        'n3':0.3,
        'm': 7/6,
        'a':1,
        'b':1,
        'phi':12
    }
    supershape(hapi, x_coord, y_coord, size_x, size_y, flowing_star_options, fill=fill)