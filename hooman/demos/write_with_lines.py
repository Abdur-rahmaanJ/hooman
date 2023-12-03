"""
Author: Siddharth Kandlakunta
Github: https://github.com/SiddharthKandlakunta
"""

import pygame
from hooman import Hooman

# Initialize Pygame and Hooman
pygame.init()
window_width, window_height = 1280, 720
hapi = Hooman(window_width, window_height)

# Drawing variables
drawing = False
lines = []  # List to store line segments along with their colors
background_color = hapi.color["white"]
current_draw_color = hapi.color['black']  # Current drawing color
draw_thickness = 5

def handle_events(event):
    global drawing, current_draw_color

    if event.type == pygame.QUIT:
        hapi.is_running = False  
    elif event.type == pygame.MOUSEBUTTONDOWN:
        drawing = True
        # Start a new line segment with the current color
        lines.append(([(hapi.mouseX(), hapi.mouseY())], current_draw_color))
    elif event.type == pygame.MOUSEMOTION and drawing:
        # Append points to the current line segment
        lines[-1][0].append((hapi.mouseX(), hapi.mouseY()))
    elif event.type == pygame.MOUSEBUTTONUP:
        drawing = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
        elif event.key == pygame.K_r:
            current_draw_color = hapi.color["red"]
        elif event.key == pygame.K_g:
            current_draw_color = hapi.color["green"]
        elif event.key == pygame.K_b:
            current_draw_color = hapi.color["blue"]
        elif event.key == pygame.K_c:
            lines.clear()

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(background_color)
    for event in pygame.event.get():
        handle_events(event)

    for points, color in lines:
        hapi.stroke_size(draw_thickness)
        hapi.stroke(color)
        for i in range(1, len(points)):
            hapi.line(points[i-1][0], points[i-1][1], points[i][0], points[i][1])

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
