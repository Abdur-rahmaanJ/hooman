falling stars

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/falling_stars.gif)

```python
"""Author: Bhargava N Reddy
   Github: https://github.com/reddybhargava
"""

from hooman import Hooman
import pygame
from random import sample

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

clock = pygame.time.Clock()

background_color = (0, 255, 255)
while hapi.is_running:
    hapi.background(background_color)

    num_of_stars = window_width // 100
    random_colors = sample(list(hapi.color.values()), num_of_stars)

    for y in range(0, window_height, 20):
        hapi.background(background_color)
        for i, x in enumerate(range(50, window_width, 100)):
            hapi.fill(random_colors[i])
            hapi.star(x, y, 40, 20, 10)

        hapi.flip_display()
        hapi.event_loop()
        clock.tick(10)

pygame.quit()

```