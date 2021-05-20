from hooman import Hooman  # imports local not from

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
    this.background_color = hapi.color["blue"]


def button_hover_enter(this):
    # hapi.rect(this.x + this.w, 250, 100, 20)
    this.curve = 0.5
    # hapi.background(hapi.color['green'])
    global bg_col
    bg_col = hapi.color["green"]
    this.create_button()


def button_hover_exit(this):
    # hapi.rect(this.x + this.w, 250, 100, 20)
    this.curve = 0.1
    # hapi.background(hapi.color['green'])
    global bg_col
    bg_col = hapi.color["white"]
    this.create_button()


grey_style = {
    "background_color": (200, 200, 200),
    "hover_background_color": (220, 220, 220),
    "curve": 100,
    "padding_x": 5,
    "padding_y": 5,
    "font_size": 15,
    "on_click": button_clicked,
    "on_hover_enter": button_hover_enter,
    "on_hover_exit": button_hover_exit,
}


button2 = hapi.button(150, 250, 0, 0, "No Click Me", grey_style)


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

    hapi.update_ui()
    hapi.event_loop()

    hapi.flip_display()

    clock.tick(60)

pygame.quit()
