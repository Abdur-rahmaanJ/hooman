from hooman import Hooman, Button, Outline

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255,255,255)


def button_clicked(): #the function that gets called when the button is clicked on
    if button2.y == 250:
        button2.y = 300
    else:
        button2.y = 250

button1 = Button(
    x = 150,
    y = 150,
    w = 200,
    h = 30,
    text = "Click Me",
    background = (200,200,200),
    hover_background_color = (150,150,150),
    curve_amount = 0.3
)

button2 = Button(
    x = 150,
    y = 250,
    w = 200,
    h = 30,
    text = "No Click Me",
    background = (200,200,200),
    hover_background_color = (220,220,220),
    outline = Outline(outline_color = (200,200,200)),
    curve_amount = 0.3,
    action = button_clicked
)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False

hapi.handle_events = handle_events

clock = pygame.time.Clock()

while hapi.is_running:
    hapi.background(bg_col)

    if button1.update(): #if the button was clicked
        bg_col = (255,0,0) if bg_col == (255,255,255) else (255,255,255)
    button2.update()

    hapi.event_loop()
    
    hapi.flip_display()

    clock.tick(60)

pygame.quit()
