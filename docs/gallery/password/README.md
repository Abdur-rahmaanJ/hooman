lock pattern password widget

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/password.gif)


```python
from hooman import Hooman
from hooman.formula import distance
from hooman.ui import Button

import pygame

hapi = Hooman(500, 500)


lp = hapi.lock_pattern([1, 2, 3, 4, 5, 6, 7], row=3)

while hapi.is_running:
    hapi.background(255)

    # --- draw lock pattern ---
    # lp.update()

    hapi.update_ui()

    hapi.flip_display()
    hapi.event_loop()

```