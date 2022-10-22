.WIDTH
---

Contains the width of the screen


Examples
---

```python
from hooman import Hooman

hapi = Hooman(500, 500)
hapi.no_stroke()
hapi.rect(0, 160, hapi.WIDTH, 80)
hapi.rect(0, 240, hapi.WIDTH/2, 80)


# pygame stuffs
while hapi.is_running:

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()
```

