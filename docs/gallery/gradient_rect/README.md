gradient rect

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/gradient_rect.png)

```python
from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (100, 100, 255)


while hapi.is_running:
    hapi.background(bg_col)

    hapi.gradient_rect(10, 10, 210, 100, hapi.color["black"], hapi.color["white"])

    hapi.gradient_rect(230, 10, 210, 100, hapi.color["green"], hapi.color["blue"])

    hapi.gradient_rect(10, 120, 100, 200, hapi.color["black"], hapi.color["yellow"], 1)

    hapi.gradient_rect(120, 120, 100, 200, hapi.color["red"], hapi.color["white"], 1)

    hapi.gradient_rect(340, 120, 100, 200, hapi.color["red"], hapi.color["blue"])

    hapi.gradient_rect(230, 120, 100, 200, hapi.color["yellow"], hapi.color["green"])

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()

```