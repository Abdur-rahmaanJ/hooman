"""
Author: https://github.com/TheBigKahuna353
Edit: https://github.com/Abdur-rahmaanJ
"""

from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

# the function that gets called when the button is clicked on
def button_clicked(this):
    if this.y == 250:
        this.y = 300
    else:
        this.y = 250


grey_style = {
    "background_color": (200, 200, 200),
    "hover_background_color": (220, 220, 220),
    "curve": 0.1,
    "padding_x": 5,
    "padding_y": 5,
    "font_size": 15,
}


def button_hover_enter(this):
    hapi.set_background(hapi.color["green"])


def button_hover_exit(this):
    hapi.set_background(hapi.color["white"])


stylex = grey_style.copy()
stylex["on_hover_enter"] = button_hover_enter
stylex["on_hover_exit"] = button_hover_exit

button1 = hapi.button(150, 150, "Click Me", grey_style)

buttonx = hapi.button(150, 10, "Hover Me", stylex)

button2 = hapi.button(
    150,
    250,
    "No Click Me",
    {
        "background_color": (200, 200, 200),
        "hover_background_color": (220, 220, 220),
        "outline": True,
        "outline_color": (200, 200, 200),
        "outline_thickness": 5,
        "curve": 0.3,
        "on_click": button_clicked,
        "padding_x": 40,
        "padding_y": 10,
        "font_size": 15,
    },
)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

clock = pygame.time.Clock()

hapi.set_background(hapi.colour["white"])

while hapi.is_running:

    if button1.update():  # if the button was clicked
        bg_col = (255, 0, 0) if bg_col == (255, 255, 255) else (255, 255, 255)
        hapi.set_background(bg_col)

    # for i in range(5):
    #     x = hapi.button(10+i*80, hapi.mouseY(), "Click Me",
    #         grey_style
    #     )
    # don't use it for ui elements in loop lile the above
    # each element can also be individually
    # updated
    hapi.update_ui()
    hapi.event_loop()

    hapi.flip_display()

    clock.tick(60)

pygame.quit()
