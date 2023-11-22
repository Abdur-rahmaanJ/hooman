import sys
import os 
import shutil
import uuid
import time

import pygame
import pygame.gfxdraw

from math import pi
from math import cos
from math import sin
from math import sqrt
import datetime

from .ui import Button
from .ui import Slider
from .ui import TextBox
from .ui import slider_with_text
from .ui import Scroll

from .shapes import star
from .shapes import alpha_ellipse
from .shapes import curve_rect
from .shapes import arrow
from .shapes import heart
from .shapes import regular_polygon
from .shapes import supershape
from .shapes import smooth_star
from .shapes import flowing_star
from .shapes import oil_drop
from .shapes import ellipse
from .shapes import cross_hair
from .shapes import gradient_rect

from .formula import constrain
from .formula import round_to_num
from .formula import distance
from .formula import rgb_to_hls
from .formula import hls_to_rgb

from .time import Timer

from .charts import barchart
from .charts import linechart
from .charts import piechart
from .charts import scatterchart

from .svg import SVG

from .check import check_color
from .check import verify_color
from .check import check_value
from .check import verify_func_param

from .colors import candy_colors
from .colors import candy_colors_list

from .widget import RippleGraph
from .widget import LockPattern


class Hooman:
    def __init__(self, WIDTH=None, HEIGHT=None, svg=False, integrate=False, screen=None):
        pygame.init()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.PI = pi
        self.HALF_PI = pi / 2 
        self.QUARTER_PI = 0.75 * pi 
        self.TWO_PI = 2 * pi
        self.TAU = 2 * pi

        if not integrate:
            self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        else:
            self.screen = screen

        if not integrate:
            self.center_x = WIDTH // 2
            self.center_y = HEIGHT // 2
        else:
            x, y = self.screen.get_size()
            self.WIDTH = x
            self.HEIGHT = y
            self.center_x = x // 2 
            self.center_y = y // 2
        self.sin = sin
        self.cos = cos
        self.constrain = constrain
        self.sqrt = sqrt
        self.round_to = round_to_num
        self.dist = distance

        self.colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "yellow": (255, 255, 0),
            "grey": (100, 100, 100),
            "light_grey": (200, 200, 200),
            "candy_gray": (240, 240, 255),
        }
        self.colours = self.colors
        self.color = self.colors
        self.colour = self.colors
        self.candy_colors = candy_colors
        self.candy_colors_list = candy_colors_list

        self.set_caption = pygame.display.set_caption


        self.is_running = True
        self.bg_col = None
        self.set_caption("hooman window")

        self._rotation = 0
        self._alpha = 255
        self._fill = (255, 255, 255)
        self._stroke = (255, 255, 255)
        self._stroke_weight = 0
        self._font_name = "freesansbold.ttf"
        self._font_size = 32
        self._font = pygame.font.Font(self._font_name, self._font_size)
        self._matrix_stack = []

        self.sysfont = "comicsansms"
        self._font_size = 10
        self.pygame = pygame
        self.mouse_test_x = 0
        self.clock = pygame.time.Clock()
        self._all_widgets = []
        self._polygon_coords = []

        self._star = star
        self._alpha_ellipse = alpha_ellipse
        self._curve_rect = curve_rect
        self._arrow = arrow
        self._heart = heart
        self._reg_poly = regular_polygon
        self._supershape = supershape
        self._smooth_star = smooth_star
        self._flowing_star = flowing_star
        self._oil_drop = oil_drop
        self._cross_hair = cross_hair
        self._gradient = gradient_rect

        self._timers = []

        self._barchart = barchart
        self._linechart = linechart
        self._piechart = piechart
        self._scatterchart = scatterchart

        self.hls_to_rgb = hls_to_rgb
        self.rgb_to_hls = rgb_to_hls

        self._svg = svg
        self._svg_commands = []

        self.session_id = uuid.uuid1()
        self._session_vars = {}

        self._previous_mouse = []

        self._frame_count = 0

        self._has_cursor = False

        self._start_millis = time.time()


    #
    # colors
    #

    def fill(self, *col):
        """The color to fill drawn shapes with"""
        # verify_color([col])
        self._fill = check_color(col).value

    def stroke(self, *col):
        """The color to draw lines/strokes with"""
        # verify_color([col])
        self._stroke = check_color(col).value

    def background(self, *col):
        """Fill the screen with a color"""

        # verify_color([col])
        v = check_color(col).value

        self.screen.fill(v)

        # check_col = check_

    def gradient(self, w : int, h : int, start_col, end_col, direction : int =0):
        """returns a pygame.Surface with a gradient between 2 colors"""
        param_types = {
            "w": [int, []],
            "h": [int, []],
            "direction": [int, []],
        }
        verify_color([start_col, end_col])
        verify_func_param(self.gradient, param_types, locals())
        return self._gradient(
            w, h, check_color(start_col).value, check_color(end_col).value, direction
        )

    def set_background(self, col):
        """this calls hapi.background every frame with the given color"""

        verify_color([col])
        self.bg_col = check_color(col).value

    def stroke_size(self, weight):
        """The thickness of drawn lines"""
        param_types = {
            "weight": [int, []],
        }
        verify_func_param(self.stroke_size, param_types, locals())

        self._stroke_weight = weight

    def set_alpha(self, alpha):
        """sets the alpha to """
        self._alpha = alpha

    #
    # size
    #

    def no_stroke(self):
        self._stroke_weight = 0

    def font_size(self, font_size):
        param_types = {
            "font_size": [int, []],
        }

        verify_func_param(self.font_size, param_types, locals())

        self._font_size = font_size

    #
    # transforms
    #

    def rotate(self, angle):
        param_types = {
            "angle": [int, []],
        }
        verify_func_param(self.rotate, param_types, locals())
        self._rotation = angle % 360

    def push_matrix(self):
        self._matrix_stack.append(self._rotation)

    def pop_matrix(self):
        self._rotation = self._matrix_stack.pop()

    #
    # shapes
    #

    def ellipse(self, x, y, width, height):
        param_types = {
            "x": [[int, float], []],
            "y": [[int, float], []],
            "width": [[int, float], []],
            "height": [[int, float], []],
        }
        verify_func_param(self.ellipse, param_types, locals())

        pygame.draw.ellipse(self.screen, self._fill, (x, y, width, height))

        if self._svg:
            attributes = {
                "cx": x,
                "cy": y,
                "rx": width / 2,
                "ry": height / 2,
                "fill": f"rgb({self._fill[0]},{self._fill[1]},{self._fill[2]})",
                "stroke": f"rgb({self._stroke[0]},{self._stroke[1]},{self._stroke[2]})",
                "stroke-width": self._stroke_weight,
                "transform": f"rotate({self._rotation}, {x}, {y})",  # "translate(30,40) rotate(45)'
            }
            svg_element = SVG.tag("ellipse", attributes=attributes, self_close=True)
            self._svg_commands.append(svg_element)

    def circle(self, x, y, width):
        self.ellipse(x, y, width, width)


    def rect(self, x, y, width, height):
        param_types = {
            "x": [[int, float], []],
            "y": [[int, float], []],
            "width": [[int, float], []],
            "height": [[int, float], []],
        }
        verify_func_param(self.rect, param_types, locals())
        if self._rotation % 360 == 0:
            pygame.draw.rect(self.screen, self._fill, (x, y, width, height))

            if self._svg:
                attributes = {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height,
                    "fill": f"rgb({self._fill[0]},{self._fill[1]},{self._fill[2]})",
                    "stroke": f"rgb({self._stroke[0]},{self._stroke[1]},{self._stroke[2]})",
                    "stroke-width": self._stroke_weight,
                    "transform": f"rotate({self._rotation}, {x}, {y})",  # "translate(30,40) rotate(45)'
                }
                svg_element = SVG.tag("rect", attributes=attributes, self_close=True)
                self._svg_commands.append(svg_element)
        else:
            self.regular_polygon(x, y, width, height, 4, 45)

    def square(self, x, y, width):
        self.rect(x, y, width, width)
    
    def text(self, letters, x, y):
        if not isinstance(letters, str):
            letters = str(letters)

        param_types = {
            "x": [[int, float], []],
            "y": [[int, float], []],
            "letters": [str, []],
        }
        verify_func_param(self.text, param_types, locals())

        font = pygame.font.SysFont(self.sysfont, self._font_size)
        text = font.render(letters, True, self._fill)
        text = pygame.transform.rotate(text, self._rotation)
        self.screen.blit(text, (x, y))

        if self._svg:
            attributes = {
                "x": x,
                "y": y,
                "font-size": self._font_size,
                # 'fill': f'rgb({self._fill[0]},{self._fill[1]},{self._fill[2]})',
                # 'stroke': f'rgb({self._stroke[0]},{self._stroke[1]},{self._stroke[2]})',
                # 'stroke-width': self.stroke_size,
                "transform": f"rotate({self._rotation}, {x}, {y})",  # "translate(30,40) rotate(45)'
            }
            svg_element = SVG.tag("text", content=letters, attributes=attributes)
            self._svg_commands.append(svg_element)

    def arc(self, x, y, width, height, start_angle, end_angle):
        param_types = {
            "x": [[int, float], []],
            "y": [[int, float], []],
            "width": [[int, float], []],
            "height": [[int, float], []],
            "start_angle": [[int, float], []],
            "end_angle": [[int, float], []],
        }
        verify_func_param(self.arc, param_types, locals())
        pygame.draw.arc(
            self.screen,
            self._stroke,
            [x, y, width, height],
            start_angle,
            end_angle,
            self._stroke_weight,
        )

    def begin_shape(self):
        self._polygon_coords = []

    def vertex(self, coord):
        self._polygon_coords.append(coord)

    def end_shape(self, fill=1):
        if fill:
            pygame.draw.polygon(self.screen, self._fill, self._polygon_coords)
            svg_fill = f"rgb({self._fill[0]},{self._fill[1]},{self._fill[2]})"
        else:
            pygame.draw.polygon(
                self.screen, self._fill, self._polygon_coords, self._stroke_weight
            )
            svg_fill = "none"

        if self._svg:
            points = []
            for p in self._polygon_coords:
                points.append(f"{p[0]},{p[1]}")
            attributes = {
                "points": " ".join(points),
                "fill": svg_fill,
                "stroke": f"rgb({self._stroke[0]},{self._stroke[1]},{self._stroke[2]})",
                "stroke-width": self._stroke_weight,
                "transform": f"rotate({self._rotation})",  # "translate(30,40) rotate(45)'
            }
            svg_element = SVG.tag("polygon", attributes=attributes, self_close=True)
            self._svg_commands.append(svg_element)

    def polygon(self, coords, fill=1):
        if fill:
            pygame.draw.polygon(self.screen, self._fill, coords)
            svg_fill = f"rgb({self._fill[0]},{self._fill[1]},{self._fill[2]})"
        else:
            pygame.draw.polygon(self.screen, self._fill, coords, self._stroke_weight)
            svg_fill = "none"

        if self._svg:
            points = []
            for p in self._polygon_coords:
                points.append(f"{p[0]},{p[1]}")
            attributes = {
                "points": " ".join(points),
                "fill": svg_fill,
                "stroke": f"rgb({self._stroke[0]},{self._stroke[1]},{self._stroke[2]})",
                "stroke-width": self._stroke_weight,
                "transform": f"rotate({self._rotation})",  # "translate(30,40) rotate(45)'
            }
            svg_element = SVG.tag("polygon", attributes=attributes, self_close=True)
            self._svg_commands.append(svg_element)

    def line(self, x1, y1, x2, y2):
        param_types = {
            "x1": [[int, float], []],
            "y1": [[int, float], []],
            "x2": [[int, float], []],
            "y2": [[int, float], []],
        }
        verify_func_param(self.line, param_types, locals())
        pygame.draw.line(
            self.screen, self._stroke, [x1, y1], [x2, y2], self._stroke_weight
        )

        if self._svg:
            attributes = {
                "x1": x1,
                "x2": x2,
                "y1": y1,
                "y2": y2,
                "stroke": f"rgb({self._stroke[0]},{self._stroke[1]},{self._stroke[2]})",
                "stroke-width": self._stroke_weight,
                "transform": f"rotate({self._rotation}, {x1}, {y1})",  # "translate(30,40) rotate(45)'
            }
            svg_element = SVG.tag("line", attributes=attributes, self_close=True)
            self._svg_commands.append(svg_element)

    def star(self, x, y, r1, r2, npoints):
        self._star(self, x, y, r1, r2, npoints, self._rotation)

    def alpha_ellipse(self, x, y, w, h):
        param_types = {
            "x": [[int, float], []],
            "y": [[int, float], []],
            "w": [int, []],
            "h": [int, []],
        }
        verify_func_param(self.alpha_ellipse, param_types, locals())
        self._alpha_ellipse(self, x, y, w, h)

    def curve_rect(self, x, y, w, h, curve):
        self._curve_rect(self, x, y, w, h, curve, self._rotation)

    def arrow(self, x, y, width, height):
        self._arrow(self, x, y, width, height, self._rotation)

    def heart(self, x, y, w, h):
        self._heart(self, x, y, w, h, self._rotation)

    def regular_polygon(self, x, y, w, h, num_of_points, angle_offset=0):
        self._reg_poly(self, x, y, w, h, num_of_points, self._rotation, angle_offset)

    def supershape(self, x_coord, y_coord, size_x, size_y, param_options, fill=False):
        self._supershape(
            self,
            x_coord,
            y_coord,
            size_x,
            size_y,
            param_options,
            self._rotation,
            fill=False,
        )

    def smooth_star(self, x_coord, y_coord, size_x, size_y, n1=0.20, fill=False):
        self._smooth_star(self, x_coord, y_coord, size_x, size_y, n1=n1, fill=fill)

    def oil_drop(self, x_coord, y_coord, size_x, size_y, n1=0.3, fill=False):
        self._oil_drop(self, x_coord, y_coord, size_x, size_y, n1, fill=fill)

    def flowing_star(self, x_coord, y_coord, size_x, size_y, n1=0.3, fill=False):
        self._flowing_star(self, x_coord, y_coord, size_x, size_y, n1, fill=fill)

    def manual_ellipse(self, x, y, w, h, a):
        ellipse(self, x, y, w, h, self._rotation, a)

    def gradient_rect(self, x, y, w, h, start_col, end_col, direction=0):
        val = w if direction == 0 else h
        val = 1 if val == 0 else val
        sr, sg, sb = start_col
        er, eg, eb = end_col
        dr, dg, db = (er - sr) / val, (eg - sg) / val, (eb - sb) / val
        if direction == 0:
            surf = pygame.Surface((w, 1))
        else:
            surf = pygame.Surface((1, h))
        for i in range(val):
            col = (int(sr + dr * i), int(sg + dg * i), int(sb + db * i))
            if direction == 0:
                surf.set_at((i, 0), col)
            else:
                surf.set_at((0, i), col)
        self.screen.blit(pygame.transform.scale(surf, (w, h)), (x, y))

    def fill_arc(self, x, y, radius, startangle, endangle, start_rad=0):
        for r in range(start_rad, radius):
            pygame.gfxdraw.arc(
                self.screen, x, y, r, int(startangle), int(endangle), self._fill
            )

    #
    # interactivity
    #

    def mouseX(self):
        x, y = pygame.mouse.get_pos()
        return x

    def mouseY(self):
        x, y = pygame.mouse.get_pos()
        return y

    def pmouseX(self):
        if len(self._previous_mouse) == 0:
            return 0
        else:
            x, y = self._previous_mouse[0]
            return x

    def pmouseY(self):
        if len(self._previous_mouse) == 0:
            return 0
        else:
            x, y = self._previous_mouse[0]
            return y

    def mouse(self):
        return pygame.mouse.get_pos()

    def cross_hair(self, coord):
        self._cross_hair(self, coord)

    #
    # pygame
    #

    def flip_display(self, update_ui=True):
        """updates the screen. This should be called once every frame"""

        self._frame_count += 1

        self._previous_mouse.append(self.mouse())



        if len(self._previous_mouse) > 2: # bug: 3 values in previous mouse
            self._previous_mouse.remove(self._previous_mouse[0]) # a queue?
        
        if self.bg_col is not None:
            self.background(self.bg_col)


        if update_ui:
            self.update_ui()
        pygame.display.flip()
        



    def handle_events(self, event):
        pass

    def event_loop(self):
        """Get all new events. This should be called once every frame"""
        if len(self._timers) > 0:
            self._timer_update()
        self.mouse_test_x = self.mouseX()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            self.handle_events(event)

    #
    # ui
    #

    def button(self, *args, **kwargs) -> Button:
        b = Button(*args, **kwargs)
        self._all_widgets.append(b)
        return b


    def ripple_graph(self, *args, **kwargs) -> RippleGraph:
        rg = RippleGraph(self, *args, **kwargs)
        # self._all_widgets.append(b)
        return rg

    def lock_pattern(self, *args, **kwargs) -> LockPattern:
        lp = LockPattern(self, *args, **kwargs)
        self._all_widgets.append(lp)
        return lp

    def text_box(self, *args, **kwargs) -> TextBox:
        t = TextBox(*args, **kwargs)
        self._all_widgets.append(t)
        return t

    def slider(self, *args, **kwargs) -> Slider:
        s = Slider(*args, **kwargs)
        self._all_widgets.append(s)
        return s

    def update_ui(self):
        for widget in self._all_widgets:
            widget.update()

    def slider_with_text(self, slider, params={}) -> slider_with_text:
        s = slider_with_text(self, slider, params)
        self._all_widgets.append(s)
        return s

    def scroll(self, param_options={}) -> Scroll:
        s = Scroll(self, param_options)
        self._all_widgets.append(s)
        return s

    #
    # time
    #

    def timer(self, callback=None, seconds=0, minutes=0) -> Timer:
        t = Timer(callback, seconds, minutes)
        self._timers.append(t)
        return t

    def _timer_update(self):
        l = len(self._timers) - 1
        for i, timer in enumerate(reversed(self._timers)):
            t = timer.update()
            if t:
                del self._timers[l - i]

    def hour(self) -> int:
        now = datetime.datetime.now()
        return now.hour

    def minute(self) -> int:
        now = datetime.datetime.now()
        return now.minute

    def second(self) -> int:
        now = datetime.datetime.now()
        return now.second

    #
    # charts
    #

    def barchart(self, x, y, w, h, params={}, **kwargs):
        params.update(kwargs)
        self._barchart(self, x, y, w, h, params)

    def linechart(self, x, y, w, h, params={}, **kwargs):
        params.update(kwargs)
        self._linechart(self, x, y, w, h, params)

    def piechart(self, x, y, radius, data, start_rad=0):
        """
        data in the format:
            [
            ['a', 20, hapi.color['red']],
            ['b', 30, hapi.color['blue']],
            ['c', 40, hapi.color['yellow']],
            ['d', 60, hapi.color['green']],
            ['e', 30, hapi.color['black']]
        ]
        """
        self._piechart(self, x, y, radius, data, start_rad=start_rad)

    def scatterchart(self, x, y, width, height, params={}, **kwargs):
        params.update(kwargs)
        self._scatterchart(self, x, y, width, height, params)

    #
    # svg
    #

    def save_svg(self, path):
        # print(self._svg_commands)
        SVG.save(self._svg_commands, path, self.WIDTH, self.HEIGHT)


    #
    # img
    #


    def save(self, path):
        self.pygame.image.save(self.screen, path)


    #
    # video
    #

    def record(self):
        if 'record_counter' not in self._session_vars:
            self._session_vars['record_counter'] = 0

        if self._session_vars['record_counter'] == 0:
            try:
                shutil.rmtree( 'hoomanvid' )
            except FileNotFoundError:
                pass

        try:
            os.mkdir('hoomanvid')
        except:
            pass
        self.save(f"hoomanvid/{self._session_vars['record_counter']}.png")
        self._session_vars['record_counter'] += 1

    def save_record(self, path, framerate=25):

        if ('record_counter' not in self._session_vars):
            sys.exit('You must .record before using .save_record')

        max_records = len(str(self._session_vars['record_counter']))

        for file in os.listdir('hoomanvid'):
            # print(f'hoomanvid/{file}', f'hoomanvid/{file.zfill(max_records)}')
            
            if not file.startswith('__'):
                newfilename = file.strip('.png').zfill(max_records)
                os.rename(f'hoomanvid/{file}', f'hoomanvid/{newfilename}.png')

        
        try:
            import ffmpeg
        except:
            try:
                shutil.rmtree( 'hoomanvid' )
            except FileNotFoundError:
                pass
            sys.exit("You need to pip install ffmpeg-python and ensure ffmpeg is installed to use this feature")
        
        (
            ffmpeg
            .input('hoomanvid/*.png', pattern_type='glob', framerate=framerate)
            .output(path)
            .run()
        )

        try:
            shutil.rmtree( 'hoomanvid' )
        except FileNotFoundError:
            pass

    #    
    # day n time
    #

    def day(self):
        d = datetime.datetime.now()
        return d.day


    def month(self):
        d = datetime.datetime.now()
        return d.month

    def hour(self):
        d = datetime.datetime.now()
        return d.hour

    def minute(self):
        d = datetime.datetime.now()
        return d.minute


    def second(self):
        d = datetime.datetime.now()
        return d.second


    def year(self):
        d = datetime.datetime.now()
        return d.hour

    def millis(self):
        return (time.time() - self._start_millis) * 1000

    #
    # Environment
    #

    def noCursor(self):
        self._has_cursor = False 


    def frameCount(self):
        return self._frame_count
