from hooman import Hooman
import pygame

hapi = Hooman(700, 700)

"""
TESTS completed:

All Widgets:
    __str__
    image
    on_enter
    on_exit
    curve
    transparent background


Button
    outline
    half outline
    enlarge
    font
    center
    calculate_size -> only works if no image is used (perhaps unneccessary)(or chnage name to adjust size with text?)
    padding
    text
    click - through .update() and .clicked 

Slider
    slider_image
    both curve
    slider sizes
    range
    step
    starting value
    direction

TextBox
    text
    cursor
    padding
    typing using events
    curve - kinda works
    arrow keys
    backspace wrapping lines 
    new line
    get lines

"""
image = pygame.Surface((200, 40))
image.fill((130, 130, 130))
pygame.draw.line(image, (0, 0, 0), (0, 20), (200, 20), 5)

image2 = pygame.Surface((20, 40), pygame.SRCALPHA)
image2.fill((180, 180, 180, 100))


params = {
    "background_color": (180, 180, 180),
    "hover_background_color": (220, 220, 220),
    "calculate_size": True,
    
}

button = hapi.button(100, 100, 30, 20, "Add", params)

pri_slider = hapi.slider(160, 250, 200, 20, {
    'range': [1, 3],
    'step': 1,
    'starting_value': 1,
    'curve': 0.5,
    "slider_curve": 0.5,
    "slider_width": 20,
    "background_color": (200, 200, 200),
    "slider_color": (150,150,150),
})


hapi.set_background(hapi.color['white'])
while hapi.is_running:

    if button.update():
        print("clicked")

    pri_slider.update()


    hapi.flip_display()
    hapi.event_loop()
