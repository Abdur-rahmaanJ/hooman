

import pygame
from math import pi

class Hooman:
    def __init__(self, WIDTH, HEIGHT):

        pygame.init()
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

    def stroke_size(self, weight):
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
        if not isinstance(letters, str):
            letters = str(letters)
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


class Button:
    def __init__(self, x, y, w=0, h=0, calculateSize=False, text="", background=(255, 255, 255),
                 font="Calibri", font_size=30, font_colour=(0, 0, 0), outline=None, action=None,
                 action_arg=None, surface=None, image=None, enlarge=False, enlarge_amount=1.1,
                 hover_image=None, dont_generate=False, hover_background_color=None, curve_amount=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.surface = surface
        #if no surface is supplied, try getting main screen
        if self.surface is None:
            self.surface = pygame.display.get_surface()
            if self.surface is None:
                raise ValueError("No surface to blit to")
        self.text = text
        self.text_colour = font_colour
        self.background = background
        self.curve_amount = curve_amount
        self.hover_background = self.background
        if hover_background_color is not None:
            self.hover_background = hover_background_color
        self.font = pygame.font.Font(pygame.font.match_font(font),font_size)
        self.out = outline
        self.action = action
        self.image = image.copy() if image else None
        self.clicked_on = False
        self.hover_image = hover_image
        self.enlarge = enlarge
        self.enlarge_amount = enlarge_amount
        if self.enlarge:
            if self.text != "":
                self.enlarge_font = pygame.font.Font(
                    pygame.font.match_font(font), int(font_size * enlarge_amount))
        self.action_arg = action_arg
        self.hover = False
        self.caclulateSize = calculateSize
        self.prev_clicked_state = False
        #create the surfaces for the button to blit every frame
        if not dont_generate:
            if self.w == 0 or self.h == 0 or self.caclulateSize:
                if image is not None:
                    self.w = self.image.get_width()
                    self.h = self.image.get_height()
                else:
                    if self.text != "":
                        self._caclulate_size()
                    else:
                        raise ValueError("cannot calculate width and height without text")
            self._Generate_images()


    def _Generate_images(self):     
        #generate images
        #if no image, create the button by drawing
        if self.image is None:
            self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.hover_image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.image.blit(curve_square(self.w, self.h, self.curve_amount, self.background), (0,0))
            self.hover_image.blit(curve_square(
                self.w, self.h, self.curve_amount, self.hover_background), (0,0))
            #self.hover_image.fill(self.hover_background)
            if self.out is not None:
                self.out._draw(self.hover_image,self.hover_background,self.w,self.h,self.curve_amount)
            self.hover_image.convert()
            self.image.convert()
        #if the user gives an image, create the image when the mouse hovers over
        elif self.hover_image is None:
            self.hover_image = self.image.copy()
            if not self.out is None:
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (0, 0, self.w, self.out.s))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (0 ,0 ,self.out.s, self.h))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (self.w, self.h, -self.w, -self.out.s))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (self.w, self.h, -self.out.s, -self.h))
            self.hover_image.convert_alpha()
            self.image.convert_alpha()
        #enlarge the image, no matter if user gives an image or not
        if self.enlarge:
            size = (int(self.w * self.enlarge_amount), int(self.h * self.enlarge_amount))
            self.dx, self.dy = size[0] - self.w, size[1] - self.h
            self.hover_image = pygame.transform.scale(self.image,size) 
        #put the text over images, if enlarge, create a bigger font so resolution stays high
        if self.text != "":
            txt = self.font.render(self.text, True, self.text_colour)
            self.image.blit(txt,((self.w - txt.get_width())//2, (self.h - txt.get_height())//2))
            if self.enlarge:
                txt = self.enlarge_font.render(self.text, True, self.text_colour)
            self.hover_image.blit(txt,((self.hover_image.get_width() - txt.get_width())//2,
                                       (self.hover_image.get_height() - txt.get_height())//2))  
        #if the user gives both images, check to see if different sizes so know if enlarged or not
        if self.hover_image.get_width() != self.w or self.hover_image.get_height() != self.h:
            self.enlarge = True
            self.dx, self.dy = self.hover_image.get_width() - self.w, self.hover_image.get_height() - self.h
        #convert the images so it is faster to put on screen
        self.image.convert()
        self.hover_image.convert()

 
    #if no width or height is given, calculate it with length of text
    def _caclulate_size(self):
        txt = self.font.render(self.text, False, (0, 0, 0))
        self.w = txt.get_width() + self.w
        self.h = txt.get_height() + self.h


    #return a pygame.Rect of the button
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


    #this is what will be shown when print(button)
    def __str__(self):
        if self.text:
            return "Button: '" + self.text + "'"
        else:
            return "Button: at (" + str(self.x)  + ", " + str(self.y) + ")"  


    #update the text of the button, remake the surfaces for the button
    def Update_text(self,text):
        self.text = text
        if self.caclulateSize:
            self._caclulate_size()
        self._Generate_images()

    
    #update the button, this should get called every frame
    def update(self):
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        self.hover = False
        returnee = False
        #check if mouse over button
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
                self.hover = True
                #check for click, if held down, action only gets called once
                if click and not self.prev_clicked_state:
                    self.clicked_on = True
                if self.prev_clicked_state and self.clicked_on and click == False:
                    if self.action:
                        if self.action_arg:
                            self.action(self.action_arg)
                        else:
                            self.action()
                    returnee = True
                if not click:
                    self.clicked_on = False
        self.prev_clicked_state = click
        #draw
        self._draw()
        #return if the button was clicked on
        return returnee
    
    
    #draw the button
    def _draw(self):
        if self.hover:
            if self.enlarge:
                self.surface.blit(self.hover_image,(self.x - self.dx//2, self.y - self.dy//2))
            else:
                self.surface.blit(self.hover_image, (self.x, self.y))
        else:
            self.surface.blit(self.image, (self.x, self.y))


#used to simplify outlining the button/checkbox
#instead of many vars in button, create an outline object to give to button
class Outline:
    def __init__(self, type="full", outline_amount=2, outline_color=(0, 0, 0)):
        self.type = type
        self.s = outline_amount
        self.col = outline_color


    def _draw(self, surf, col, w, h, curve_amount):
        if self.type == "half":
            surf.blit(curve_square(w, h, curve_amount, col), (0, 0))
        elif self.type == "full":
            surf.blit(curve_square(w, h, curve_amount, self.col), (0, 0))
            surf.blit(curve_square(w - self.s * 2, h - self.s * 2, curve_amount, col), (self.s, self.s))


#this creates a curved rect, given a w,h and the curve amount, bewtween 0 and 1
def curve_square(width, height, curve, color=(0, 0, 0)):
    if not 0 <= curve <= 1:
        raise ValueError("curve value out of range, must be between 0 and 1")
    curve *= min(width, height)
    curve = int(curve)
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (0, curve, width, height - 2 * curve))
    pygame.draw.rect(surf, color, (curve, 0, width - 2 * curve, height))
    pygame.draw.circle(surf, color, (curve, curve), curve)
    pygame.draw.circle(surf, color, (width - curve, curve), curve)
    pygame.draw.circle(surf, color, (curve, height - curve), curve)
    pygame.draw.circle(surf, color, (width - curve, height - curve), curve)
    return surf
