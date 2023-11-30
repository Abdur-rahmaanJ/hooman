

<p align="center">
  <br>
  <a href="https://github.com/Abdur-rahmaanJ/hooman"><img src="https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/hooman.png" alt="Hooman"></a>
  <br>
</p>


# hooman [![Downloads](https://static.pepy.tech/badge/hooman)](https://pepy.tech/project/hooman) ![PyPI](https://img.shields.io/pypi/v/hooman)

~ pygame for humans [ [docs](https://abdur-rahmaanj.github.io/hooman) | [gallery](https://abdur-rahmaanj.github.io/hooman/gallery) ]

```
pip install hooman
```

demos

```
python -m hooman.demos # see all demos
python -m hooman.demos.sliders # select one
```

join discord: https://discord.gg/Q23ATve

The package for clearer, shorter and cleaner PyGame codebases!

Featured by [r/Pygame](https://www.reddit.com/r/pygame/)

Fun fact: Codementor.io [tweeted about Hooman](https://twitter.com/CodementorIO/status/1306295790441246725?s=20) tagged #LearnPython #100DaysOfCode

# Tutorials

- [Building A Color Picker](https://dev.to/abdurrahmaanj/building-a-color-picker-in-pygame-using-hooman-307m)
- [Display most frequent words using PyGame](https://www.pythonkitchen.com/display-most-frequent-words-python-pygame/)
- [Realtime CPU monitor using PyGame](https://www.pythonkitchen.com/realtime-cpu-monitor-using-pygame/)
- [Android's Lock Screen in Pygame](https://www.codementor.io/@abdurrahmaanj/android-s-lock-screen-pattern-in-pygame-1y12ejsg3s)


# Getting Started

hooman makes developing with pygame easy by having everything in 1 object!

```python
from hooman import Hooman

hapi = Hooman(width, height)

while hapi.is_running:

    hapi.flip_display()
    hapi.event_loop()
```

# Playground

You can use the *[jurigged](https://github.com/breuleux/jurigged)* package to reload your code while you update your file. The latter will give you a quick visual feedback while coding.

## Example

```
jurigged hooman/hooman/demos/sketch_pad.py
```
# Contributing Notes

-   **Demos**: Include your name and Github URL in a docstring at the top of the demo file

# [features](new_features.md)

- record video
- screenshot
- integrate with other pygame codes
- save to svg
- keyword argument same as dictionary

# Docs

## Attributes

## .WIDTH

-   `hapi.WIDTH` is gives the width of the screen

## .HEIGHT

-   `hapi.HEIGHT` is gives the height of the screen

## .is_running

-   if loop is running

## .screen

still exposes a screen to draw with any pygame shape

`pygame.draw.arc(hapi.screen, (255, 0, 0), [80,10,200,200], hapi.PI, hapi.PI/2, 2)`

## Constants

## .PI

The value of pi as provided by the maths module

`pygame.draw.arc(hapi.screen, (255, 0, 0), [80,10,200,200], hapi.PI, hapi.PI/2, 2)`

## Colors, strokes & Fill

## .fill

-   used for colouring next shapes
-   `hapi.fill((100, 100, 100))` for r g b
-   `hapi.fill(100)` same as `hapi.fill((100, 100, 100))`

## .stroke

-   used to set color of next shapes' outlines
-   `hapi.stroke((100, 100, 100))` for r g b
-   `hapi.stroke(100)` same as `hapi.stroke((100, 100, 100))`

## .background

-   used to set background color of screen
-   `hapi.background((100, 100, 100))` for r g b
-   `hapi.background(100)` same as `hapi.background((100, 100, 100))`

## .set_background

-   used to have the background drawn every frame automatically
-   `hapi.set_background((100, 100, 100))`
-   same as `hapi.background((100, 100, 100))`

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

-   used to control thickness of lines and outlines
-   `hapi.stroke_size(size)` where size is an int

## .no_stroke

-   set lines and outlines thickness to 0
-   `hapi.no_stroke()`
-   same as `hapi.stroke_size(0)`

## .font_size

-   sets font size of text
-   `hapi.font_size(12)`

## Basic elements

## .rect

`hapi.rect(x, y, width, height)`

-   x - x coordinate
-   y - y coordinate

## .ellipse

`hapi.ellipse(x, y, width, height)`

-   x - x coordinate
-   y - y coordinate

## .line

`hapi.line(x1, y1, x2, y2)`

-   x1 - x coordinate of first point
-   y1 - y coordinate of first point
-   x2 - x coordinate of second point
-   y2 - y coordinate of second point

## .text

`.text(letters, x, y)`

-   letters - string of chars eg. 'abcd'
-   x - x coordinate
-   y - y coordinate
-   will convert any type passed to string
-   `hapi.text(5, 10, 10)` is valid
-   `hapi.text(hapi.mouseX(), 10, 10)` is valid out of the box

## .polygon

`.polygon(coords, fill=True)`

-   coords is a 2d array [(0,0), (10, 10), (10, 100)]
-   if fill is `False`, only the outline will be drawn
-   adjust outline with `.stroke_size`

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

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height

## .star

`.star(x, y, r1, r2, npoints)`

-   x - x coordinate
-   y - y coordinate
-   r1 - radius on the x axis, same as half width
-   r2 - radius on the y axis, same as half height
-   npoints - the number of points of the star, this is a minimum of 2

## .curve_rect

`.curve_rect(x, y, w, h, curve)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height
-   curve - the percentage of curve with 0 being no curve and 100 being full curve

## .arrow

`.arrow(x, y, w, h)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height

## .alpha_ellipse

`.alpha_ellipse(x, y, w, h)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height

## .regular_polygon

`.regular_polygon(x, y, w, h, npoints, angle_offset)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height
-   npoints - the number of points/corners of the polygon eg. 4 is a square
-   angle_offset - the first point will be drawn from the top, this moves it to θ degrees anti-clockwise

## .supershape

-   note see paulbourke.net/geometry/supershape/ on how to use supershape
-   there is also presets for this below

`.supershape(x, y, w, h, options)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height
-   options - optional options for the shape

#### optional options

-   n1
-   n2
-   n3
-   m
-   a
-   b
-   phi

## .smooth_star

note this is a preset for supershape

`.smooth_star(x, y, w, h, n1=0.20, fill=False)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height
-   n1 - controls the smoothness of the star, this is between 0 and 1
-   fill - when set to False, only the outline will be drawn

## .oil_drop

note this is a preset for supershape

`.oil_drop(x, y, w, h, n1=0.3, fill=False)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height
-   n1 - controls the size of the drop, must be between 0 and 1
-   fill - when set to False, only the outline will be drawn

## .flowing_star

note this is a preset for supershape

`.flowing_star(x, y, w, h, n1=0.3, fill=False)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height
-   n1 - controls the inflation of the shape, must be between 0 and 1
-   fill - when set to False, only the outline will be drawn

## .gradient_rect

`.gradient_rect(x, y, w, h, start_col, end_col, direction=0)`

-   x - x coordinate
-   y - y coordinate
-   w - width
-   h - height
-   start_col - this is the color it starts with
-   end_col - this is the color it ends with
-   direction - the direction of the gradient, 0 is horizontal where it starts on the left and 1 is vertical where is starts on the top

## .cross_hair

`.cross_hair(coord)`

-   coord - the x and y position of the center of the cross_hairs

## Interactivity

## .mouseX

-   `hapi.mouseX()` gives the current x coordinate of the mouse

## .mouseY

-   `hapi.mouseY()` gives the current y coordinate of the mouse

## Pygame specifics

## .flip_display

-   is just `pygame.display.flip()` behind the scene

## .event_loop

requires

```python
def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events
```

-   is put inside `hapi.is_running` loop

## .set_caption

same as `pygame.display.set_caption`

# Ui

## .update_ui

-   no need to update each element if you call this
-   called inside `hapi.is_running` loop
-   here is when **NOT** to use it:

```python
while hapi.is_running:
    for i in range(5):
            x = hapi.button(10+i*80, hapi.mouseY(), "Click Me",
                grey_style
            )
        hapi.update_ui()
```


## .button

Create a button with `hapi.button(x, y, w, h, text, [optional paramters])`

-   `x` - x location of the button
-   `y` - y location of the button
-   `w` - width of the button
-   `h` - height of the button
-   `text` - the text on the button
-   `[optional parameters]` - a dictionary of any extra options you want for the button listed below

#### Optional Parameters
```python
    "hover_background_color": None
    "outline": False
    "outline_thickness": 0
    "hover_outline_thickness": None
    "outline_color": (0, 0, 0)
    "outline_half": False
    "hover_image": None
    "enlarge": False
    "enlarge_amount": 1.1
    "calculate_size": False
    "dont_generate": False
    "padding_x": 0
    "padding_y": 0
    all options from Base Ui Widget
```
plus all parameters from [Base Widget](#Base-Widget)


```python
def on_hover_enter(btn):
    btn.background_color = hapi.color['blue']

button = hapi.button(150, 250, "Click Me",
        {'on_hover_enter':on_hover_enter}
    )
```

#### Methods

-   `update()` -> bool - this updates the button and draws it on screen, this should be called every frame, return whether the button was clicked
-   `Update_text(text)` - this changes the text and recreates the button
-   `create_button()` - this applies any changes to the button

## .slider

`.slider(x, y, w, h, [optional parameters])`

-   `x` - x coordinate
-   `y` - y coordinate
-   `w` - width
-   `h` - height
-   optional parameters - a dictionary of optional options

#### optional parameters
```python
    "slider_width": None
    "slider_color": (200, 200, 200)
    "starting_value": None
    "range": [0, 1]
    "slider_height": None
    "step": 0
    "direction": "horizontal"
    "slider_image": None
    "slider_curve": 0
```
plus all parameters from [Base Widget](#Base-Widget)
#### Methods

-   `update()` -> float - this updates the slider and draws it on screen, this should be called every frame, return the value
-   `value()` - this returns the current value of the slider
-   `set_value(value)` - given a integer or float, this sets the value and moves the slider

## .slider_with_text

`.slider_with_text(slider, [optianl parameters])`

- `slider` - a `.slider` widget
- optional parameters - a dictionary of optional options

#### optional parameters
```python
    "font": "calibri"
    "font_size": 20
    "font_color": (0, 0, 0)
    "padding_y": 2
    "padding_x": 0
    "pivot": "top_left"
    "accuracy": 0
```
plus all parameters from [Base Widget](#Base-Widget)
#### Methods

- `update()` - this updates the text and the given slider
- `value()` - this returns the value of the given slider

## .scroll

`.scroll([optional parameters])`

-   optional parameters - a dictionary of optional options

#### optional parameters
```python
    "starting_x": 0
    "starting_y": 0
    "range_x": 0
    "range_y": 0
    "bar_color": (200, 200, 200)
    "slider_color": (150, 150, 150)
```
#### Methods

-`update()` - this updates the scroll widget

#### how to use the scroll

- use `scroll_widget[0]` to get the amount of horizontal scroll and
`scroll_widget[1]` to get the amount of vertical scroll

eg.
```python
scroll_obj = hapi.scroll(params)

while hapi.running:
    hapi.rect(100 + scroll_obj[0], 100 + scroll_obj[1], 50, 50)
    scroll_obj.update()
```


## .textbox

`.textbox(x, y, w, h=0, [optional parameters])`

-   `x` - x coordinate
-   `y` - y coordinate
-   `w` - width
-   `h` - height of each line
-   optional parameters - a dictionary of optional options

#### optional parameters

```python
   "max_lines": 1
    "text": "" # this can be a list containg a string of each line or a single string containing '\n's
    "padding_x": 2
    "padding_y": 2
    "cursor": True
    "on_return": None
    "calculate_size": False
    "typing": True
```
#### Methods

-   `update()` - this updates the textbox and draws it on screen, this should be called every frame
-   `get_lines(lines=1, return_as_string=False)` - this returns the text in the textbox, lines can be the line number (starting from 1) or a range of lines eg. `(1,4)` gets lines 1 to 4, when return_as_string is False, it will return each line in a list
-   `key_down(event)` - when a KEYDOWN event happens, giving it to this method updates the textbox

```python
def handle_events(event):
    if event.type == pygame.KEYDOWN:
        my_textbox.keydown(event)
```

## Base Widget
these are all optianl parameters and methods that all widgests have

#### optional parameters

```python
    "background_color": (255, 255, 255)
    "surface": None
    "on_click": None
    "on_hover": None
    "on_hold": None
    "on_release": None
    "on_enter": None
    "on_exit": None
    "image": None
    "curve": 0
    "font_colour": (0, 0, 0)
    "font": "Calibri"
    "font_size": 30
    "center": False
```
#### methods

- `get_rect()` -> pygame.Rect

## Charts

### .barchart

```python
params = {
        "ticks_y": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "data": {"a": 10, "b": 20},
        "bin_color": (255, 99, 97),
        "line_color": (200, 200, 200),
        "text_color": (100, 100, 100),
        "mouse_line": False,
    }
hapi.barchart(x, y, w, h, params)
```


### .linechart

```python
params = {
        "ticks_y": 10,
        "ticks_x": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "range_x": [0, 100],
        "lines":[{
                "label": "---",
                "color": (255, 0, 0),
                "data": [[1,1]],
                "values_window": 200
            }],
        "labels": ["apple", "", "", "tree"],
        "line_color": (200, 200, 200),
        "text_color": (100, 100, 100),
        "mouse_line": False,
        "mouse_line_color": (255, 0, 0),
        "graph_color": (0, 0, 0),
        "show_axes": True,
        "show_ticks_x": True,
        "show_ticks_y": True,
        "x_axis_label": "x_axis_label",
        "y_axis_label": "y_axis_label",
        "plot_background": True,
        "plot_grid": True,
        "plot_background_color": (234,234,242),
        "plot_grid_color": 255
    }
hapi.linechart(x, y, w, h, params)
```


### .scatterchart

```python
params = {
        "ticks_y": 10,
        "ticks_x": 10,
        "tick_size": 5,
        "range_y": [0, 100],
        "range_x": [0, 100],
        "data": {
            "carat": [0.23, 0.21, 0.23, 0.29, 0.31, 0.24, 0.24, 0.26, 0.22, 0.23], 
            "cut": ["Ideal", "Premium", "Good", "Premium", "Good", "Very Good", "Very Good", "Very Good", "Fair"],
            "color": ["E", "E", "E", "I", "J", "J", "I", "H", "E", "H"],
            "clarity": ["SI2", "SI1", "VS1", "VS2", "SI2", "VVS2", "VVS1", "SI1", "VS2", "VS1"],
            "depth": [61.5, 59.8, 56.9, 62.4, 63.3, 62.8, 62.3, 61.9, 65.1, 59.4],
            "table": [55, 61, 65, 58, 58, 57, 57, 55, 61, 61],
            "price": [326, 326, 327, 334, 335, 336, 336, 337, 337, 338],
            "x": [3.95, 3.89, 4.05, 4.2, 4.34, 3.94, 3.95, 4.07, 3.87, 4],
            "y": [3.98, 3.84, 4.07, 4.23, 4.35, 3.96, 3.98, 4.11, 3.78, 4.05],
            "z": [2.43, 2.31, 2.31, 2.63, 2.75, 2.48, 2.47, 2.53, 2.49, 2.39]
        },
        "hue": None,
        "hue_order": [],
        "size": None,
        "text_color": (100, 100, 100),
        "mouse_line": False,
        "mouse_line_color": (255, 0, 0),
        "graph_color": (0, 0, 0),
        "show_axes": True,
        "show_ticks_x": True,
        "show_ticks_y": True,
        "x": "price",
        "y": "carat",
        "plot_background": True,
        "plot_grid": True,
        "plot_background_color": (234,234,242),
        "plot_grid_color": 255,
        "line_color": 200,
        "strong_color": (107, 107, 255),
        "light_color": (235, 235, 255),
        "type": "normal",
        "kind": "rect",
        "hist_color": "b",
        "hist_color_invert": False
    }

```

