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

from .time import Timer

from .charts import barchart
from .charts import linechart
from .charts import piechart


class Hooman:
    def __init__(self, WIDTH, HEIGHT):
        pygame.init()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.PI = pi
        self.center_x = WIDTH//2
        self.center_y = HEIGHT//2
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
        }
        self.colours = self.colors
        self.color = self.colors
        self.colour = self.colors

        self.set_caption = pygame.display.set_caption
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
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

    #
    # colors
    #

    def fill(self, col):
        """The color to fill drawn shapes with"""
        if isinstance(col, int):
            self._fill = (col, col, col)
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self._fill = (col[0], col[0], col[0])
            else:
                self._fill = (col[0], col[1], col[2])

    def stroke(self, col):
        """The color to draw lines/strokes with"""
        if isinstance(col, int):
            self._stroke = (col, col, col)
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self._stroke = (col[0], col[0], col[0])
            else:
                self._stroke = (col[0], col[1], col[2])

    def background(self, col):
        """Fill the screen with a color"""
        if isinstance(col, int) or isinstance(col, float):
            self.screen.fill((col, col, col))
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self.screen.fill((col[0], col[0], col[0]))
            else:
                self.screen.fill((col[0], col[1], col[2]))

    def gradient(self, w, h, start_col, end_col, direction=0):
        """returns a pygame.Surface with a gradient between 2 colors"""
        return self._gradient(w, h, start_col, end_col, direction)

    def set_background(self, col):
        """this calls hapi.background every frame with the given color"""
        self.bg_col = col

    def stroke_size(self, weight):
        """The thickness of drawn lines"""
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
        self._font_size = font_size

    #
    # transforms
    #

    def rotate(self, angle):
        self._rotation = angle % 360

    def push_matrix(self):
        self._matrix_stack.append(self._rotation)

    def pop_matrix(self):
        self._rotation = self._matrix_stack.pop()

    #
    # shapes
    #

    def ellipse(self, x, y, width, height):
        pygame.draw.ellipse(self.screen, self._fill, (x, y, width, height))

    def rect(self, x, y, width, height):
        if self._rotation % 360 == 0:
            pygame.draw.rect(self.screen, self._fill, (x, y, width, height))
        else:
            self.regular_polygon(x, y, width, height, 4, 45)

    def text(self, letters, x, y):
        if not isinstance(letters, str):
            letters = str(letters)
        font = pygame.font.SysFont(self.sysfont, self._font_size)
        text = font.render(letters, True, self._fill)
        text = pygame.transform.rotate(text, self._rotation)
        self.screen.blit(text, (x, y))

    def arc(self, x, y, width, height, start_angle, end_angle):
        pygame.draw.arc(
            self.screen,
            self._fill,
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
        else:
            pygame.draw.polygon(
                self.screen, self._fill, self._polygon_coords, self._stroke_weight
            )

    def polygon(self, coords, fill=1):
        if fill:
            pygame.draw.polygon(self.screen, self._fill, coords)
        else:
            pygame.draw.polygon(self.screen, self._fill, coords, self._stroke_weight)

    def line(self, x1, y1, x2, y2):
        pygame.draw.line(
            self.screen, self._stroke, [x1, y1], [x2, y2], self._stroke_weight
        )

    def star(self, x, y, r1, r2, npoints):
        self._star(self, x, y, r1, r2, npoints, self._rotation)

    def alpha_ellipse(self, x, y, w, h):
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
            pygame.gfxdraw.arc(self.screen, x, y, r, int(startangle), int(endangle), self._fill)

    #
    # interactivity
    #

    def mouseX(self):
        x, y = pygame.mouse.get_pos()
        return x

    def mouseY(self):
        x, y = pygame.mouse.get_pos()
        return y

    def cross_hair(self, coord):
        self._cross_hair(self, coord)

    #
    # pygame
    #

    def flip_display(self):
        """updates the screen. This should be called once every frame"""
        pygame.display.flip()
        if self.bg_col is not None:
            self.background(self.bg_col)

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False

    def event_loop(self):
        """Get all new events. This should be called once every frame"""
        if len(self._timers) > 0:
            self._timer_update()
        self.mouse_test_x = self.mouseX()
        for event in pygame.event.get():
            self.handle_events(event)

    #
    # ui
    #

    def button(self, *args, **kwargs) -> Button:
        b = Button(*args, **kwargs)
        self._all_widgets.append(b)
        return b

    def text_box(self, *args, **kwargs) -> TextBox:
        t = TextBox(*args, **kwargs)
        self._all_widgets.append(t)
        return t

    def slider(self, *args, **kwargs) -> Slider:
        s = Slider(self, *args, **kwargs)
        self._all_widgets.append(s)
        return s

    def update_ui(self):
        for widget in self._all_widgets:
            widget.update()

    def slider_with_text(self, slider, params={}) -> slider_with_text:
        s = slider_with_text(self, slider, params)
        self._all_widgets.append(s)
        return s

    def scroll(self, param_options = {}) -> Scroll:
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

    def barchart(self, x, y, w, h, params):
        self._barchart(self, x, y, w, h, params)

    def linechart(self, x, y, w, h, params):
        self._linechart(self, x, y, w, h, params)

    def piechart(self, x, y, radius, data, start_rad=0):
        '''
        data in the format:
            [
            ['a', 20, hapi.color['red']],
            ['b', 30, hapi.color['blue']],
            ['c', 40, hapi.color['yellow']],
            ['d', 60, hapi.color['green']],
            ['e', 30, hapi.color['black']]
        ]
        '''
        self._piechart(self, x, y, radius, data, start_rad=start_rad)
