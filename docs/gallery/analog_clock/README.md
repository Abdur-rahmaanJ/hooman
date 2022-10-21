analog clock

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/analog_clock.gif)


```python
from hooman import Hooman
import numpy
from math import pow
from math import sqrt
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


r_slider = hapi.slider(50, 330, 400, 10, {"range": [0, 100]})

offsetx = 200
offsety = 200

while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)

    hapi.fill(hapi.color["red"])
    hapi.stroke(hapi.color["black"])

    hapi.text("r value: {}".format(r_slider.value()), 50, 330 - 15)

    for i in range(13):
        x = (
            offsetx
            + hapi.cos(hapi.constrain(i, 0, 12, 0, hapi.PI * 2) - hapi.PI * 0.5)
            * r_slider.value()
        )
        y = (
            offsety
            + hapi.sin(hapi.constrain(i, 0, 12, 0, hapi.PI * 2) - hapi.PI * 0.5)
            * r_slider.value()
        )
        if i != 0:
            hapi.text(i, x, y)

    # - hapi.PI*0.5 to put display in place
    pointxh = offsetx + hapi.cos(
        hapi.constrain(hapi.hour(), 0, 12, 0, hapi.PI * 2) - hapi.PI * 0.5
    ) * (r_slider.value() - 40)
    pointyh = offsetx + hapi.sin(
        hapi.constrain(hapi.hour(), 0, 12, 0, hapi.PI * 2) - hapi.PI * 0.5
    ) * (r_slider.value() - 40)

    pointxm = offsetx + hapi.cos(
        hapi.constrain(hapi.minute(), 0, 60, 0, hapi.PI * 2) - hapi.PI * 0.5
    ) * (r_slider.value() - 30)
    pointym = offsetx + hapi.sin(
        hapi.constrain(hapi.minute(), 0, 60, 0, hapi.PI * 2) - hapi.PI * 0.5
    ) * (r_slider.value() - 30)

    pointxs = offsetx + hapi.cos(
        hapi.constrain(hapi.second(), 0, 60, 0, hapi.PI * 2) - hapi.PI * 0.5
    ) * (r_slider.value() - 20)
    pointys = offsetx + hapi.sin(
        hapi.constrain(hapi.second(), 0, 60, 0, hapi.PI * 2) - hapi.PI * 0.5
    ) * (r_slider.value() - 20)

    hapi.stroke_size(5)
    hapi.line(offsetx, offsety, pointxh, pointyh)
    hapi.stroke_size(4)
    hapi.line(offsetx, offsety, pointxm, pointym)
    hapi.stroke_size(2)
    hapi.line(offsetx, offsety, pointxs, pointys)

    r_slider.update()

    hapi.flip_display()
    hapi.event_loop()


pygame.quit()
```