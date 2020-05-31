

import pygame
from math import pi

from ui import Button
from ui import Outline
from shapes import star, alpha_ellipse, curve_rect, arrow, heart

class Hooman:
    def __init__(self, WIDTH, HEIGHT):
        pygame.init()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.PI = pi
        
        self.colors = {
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'yellow': (255, 255, 0),
            'grey': (100, 100, 100)
        }
        self.colours = self.colors
        self.color = self.colors
        self.colour = self.colors

        self.set_caption = pygame.display.set_caption
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.is_running = True

        self._alpha = 255
        self._fill = (255, 255, 255)
        self._stroke = (255, 255, 255)
        self._stroke_weight = 0
        self._font_name = 'freesansbold.ttf'
        self._font_size = 32
        self._font = pygame.font.Font(self._font_name, self._font_size)

        self.sysfont = "comicsansms"
        self.font_size = 10
        self.pygame = pygame
        self.mouse_test_x = 0
        self.clock = pygame.time.Clock()
        self._all_widgets = []
        self._polygon_coords = []

        self.outline = Outline
        self._star = star
        self._alpha_ellipse = alpha_ellipse
        self._curve_rect = curve_rect
        self._arrow = arrow
        self._heart = heart
        

    def fill(self, col):
        if isinstance(col, int):
            self._fill = (col, col, col)
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self._fill = (col[0], col[0], col[0])
            else:
                self._fill = (col[0], col[1], col[2])

    def stroke(self, col):
        if isinstance(col, int):
            self._stroke = (col, col, col)
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self._stroke = (col[0], col[0], col[0])
            else:
                self._stroke = (col[0], col[1], col[2])

    def background(self, col):
        if isinstance(col, int):
            self.screen.fill((col, col, col))
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self.screen.fill((col[0], col[0], col[0]))
            else:
                self.screen.fill((col[0], col[1], col[2]))

    def stroke_size(self, weight):
        self._stroke_weight = weight

    def no_stroke(self):
        self._stroke_weight = 0

    def font_size(self, font_size):
        self.font_size = font_size

    def set_alpha(self, alpha):
        self._alpha = alpha

    def ellipse(self, x, y, width, height):
        pygame.draw.ellipse(self.screen, self._fill, (x, y, width, height))

    def rect(self, x, y, width, height):
        pygame.draw.rect(self.screen, self._fill, (x, y, width, height))
        if self._stroke_weight > 0:
            pygame.draw.rect(self.screen, self._stroke, (x, y, width, height), 
                self._stroke_weight)

    def text(self, letters, x, y):
        if not isinstance(letters, str):
            letters = str(letters)
        font = pygame.font.SysFont(self.sysfont, self.font_size)
        text = font.render(letters, True, self._fill)
        self.screen.blit(text, (x, y))

    def arc(self, x, y, width, height, start_angle, end_angle):
        pygame.draw.arc(self.screen, self._fill, [x, y, width, height],
            start_angle, end_angle, self._stroke_weight)

    def begin_shape(self):
        self._polygon_coords = []

    def vertex(self, coord):
        self._polygon_coords.append(coord)

    def end_shape(self, fill=1):
        if fill:
            pygame.draw.polygon(self.screen, self._fill, self._polygon_coords)
        else:
            pygame.draw.polygon(self.screen, self._fill, self._polygon_coords, self._stroke_weight)

    def polygon(self, coords, fill=1):
        if fill:
            pygame.draw.polygon(self.screen, self._fill, coords)
        else:
            pygame.draw.polygon(self.screen, self._fill, coords, self._stroke_weight)

    def mouseX(self):
        x, y = pygame.mouse.get_pos()
        return x

    def mouseY(self):
        x, y = pygame.mouse.get_pos()
        return y

    def flip_display(self):
        pygame.display.flip()

    def line(self, x1, y1, x2, y2):
        pygame.draw.line(self.screen, self._stroke, [x1, y1], [x2, y2], self._stroke_weight)

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False

    def event_loop(self):
        self.mouse_test_x = self.mouseX()
        for event in pygame.event.get():
            self.handle_events(event)

    def button(self, *args, **kwargs):
        b = Button(*args, **kwargs)
        self._all_widgets.append(b)
        return b

    def update_ui(self):
        for widget in self._all_widgets:
            widget.update()

    def star(self, x, y, r1, r2, npoints):
        self._star(self, x, y, r1, r2, npoints)

    def alpha_ellipse(self, x, y, w, h):
        self._alpha_ellipse(self, x, y, w, h)
    
    def curve_rect(self, x, y, w, h, curve):
        self._curve_rect(self, x, y, w, h, curve)
    
    def arrow(self, x, y, size, angle):
        self._arrow(self,x,y,size,angle)
    
    def heart(self, x, y, w, h):
        self._heart(self,x,y,w,h)