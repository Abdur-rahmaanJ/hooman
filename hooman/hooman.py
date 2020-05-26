import pygame
from math import pi

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Hooman:
    def __init__(self, WIDTH, HEIGHT):
        pygame.init()
        self.codes = pygame.locals
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self._fill = (255, 255, 255)
        self._stroke = (255, 255, 255)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.pi = pi
        self._stroke_weight = 0
        self._font_name = 'freesansbold.ttf'
        self._font_size = 32
        self._font = pygame.font.Font(self._font_name, self._font_size)
        self.sysfont = "comicsansms"
        self.font_size = 10
        self.pygame = pygame
        self.is_running = True
        self.mouse_test_x = 0

    def fill(self, col):
        if isinstance(col, int):
            self._fill = (col, col, col)
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self._fill = (col[0], col[0], col[0])
            else:
                self._fill = (col[0], col[1], col[2])

    def stroke(self, color):
        self._stroke = (color[0], color[1], color[2])

    def background(self, col):
        if isinstance(col, int):
            self.screen.fill((col, col, col))
        elif isinstance(col, list) or isinstance(col, tuple):
            if len(col) == 1:
                self.screen.fill((col[0], col[0], col[0]))
            else:
                self.screen.fill((col[0], col[1], col[2]))

    def stroke_weight(self, weight):
        self._stroke_weight = weight

    def no_stroke(self):
        self._stroke_weight = 0

    def font_size(self, font_size):
        self.font_size = font_size

    def ellipse(self, x, y, width, height):
        pygame.draw.ellipse(self.screen, self._fill, (x, y, width, height))

    def rect(self, x, y, width, height):
        pygame.draw.rect(self.screen, self._fill, (x, y, width, height))
        if self._stroke_weight > 0:
            pygame.draw.rect(self.screen, self._stroke, (x, y, width, height), 
                self._stroke_weight)

    def mouseX(self):
        x, y = pygame.mouse.get_pos()
        return x

    def mouseY(self):
        x, y = pygame.mouse.get_pos()
        return y

    def text(self, letters, x, y):
        font = pygame.font.SysFont(self.sysfont, self.font_size)
        text = font.render(letters, True, self._fill)
        self.screen.blit(text, (x, y))

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