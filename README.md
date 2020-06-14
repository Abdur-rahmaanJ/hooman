# hooman ![](https://img.shields.io/pypi/dm/hooman)


~ pygame for humans

```
pip install hooman
```

discord: https://discord.gg/Q23ATve

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

from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

#the function that gets called when the button is clicked on
def button_clicked(this): 
    if this.y == 250:
        this.y = 300
    else:
        this.y = 250
        
    print(this.y)



grey_style = {
    'background_color':(200, 200, 200),
    'curve':0.1,
    'padding_x':5,
    'padding_y':5,
    'font_size':15
    }

button1 = hapi.button(150, 150, "Click Me",
    grey_style
)

def button_hover(this):
    hapi.background(hapi.color['green'])
stylex = grey_style.copy()
stylex['on_hover'] = button_hover

buttonx = hapi.button(150, 10, "Hover Me",
    stylex
)

button2 = hapi.button(150, 250, "No Click Me",
    {
    'background_color':(200, 200, 200),
    'outline':hapi.outline({
            'color':(200, 200, 200), 
            'amount':5
            }),
    'curve':0.3,
    'on_click':button_clicked,
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

transparent circles

```python
import pygame
from hooman import Hooman
pygame.init()

hapi = Hooman(800, 600)


while hapi.is_running:
    hapi.background(hapi.color['white'])


    hapi.set_alpha(100)
    hapi.fill(hapi.color['red'])
    hapi.alpha_ellipse(100, 100, hapi.mouseX()//2, hapi.mouseX()//2)
    hapi.fill(hapi.color['yellow'])
    hapi.alpha_ellipse(100, 100, 100, 100)
    hapi.fill(hapi.color['green'])
    hapi.alpha_ellipse(150, 100, 100, 100)
    pygame.display.flip()

    hapi.event_loop()

pygame.quit()
```

supershapes

![](assets/supershapes.png)

```python
from hooman import Hooman
import numpy
from math import pow
from math import sqrt
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)


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
    
    hapi.fill(hapi.color['red'])
    
    #hapi.text(n1, 10+hapi.mouseX(), 10+hapi.mouseY())
    
    hapi.smooth_star(100, 100, 100, 100)
    hapi.oil_drop(100, 250, 100, 100)
    hapi.flowing_star(100, 350, 100, 100)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
```

cross hair

![](assets/cross_hair.gif)

```python
from hooman import Hooman
from math import pow
from math import sqrt

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(bg_col)
    
    hapi.stroke(hapi.color['red'])
    hapi.stroke_size(2)
    
    mouse_coord = (hapi.mouseX(), hapi.mouseY())
    hapi.cross_hair(mouse_coord)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
```

constrain

![](assets/constrain.gif)

```python
from hooman import Hooman
import numpy
from math import pow
from math import sqrt
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events


def fake_slider(pos, x, y, width):
    size = 10
    hapi.fill(hapi.color['grey'])
    hapi.rect(x, y, width, size)
    hapi.fill((200, 200, 200))
    hapi.rect(pos, y, size, size)

while hapi.is_running:
    hapi.background(bg_col)
    
    fake_slider(hapi.mouseX(), 0, 450, hapi.WIDTH)

    reflected_val = hapi.constrain(hapi.mouseX(), 0, 500, 0, 255)
    reflected_col = (reflected_val, reflected_val, reflected_val)
    hapi.fill(reflected_col)
    hapi.rect(10, 10, 100, 100)

    reflected_val2 = hapi.constrain(hapi.mouseX(), 0, 500, 100, 200)
    fake_slider(reflected_val2, 100, 200, 100)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
```

graphs

![](assets/graphs.png)

```python
from hooman import Hooman
from collections import OrderedDict
import pygame
import random

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)



while hapi.is_running:
    hapi.background(bg_col)

    hapi.piechart(100, 100, 50, [
        ['a', 20, hapi.color['red']],
        ['b', 30, hapi.color['blue']],
        ['c', 40, hapi.color['yellow']],
        ['d', 60, hapi.color['green']],
        ['e', 30, hapi.color['black']]
    ], start_rad=20)

    hapi.barchart(
        190, 30, 200, 200, {
        "data": {"a": 10, "b": 20, "c": 90}, 
        "mouse_line": True
        }
    )

    hapi.linechart(
        30,
        270,
        200,
        100,
        {
            "data": [[0, 0], [100, 100], [200, 20], [300, 200]],
            "mouse_line": True,
            "range_y": [0, 200],
            "range_x": [0, 300],
        },
    )

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()

```

# All Demos

- [Buttons.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/Buttons.py)
- [Gradient_rect.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/Buttons.py)
- [analog_clock.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/analog_clock.py)
- [button_events.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/button_events.py)
- [color_mouse.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/color_mouse.py)
- [constrain.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/constrain.py)
- [gravity.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/gravity.py)
- [heart_arrow_curve_rect.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/heart_arrow_curve_rect.py)
- [line_mouse.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/line_mouse.py)
- [more_supershapes.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/more_supershapes.py)
- [rotation.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/rotation.py)
- [slider_color_picker.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/slider_color_picker.py)
- [sliders.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/sliders.py)
- [squares.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/squares.py)
- [star.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/star.py)
- [super_shape.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/super_shape.py)
- [text_box.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/text_box.py)
- [transparent_circles.py](https://github.com/Abdur-rahmaanJ/hooman/tree/master/hooman/demos/transparent_circles.py)

- more...

# Docs

## Attributes

## .WIDTH

- `hapi.WIDTH` is gives the width of the screen

## .HEIGHT

- `hapi.HEIGHT` is gives the height of the screen

## .is_running

- if loop is running

## .screen

still exposes a screen to draw with any pygame shape

`pygame.draw.arc(hapi.screen, (255, 0, 0), [80,10,200,200], hapi.PI, hapi.PI/2, 2)`

## Constants

## .PI

The value of pi as provided by the maths module

`pygame.draw.arc(hapi.screen, (255, 0, 0), [80,10,200,200], hapi.PI, hapi.PI/2, 2)`


## Colors, strokes & Fill

## .fill

- used for colouring next shapes
- `hapi.fill((100, 100, 100))` for r g b
- `hapi.fill(100)`  same as `hapi.fill((100, 100, 100))`

## .stroke

- used to set color of next shapes' outlines
- `hapi.stroke((100, 100, 100))` for r g b
- `hapi.stroke(100)`  same as `hapi.stroke((100, 100, 100))`

## .background

- used to set background color of screen
- `hapi.background((100, 100, 100))` for r g b
- `hapi.background(100)`  same as `hapi.background((100, 100, 100))`

## .set_background

- used to have the background drawn every frame automatically
- `hapi.set_background((100, 100, 100))`
- same as `hapi.background((100, 100, 100))`

## .color

same as

```
{
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 0, 0),
    'yellow': (255, 255, 0),
    'grey': (100, 100, 100)
}
```

also `.colors`, `.colours`, `.colour` same

## Size

## .stroke_size

- used to control thickness of lines and outlines
- `hapi.stroke_size(size)` where size is an int

## .no_stroke

- set lines and outlines thickness to 0
- `hapi.no_stroke()`
- same as `hapi.stroke_size(0)`

## .font_size

- sets font size of text
- `hapi.font_size(12)`

## Basic elements

## .rect

`hapi.rect(x, y, width, height)`
- x - x coordinate
- y - y coordinate

## .ellipse

`hapi.ellipse(x, y, width, height)`
- x - x coordinate
- y - y coordinate

## .line

`hapi.line(x1, y1, x2, y2)`

- x1 - x coordinate of first point
- y1 - y coordinate of first point
- x2 - x coordinate of second point
- y2 - y coordinate of second point

## .text

`.text(letters, x, y)`

- letters - string of chars eg. 'abcd'
- x - x coordinate
- y - y coordinate
- will convert any type passed to string
- `hapi.text(5, 10, 10)` is valid
- `hapi.text(hapi.mouseX(), 10, 10)` is valid out of the box

## .polygon

`.polygon(coords, fill=True)`

- coords is a 2d array [(0,0), (10, 10), (10, 100)]
- if fill is `False`, only the outline will be drawn
- adjust outline with `.stroke_size`

## .begin_shape

`hapi.begin_shape()` starts drawing a polygon

## .vertex

`.vertex((100, 200))`

## .end_shape

`hapi.end_shape(fill=True)` draws polygon on closing

Minimal demo of `.begin_shape`, `.vertex` and `.end_shape`

```python
from hooman import Hooman

import pygame

hapi = Hooman(500, 500)

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(hapi.color['white'])

    hapi.fill(hapi.color['blue'])
    hapi.stroke_size(4)

    hapi.begin_shape()
    hapi.vertex((0, 0))
    hapi.vertex((100, 0))
    hapi.vertex((hapi.mouseX(), hapi.mouseY()))
    hapi.end_shape()

    # same as hapi.polygon([(0, 0), (100, 0), (hapi.mouseX(), hapi.mouseY())])

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()

```

## .heart

`.heart(x, y, w, h)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height

## .star

`.star(x, y, r1, r2, npoints)`

- x - x coordinate
- y - y coordinate
- r1 - radius on the x axis, same as half width
- r2 - radius on the y axis, same as half height
- npoints - the number of points of the star, this is a minimum of 2

## .curve_rect

`.curve_rect(x, y, w, h, curve)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- curve - the percentage of curve with 0 being no curve and 100 being full curve

## .arrow

`.arrow(x, y, w, h)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height

## .alpha_ellipse

`.alpha_ellipse(x, y, w, h)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height

## .regular_polygon

`.regular_polygon(x, y, w, h, npoints, angle_offset)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- npoints - the number of points/corners of the polygon eg. 4 is a square
- angle_offset - the first point will be drawn from the top, this moves it to θ degrees anti-clockwise

## .supershape

- note see paulbourke.net/geometry/supershape/ on how to use supershape
- there is also presets for this below

`.supershape(x, y, w, h, options)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- options - optional options for the shape 

#### optional options

- n1
- n2
- n3
- m
- a
- b
- phi

## .smooth_star

note this is a preset for supershape

`.smooth_star(x, y, w, h, n1=0.20, fill=False)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- n1 - controls the smoothness of the star, this is between 0 and 1
- fill - when set to False, only the outline will be drawn

## .oil_drop

note this is a preset for supershape

`.oil_drop(x, y, w, h, n1=0.3, fill=False)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- n1 - controls the size of the drop, must be between 0 and 1
- fill - when set to False, only the outline will be drawn

## .flowing_star

note this is a preset for supershape

`.flowing_star(x, y, w, h, n1=0.3, fill=False)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- n1 - controls the inflation of the shape, must be between 0 and 1
- fill - when set to False, only the outline will be drawn

## .gradient_rect

`.gradient_rect(x, y, w, h, start_col, end_col, direction=0)`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- start_col - this is the color it starts with
- end_col - this is the color it ends with
- direction - the direction of the gradient, 0 is horizontal where it starts on the left and 1 is vertical where is starts on the top

## .cross_hair

`.cross_hair(coord)`

- coord - the x and y position of the center of the cross_hairs

## Interactivity

## .mouseX

- `hapi.mouseX()` gives the current x coordinate of the mouse

## .mouseY

- `hapi.mouseY()` gives the current y coordinate of the mouse

## Pygame specifics

## .flip_display

- is just `pygame.display.flip()` behind the scene

## .event_loop

requires

```python
def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events
```

- is put inside `hapi.is_running` loop

## .set_caption

same as `pygame.display.set_caption`

# Ui

## .update_ui

- no need to update each element if you call this
- called inside `hapi.is_running` loop
- here is when **NOT** to use it:

```python
while hapi.is_running:
    for i in range(5):
            x = hapi.button(10+i*80, hapi.mouseY(), "Click Me",
                grey_style
            )
        hapi.update_ui() 
```

## .button

Create a button with `hapi.button(x, y, text, [optional paramters])`

- `x` - x location of the button
- `y` - y location of the button
- `text` - the text on the button
- `[optional parameters]` - a dictionary of any extra options you want for the button listed below

#### Optional Parameters

- surface - the surface you want the button on, by default it is the main window
- background_color - the color of the button background
- hover_background_color - the color of the button background when the mouse is over the button
- font - the font of the text, by default it is Calibri
- font_size - the size of the text, by default it is 30
- font_colour - the colour of the text, by default it is black
- outline - when set to True, the button will have an outline when the mouse hovers over
- outline_thickness - this is the thickness of the outline
- outline_color - the colour of the outline
- outline_half - when set to True, it will create an outline for the bottom and right side of the button
- action - this is a function that gets called when the button is clicked
- action_arg - if the function given in action requires a parameter, you can use this to send to the function
- image - this should be a `pygame.Surface()` object that the button will show instead
- hover_image - this should be a `pygame.Surface()` object that the button will show when the mouse is over the button
- enlarge - this will resize the button when the mouse is over the button, this should be a bool
- enlarge_amount - this is the percentage that you want the button to resize to when the mouse is over the button (1 = no change)
- calculate_size - when set to True, this will calculate the width and height of the button from the size of the text
- padding_x - an integer that is added on to the width on both sides of the text when calculate_size is set to True
- padding_y - an integer that is added on to the height on both sides of the text when calulate_size is set to True
- dont_generate - when set to True, the button will not generate the images to put on screen, this can be handy if you want to use calculate_size without supplying text, you will need to call `button.update_text()` to generate the images before drawing
- curve - the amount of curve you want the button to have on the edges with 0 being no curve and 1 being full curve, by default it is 0
- on_hover_enter - this is a function that gets called when the mouse enters the button, the first frame it hovers over
- on_hover_exit - this is a function that gets called when the mouse exits the button, the frame once it stops hovering over
- on_click - this is a function that gets called when the mouse clicks the button, this only gets called once, even if mouse i being held down
```python

def on_hover_enter(this): # this refers to the button
    this.background_color = hapi.color['blue']

button = hapi.button(150, 250, "Click Me",
        {'on_hover_enter':on_hover_enter}
    )
```

#### Methods

- update() - this updates the button and draws it on screen, this should be called every frame
- Update_text(text) - this changes the text and recreates the button
- get_rect() - this returns a pygame.Rect of the button
- width() - this returns the width of the button
- height() - this returns the height of the button
- create_button() - this applies any changes to the button

## .slider

`.slider(x, y, w, h, [optional parameters])`

- x - x coordinate
- y - y coordinate
- w - width
- h - height
- optional parameters - a dictionary of optional options 

#### optional parameters

- background_color - the background color of the slider
- slider_width - the width of slider, by default it is the same as the height
- slider_color - the color of the slider
- starting_value - the starting value of the slider, by default it is in the middle of the range
- value_range - the range that the slider ranges between, by default it is between 0 and 1

#### Methods

- update() - this updates the slider and draws it on screen, this should be called every frame
- value() - this returns the current value of the slider
- set_value(value) - given a integer or float, this sets the value and moves the slider

## .textbox

`.textbox(x, y, w, h=0, [optional parameters])`

- x - x coordinate
- y - y coordinate
- w - width
- h - height of each line
- optional parameters - a dictionary of optional options

#### optional parameters

- lines - the amount of lines the textbox has
- text - the starting text it has
- background_color - the color of the background
- font_size - the size of the text font
- font - the font of the text
- text_color - the color of the text
- surface - the surface to put the textbox on, by default it is the main window
- margin - the offset from the left side that the text starts from
- cursor - a cursor to show you where you are typing, by default it is on
- Enter_action - a function that gets called when enter is pressed
- calculateSize - when True, it will calculate the height based off the height of the text

#### Methods

- update() - this updates the textbox and draws it on screen, this should be called every frame
- get_lines(lines=1, return_as_string=False) - this returns the text in the textbox, lines can be the line number (starting from 1) or a range of lines eg. `(1,4)` gets lines 1 to 4, when return_as_string is False, it will return each line in a list
- key_down(event) - when a KEYDOWN event happens, giving it to this method updates the textbox
```
def handle_events(event):
    if event.type == pygame.KEYDOWN:
        .keydown(event)
```


