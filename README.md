# hooman
~ pygame for humans

```
pip install hooman
```

# demos


![](assets/color_change.gif)

color change

```python
from hooman import Hooman

import pygame

hapi = Hooman(500, 500)

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background((255, 255, 255))

    hapi.no_stroke()
    mx = (hapi.mouseX() / hapi.WIDTH) * 255

    hapi.fill((0, mx, 0))
    for i in range(50 , 200, 60):
        hapi.rect(i, 50, 30, 30)

    hapi.fill((255, 0, 0))
    hapi.ellipse(hapi.mouseX(), hapi.mouseY(), 10, 10)

    hapi.stroke_size(1)
    hapi.stroke((255, 10, 10))
    hapi.line(0, hapi.mouseY(), hapi.mouseX()-10, hapi.mouseY())

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()

```

lines

![](assets/lines.gif)

```python
from hooman import Hooman

import pygame

hapi = Hooman(500, 500)

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background((255, 255, 255))

    hapi.stroke_size(5)
    hapi.stroke((0, 255, 0))

    for i in range(0, hapi.WIDTH, 20):
        hapi.line(i, 0, hapi.mouseX(), hapi.mouseY())

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()

```

squares

![](assets/squares.jpg)

```python
from hooman import Hooman

import pygame

hapi = Hooman(500, 500)

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events

size = 50
while hapi.is_running:
    hapi.background((255, 255, 255))

    hapi.no_stroke()
    hapi.fill((0, 255, 0))
    hapi.rect(10, 10, size, size)
    hapi.fill((255, 255, 0))
    hapi.rect(100, 100, size, size)
    hapi.fill((255, 0, 0))
    hapi.rect(100, 10, size, size)
    hapi.fill((0, 0, 255))
    hapi.rect(10, 100, size, size)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()

```

buttons


![](assets/demo_buttons.png)

```python
from hooman import Hooman, Button, Outline

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

#the function that gets called when the button is clicked on
def button_clicked(): 
    if button2.y == 250:
        button2.y = 300
    else:
        button2.y = 250


grey_style = {
    'background_color':(200, 200, 200),
    'hover_background_color':(220, 220, 220),
    'curve':0.1,
    'padding_x':5,
    'padding_y':5,
    'font_size':15
    }
button1 = hapi.button(150, 150, "Click Me",
    grey_style
)

buttonx = hapi.button(150, 10, "Click Me",
    grey_style
)

button2 = hapi.button(150, 250, "No Click Me",
    {
    'background_color':(200, 200, 200),
    'hover_background_color':(220, 220, 220),
    'outline':hapi.outline({
            'color':(200, 200, 200), 
            'amount':5
            }),
    'curve':0.3,
    'action':button_clicked,
    'padding_x':40,
    'padding_y':10,
    'font_size':15
    })

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

    if button1.update(): #if the button was clicked
        bg_col = (255, 0, 0) if bg_col == (255, 255, 255) else (255, 255, 255)
    
    # for i in range(5):
    #     x = hapi.button(10+i*80, hapi.mouseY(), "Click Me",
    #         grey_style
    #     )
    # don't use it for ui elements in loop lile the above
    # each element can also be individually
    # updated
    hapi.update_ui() 
    hapi.event_loop()

    hapi.flip_display()

    clock.tick(60)

pygame.quit()

```

# docs

coming soon ...
