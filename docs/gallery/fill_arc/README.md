fill arc

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/fill_arc.gif)


```python
from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

import hooman

while hapi.is_running:
    hapi.background(bg_col)

    hapi.fill(hapi.color["red"])

    d = int(hapi.dist((hapi.mouseX(), hapi.mouseY()), (hapi.center_x, hapi.center_y)))
    hapi.fill_arc(hapi.center_x, hapi.center_y, d, 90, 0)

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()
```