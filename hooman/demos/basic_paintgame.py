import pygame
from hooman import Hooman

pygame.init()
window_width, window_height = 500,500
hapi = Hooman(window_width, window_height)
drawing = False
lines = []  # Store line segments and colors
background_color = hapi.color["white"]
draw_color = hapi.color['black']  # Current drawing color
draw_thickness = 5

def handle_events(event):
    global drawing, draw_color, lines

    if event.type == pygame.QUIT:
        hapi.is_running = False  
    elif event.type == pygame.MOUSEBUTTONDOWN:
        drawing = True
        lines.append(([(hapi.mouseX(), hapi.mouseY())], draw_color))
    elif event.type == pygame.MOUSEMOTION and drawing:
        lines[-1][0].append((hapi.mouseX(), hapi.mouseY()))
    elif event.type == pygame.MOUSEBUTTONUP:
        drawing = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:  # Reset the screen when 'R' is pressed
            lines.clear()
        elif event.key == pygame.K_b:  # Blue
            draw_color = hapi.color["black"]
        elif event.key == pygame.K_g:  # Green
            draw_color = hapi.color["green"]
        elif event.key == pygame.K_y:  # Yellow
            draw_color = hapi.color["yellow"]
        elif event.key == pygame.K_d: #red
            draw_color = hapi.color["red"]
        elif event.key == pygame.K_u: #red
            draw_color = hapi.color["blue"]
    # Add more controls for changing colors, erasing, etc.
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
      # Display instructions
    instruction_text = "Colors: B-Black, G-Green, Y-Yellow, D-Red, U-Blue | R to reset"
    text_x = 10
    text_y = window_height - 30
    hapi.fill(0)
    hapi.text(instruction_text, text_x, text_y)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
