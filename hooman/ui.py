'''
Author: https://github.com/TheBigKahuna353
Edit: https://github.com/Abdur-rahmaanJ
'''

import pygame

class Button:

    def __init__(self, x, y, text, param_options):
        self.x = x
        self.y = y
        self.w = 1
        self.h = 1
        self.text = text

        options = {
            'surface': None,
            'hover_background_color': None,
            'font': 'Calibri',
            'font_size': 30,
            'outline': None,
            'on_click': None,
            'on_hover_enter':None,
            'on_hover_exit':None,
            'image': None,
            'hover_image': None,
            'enlarge': False,
            'enlarge_amount': 1.1,
            'calculate_size': 1.1,
            'dont_generate': False,
            'font_colour': (0, 0, 0),
            'background_color': (255, 255, 255),
            'curve': 0,
            'padding_x':0,
            'padding_y':0
        }
        options.update(param_options)

        self.padding_x = options['padding_x']
        self.padding_y = options['padding_y']
        self.surface = options['surface']
        self.text_colour = options['font_colour']
        self.background_color = options['background_color']
        self.curve_amount = options['curve']
        font = options['font']
        font_size = options['font_size']
        self.outline = options['outline']
        self.on_click = options['on_click']
        self.on_hover_enter = options['on_hover_enter']
        self.on_hover_exit = options['on_hover_exit']
        image = options['image']
        dont_generate = options['dont_generate']
        self.caclulateSize = options['calculate_size']
        self.hover_image = options['hover_image']
        self.enlarge = options['enlarge']
        self.enlarge_amount = options['enlarge_amount']

        # if no surface is supplied, try getting main screen
        if self.surface is None:
            self.surface = pygame.display.get_surface()
            if self.surface is None:
                raise ValueError("No surface to blit to")

        self.font = pygame.font.Font(pygame.font.match_font(font),font_size)

        self.image = image.copy() if image else None
        self.clicked_on = False
        self.draw = False
        
        if self.enlarge:
            if self.text != "":
                self.enlarge_font = pygame.font.Font(
                    pygame.font.match_font(font), int(font_size * enlarge_amount))
        self.hover = False
        
        self.prev_clicked_state = False
        # create the surfaces for the button to blit every frame
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
        # generate images
        print("generate")
        # if no image, create the button by drawing
        if self.image is None or self.draw:
            self.draw = True
            self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.hover_image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.image.blit(curve_square(self.w, self.h, self.curve_amount, self.background_color), (0,0))
            self.hover_image.blit(curve_square(
                self.w, self.h, self.curve_amount, self.background_color), (0,0))
            # self.hover_image.fill(self.background_color)
            if self.outline is not None:
                self.outline._draw(self.hover_image,self.background_color,self.w,self.h,self.curve_amount)
            self.hover_image.convert()
            self.image.convert()
        # if the user gives an image, create the image when the mouse hovers over
        elif self.hover_image is None or self.draw:
            self.hover_image = self.image.copy()
            if not self.outline is None:
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (0, 0, self.w, self.outline.s))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (0 ,0 ,self.outline.s, self.h))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (self.w, self.h, -self.w, -self.outline.s))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (self.w, self.h, -self.outline.s, -self.h))
            self.hover_image.convert_alpha()
            self.image.convert_alpha()
        # enlarge the image, no matter if user gives an image or not
        if self.enlarge:
            size = (int(self.w * self.enlarge_amount), int(self.h * self.enlarge_amount))
            self.dx, self.dy = size[0] - self.w, size[1] - self.h
            self.hover_image = pygame.transform.scale(self.image,size) 
        # put the text over images, if enlarge, create a bigger font so resolution stays high
        if self.text != "":
            txt = self.font.render(self.text, True, self.text_colour)
            self.image.blit(txt,((self.w - txt.get_width())//2, (self.h - txt.get_height())//2))
            if self.enlarge:
                txt = self.enlarge_font.render(self.text, True, self.text_colour)
            self.hover_image.blit(txt,((self.hover_image.get_width() - txt.get_width())//2,
                                       (self.hover_image.get_height() - txt.get_height())//2))  
        # if the user gives both images, check to see if different sizes so know if enlarged or not
        if self.hover_image.get_width() != self.w or self.hover_image.get_height() != self.h:
            self.enlarge = True
            self.dx, self.dy = self.hover_image.get_width() - self.w, self.hover_image.get_height() - self.h
        # convert the images so it is faster to put on screen
        self.image.convert()
        self.hover_image.convert()
        
            
    # if no width or height is given, calculate it with length of text
    def _caclulate_size(self):
        txt = self.font.render(self.text, False, (0, 0, 0))
        self.w = txt.get_width() + self.w + self.padding_x * 2
        self.h = txt.get_height() + self.h + self.padding_y * 2
    
    # return a pygame.Rect of the button
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    # this is what will be shown when print(button)
    def __str__(self):
        if self.text:
            return "Button: '" + self.text + "'"
        else:
            return "Button: at (" + str(self.x)  + ", " + str(self.y) + ")"  
    
    # update the text of the button, remake the surfaces for the button
    def Update_text(self,text):
        self.text = text
        if self.caclulateSize:
            self._caclulate_size()
        self._Generate_images()
    
    
    # update the button, this should get called every frame
    def update(self):
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        returnee = False
        # check if mouse over button
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
                if self.hover == False:
                    if self.on_hover_enter:
                        self.on_hover_enter(self)
                self.hover = True
                        
                # check for click, if held down, action only gets called once
                if click and not self.prev_clicked_state:
                    self.clicked_on = True
                if self.prev_clicked_state and self.clicked_on and click == False:
                    if self.on_click:
                        '''
                        if self.on_click_arg:
                            self.on_click(self.on_click_arg)
                        else:
                            self.on_click()
                        '''
                        self.on_click(self)
                    returnee = True
                if not click:
                    self.clicked_on = False
            else:
                if self.hover:
                    if self.on_hover_exit:
                        self.on_hover_exit(self)
                self.hover = False
        else:
            if self.hover:
                if self.on_hover_exit:
                    self.on_hover_exit(self)
            self.hover = False            
        self.prev_clicked_state = click
        # draw
        self._draw()
        
        
        # return if the button was clicked on
        return returnee
    
    def create_button(self):
        self._Generate_images()
    
    
    # draw the button
    def _draw(self):
        if self.hover:
            if self.enlarge:
                self.surface.blit(self.hover_image,(self.x - self.dx//2, self.y - self.dy//2))
            else:
                self.surface.blit(self.hover_image, (self.x,self.y))
        else:
            self.surface.blit(self.image, (self.x, self.y))

    def width(self):
        txt = self.font.render(self.text, False, (0, 0, 0))
        w = txt.get_width() + self.w + self.padding_x * 2
        return w

    def height(self):
        txt = self.font.render(self.text, False, (0, 0, 0))
        h = txt.get_height() + self.h + self.padding_y * 2
        return


# used to simplify outlining the button/checkbox
# instead of many vars in button, create an outline object to give to button
class Outline:
    def __init__(self, options):
        self.s = options["amount"] if "amount" in options else 2 
        self.col = options["color"] if "color" in options else (0, 0, 0)
        if 'type' in options:
            self.type = options['type']
        else:
            self.type = 'full'


    def _draw(self, surf, col, w, h, curve_amount):
        if self.type == "half":
            surf.blit(curve_square(w, h, curve_amount, col), (0, 0))
        elif self.type == "full":
            surf.blit(curve_square(w, h, curve_amount, self.col), (0, 0))
            surf.blit(curve_square(w - self.s * 2, h - self.s * 2, curve_amount, col), (self.s, self.s))
            
# this creates a curved rect, given a w,h and the curve amount, bewtween 0 and 1
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