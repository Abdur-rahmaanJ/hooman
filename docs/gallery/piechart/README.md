piechart

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/piechart.png)

```python
from hooman import Hooman
from collections import OrderedDict
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

while hapi.is_running:
    hapi.background(bg_col)

    hapi.piechart(
        hapi.center_x - 100,
        hapi.center_y,
        100,
        [
            ["a", 20, hapi.color["red"]],
            ["b", 30, hapi.color["blue"]],
            ["c", 40, hapi.color["yellow"]],
            ["d", 60, hapi.color["green"]],
            ["e", 30, hapi.color["black"]],
        ],
    )
    hapi.piechart(
        hapi.center_x + 100,
        hapi.center_y,
        100,
        [
            ["a", 20, hapi.color["red"]],
            ["b", 30, hapi.color["blue"]],
            ["c", 40, hapi.color["yellow"]],
            ["d", 60, hapi.color["green"]],
            ["e", 30, hapi.color["black"]],
        ],
        start_rad=30,
    )

    hapi.event_loop()
    hapi.flip_display()

hapi.save('assets/piechart.png')
pygame.quit()

```