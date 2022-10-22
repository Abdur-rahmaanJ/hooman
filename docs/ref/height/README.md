.HEIGHT
---

Contains the height of the screen


Examples
---

```python
from hooman import Hooman

hapi = Hooman(500, 500)
hapi.no_stroke()
hapi.background(0)
hapi.rect(160, 0, 80, hapi.HEIGHT)
hapi.rect(240, 0, 80, hapi.HEIGHT/8)


# pygame stuffs
while hapi.is_running:

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()
```

