.TAU
---

TAU is a mathematical constant with the value 6.2831855. It is the circle constant relating the circumference of a circle to its linear dimension, the ratio of the circumference of a circle to its radius. It is useful in combination with trigonometric functions such as sin() and cos().

Examples
---

```python
from hooman import Hooman

hapi = Hooman(500, 500)

hapi.background(255)

x = 10
y = 10
d = 100
hapi.stroke_size(5)

hapi.stroke(255, 0, 0)
hapi.arc(x, y, d, d, 0, hapi.TAU);

x += 100
hapi.stroke(0, 255, 0)
hapi.arc(x, y, d, d, 0, hapi.PI);

x += 100
hapi.stroke(0, 0, 255)
hapi.arc(x, y, d, d, 0, hapi.HALF_PI);

x += 100
hapi.stroke(0)
hapi.arc(x, y, d, d, 0, hapi.QUARTER_PI);


# pygame stuffs
while hapi.is_running:

    hapi.event_loop()
    hapi.flip_display()

hapi.pygame.quit()
```