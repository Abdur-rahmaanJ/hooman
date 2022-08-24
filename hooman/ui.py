"""
Author: https://github.com/TheBigKahuna353
Edit: https://github.com/Abdur-rahmaanJ
"""

import pygame
from .formula import constrain
from .formula import round_to_num
from typing import Union
from .check import check_params
from time import perf_counter

class Base_Widget:
    """
    base options:
    - background_color: (r, g, b)
    - surface: pygame surface
    - on_click: function
    - on_hover: function
    - on_hold: function
    - on_release: function
    - on_enter: function
    - on_exit: function
    - image: pygame surface
    - curve: int
    - font_colour: (r, g, b)
    - font: str
    - font_size: int
    - centered: bool
    """


    def __init__(self, x, y, w, h, func, params, options):
        base_options = {
            "background_color": (255, 255, 255),
            "surface": None,
            "on_click": None,
            "on_hover": None,
            "on_hold": None,
            "on_release": None,
            "on_enter": None,
            "on_exit": None,
            "image": None,
            "curve": 0,
            "font_colour": (0, 0, 0),
            "font": "Calibri",
            "font_size": 30,
            "center": False,

        }
        # add the options to the base options
        base_options.update(options)
        # check all the options
        check_params(params, base_options, func)
        # set the options
        base_options.update(params)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.background_color = base_options["background_color"]
        # set the surface
        self.surface = pygame.display.get_surface() if base_options['surface'] is None else base_options["surface"]
        # if no window open, raise error
        if self.surface is None:
                raise ValueError("No surface to blit to")
        self.on_click = base_options["on_click"]
        self.on_hover = base_options["on_hover"]
        self.on_hold = base_options["on_hold"]
        self.on_release = base_options["on_release"]
        self.on_enter = base_options["on_enter"]
        self.on_exit = base_options["on_exit"]
        self.image = base_options["image"].copy() if base_options["image"] is not None else None
        if self.image is not None:
            if self.h != 0 and self.w != 0:
                self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.curve = base_options["curve"]
        self.font_colour = base_options["font_colour"]
        self.font_name = base_options["font"]
        self.font_size = base_options["font_size"]
        self.center = base_options["center"]
        if self.center:
            self.x = self.x - self.w // 2
            self.y = self.y - self.h // 2
        self.font = pygame.font.Font(pygame.font.match_font(self.font_name), self.font_size)

        # mouse variables
        self.hover = False #    public variable is the mouse over the widget
        self._prev_hover = False
        self._prev_click = False
        self.clicked = False #  public variable to check if the widget is clicked 
        self.hold = False
        self._started_click = False
        return base_options

    # return a pygame.Rect of the widget
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def _draw(self):
        """
        draw the widget
        """
        # this should be overridden
        pass

    def update(self, global_pos):
        """
        update the widget
        """
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        # check if mouse is over the widget
        self.hover = (self.x < mouse_pos[0] < self.x + self.w and self.y < mouse_pos[1] < self.y + self.h)
        self.clicked = False # reset the clicked variable
        # check all the events
        if self.hover:
            if self.on_hover:
                self.on_hover(self)
            if click:
                if not self._prev_click:
                    self._started_click = True
                    if self.on_click:
                        self.on_click(self)
            if not self._prev_hover:
                if self.on_enter:
                    self.on_enter(self)
        else:
            if self._prev_hover:
                if self.on_exit:
                    self.on_exit(self)
        if click and self._started_click:
            self.hold = True
            if self.on_hold:
                self.on_hold(self)
        else:
            self.hold = False
            if self._prev_click:
                if self._started_click:
                    self.clicked = True
                if self.on_release:
                    self.on_release(self)
            self._started_click = False
        # update previous states
        self._prev_hover = self.hover
        self._prev_click = click

    def __str__(self) -> str:
        if hasattr(self, "text"):
            return "%s: %s" % (self.__class__.__name__, self.text)
        return "%s at (%d, %d)" % (self.__class__.__name__, self.x, self.y)


# this creates a curved rect, given a w,h and the curve amount, bewtween 0 and 1
def curve_square(width, height, curve, color=(0, 0, 0)):
    if not 0 <= curve <= 1:
        raise ValueError("curve value out of range, must be between 0 and 1")
    curve /= 2
    curve *= min(width, height)
    curve = int(curve)
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    if curve == 0:
        surf.fill(color)
        return surf
    pygame.draw.rect(surf, color, (0, curve, width, height - 2 * curve))
    pygame.draw.rect(surf, color, (curve, 0, width - 2 * curve, height))
    pygame.draw.circle(surf, color, (curve, curve), curve)
    pygame.draw.circle(surf, color, (width - curve, curve), curve)
    pygame.draw.circle(surf, color, (curve, height - curve), curve)
    pygame.draw.circle(surf, color, (width - curve, height - curve), curve)
    return surf


class Button(Base_Widget):
    def __init__(self, x, y, w, h, text, params={}):
        self.text = text
        start = perf_counter()

        options = {
            "hover_background_color": None,
            "outline": False,
            "outline_thickness": 0,
            "hover_outline_thickness": None,
            "outline_color": (0, 0, 0),
            "outline_half": False,
            "hover_image": None,
            "enlarge": False,
            "enlarge_amount": 1.1,
            "calculate_size": False,
            "dont_generate": False,
            "padding_x": 0,
            "padding_y": 0,
        }
        options = super().__init__(x, y, w, h, "button", params, options)


        self.padding_x = options["padding_x"]
        self.padding_y = options["padding_y"]
        self.text_colour = options["font_colour"]
        self.hover_bg_colour = options["hover_background_color"]
        self.outline = options["outline"]
        self.outline_col = options["outline_color"]
        self.outline_half = options["outline_half"]
        self.outline_amount = options["outline_thickness"]
        self.outline_amount_hover = options["hover_outline_thickness"] if options["hover_outline_thickness"] is not None else options["outline_thickness"]
        dont_generate = options["dont_generate"]
        self.caclulateSize = options["calculate_size"]
        self.hover_image = options["hover_image"]
        self.enlarge = options["enlarge"]
        self.enlarge_amount = options["enlarge_amount"]

        

        if self.hover_bg_colour is None and self.image is None:
            self.hover_bg_colour = self.background_color

        if self.enlarge:
            if self.text != "":
                self.enlarge_font = pygame.font.Font(
                    pygame.font.match_font(self.font_name), int(self.font_size * self.enlarge_amount)
                )
        # create the surfaces for the button to blit every frame
        if not dont_generate:
            if self.w == 0 or self.h == 0 or self.caclulateSize:
                if self.image is not None:
                    self.w = self.image.get_width()
                    self.h = self.image.get_height()
                else:
                    if self.text != "":
                        self._caclulate_size()
                    else:
                        raise ValueError(
                            "cannot calculate width and height without text"
                        )
            self._Generate_images()

    def _Generate_images(self):
        # generate images
        # if no image, create the button by drawing
        if self.image is None:
            self.image = pygame.Surface((self.w, self.h))
            self.hover_image = pygame.Surface((self.w, self.h))
            self.image.fill(self.background_color)
            self.hover_image.fill(self.hover_bg_colour)
        # if the user gives an image, create the image when the mouse hovers over
        elif self.hover_image is None:
            self.hover_image = self.image.copy()
            if self.hover_bg_colour is not None:
                self.hover_image.fill(self.hover_bg_colour)
        
        #make square image curved
        surf = pygame.Surface((self.w, self.h))
        surf.fill((255, 0, 255))
        hover_surf = pygame.Surface((self.w, self.h))
        hover_surf.fill((255, 0, 255))
        #add outline while we are at it
        if not self.outline_half:
            surf.blit(
                curve_square(self.w, self.h, self.curve, self.outline_col), (0, 0)
                )
            surf.blit(
                curve_square(self.w - self.outline_amount*2, self.h - self.outline_amount*2, self.curve, (254, 0, 255)),
                    (self.outline_amount, self.outline_amount)
                )
            hover_surf.blit(
                curve_square(self.w, self.h, self.curve, self.outline_col), (0, 0)
                )
            hover_surf.blit(
                curve_square(self.w - self.outline_amount_hover*2, self.h - self.outline_amount_hover*2, self.curve, (254, 0, 255)),
                    (self.outline_amount_hover, self.outline_amount_hover)
                )
        else:
            surf.blit(
                curve_square(self.w, self.h, self.curve, self.outline_col), (0, 0)
                )
            surf.blit(
                curve_square(self.w - self.outline_amount, self.h - self.outline_amount, self.curve, (254, 0, 255)),
                    (0, 0)
                )
            hover_surf.blit(
                curve_square(self.w, self.h, self.curve, self.outline_col), (0, 0)
                )
            hover_surf.blit(
                curve_square(self.w - self.outline_amount_hover, self.h - self.outline_amount_hover, self.curve, (254, 0, 255)),
                    (0, 0)
                )

        surf.set_colorkey((254, 0, 255))
        self.image.blit(surf, (0, 0))
        self.image.set_colorkey((255, 0, 255))
        hover_surf.set_colorkey((254, 0, 255))
        self.hover_image.blit(hover_surf, (0, 0))
        self.hover_image.set_colorkey((255, 0, 255))
        #enlarge hover image
        if self.enlarge:
            size = (
                int(self.w * self.enlarge_amount),
                int(self.h * self.enlarge_amount),
            )
            self.dx, self.dy = size[0] - self.w, size[1] - self.h
            self.hover_image = pygame.transform.scale(self.hover_image, size)
        # put the text over images, if enlarge, create a bigger font so resolution stays high
        if self.text != "":
            txt = self.font.render(self.text, True, self.text_colour)
            self.image.blit(
                txt, ((self.w - txt.get_width()) // 2, (self.h - txt.get_height()) // 2)
            )
            if self.enlarge:
                txt = self.enlarge_font.render(self.text, True, self.text_colour)
            self.hover_image.blit(
                txt,
                (
                    (self.hover_image.get_width() - txt.get_width()) // 2,
                    (self.hover_image.get_height() - txt.get_height()) // 2,
                ),
            )
        # if the user gives both images, check to see if different sizes so know if enlarged or not
        if (
            self.hover_image.get_width() != self.w
            or self.hover_image.get_height() != self.h
        ):
            self.enlarge = True
            self.dx, self.dy = (
                self.hover_image.get_width() - self.w,
                self.hover_image.get_height() - self.h,
            )
        # convert the images so it is faster to put on screen
        self.image.convert()
        self.hover_image.convert()

    # if no width or height is given, calculate it with length of text
    def _caclulate_size(self):
        txt = self.font.render(self.text, False, (0, 0, 0))
        self.w = txt.get_width() + self.w * 2 + self.padding_x * 2
        self.h = txt.get_height() + self.h * 2 + self.padding_y * 2
        if self.center:
            self.x -= self.w // 2
            self.y -= self.h // 2


    # this is what will be shown when print(button)
    def __str__(self):
        if self.text:
            return "Button: '" + self.text + "'"
        else:
            return "Button: at (" + str(self.x) + ", " + str(self.y) + ")"

    # update the text of the button, remake the surfaces for the button
    def Update_text(self, text):
        self.text = text
        if self.caclulateSize:
            self._caclulate_size()
        self._Generate_images()

    # update the button, this should get called every frame
    def update(self, global_pos = None) -> bool:
        super().update(global_pos)
        # draw
        self._draw()
        # return if the button was clicked on
        return self.clicked

    def create_button(self):
        self._Generate_images()

    # draw the button
    def _draw(self):
        if self.hover:
            if self.enlarge:
                self.surface.blit(
                    self.hover_image, (self.x - self.dx // 2, self.y - self.dy // 2)
                )
            else:
                self.surface.blit(self.hover_image, (self.x, self.y))
        else:
            self.surface.blit(self.image, (self.x, self.y))


class Slider(Base_Widget):
    def __init__(self, x, y, w, h, params={}):
        """
        this is confusing
        basically, 
        self.x/y/w/h is the position of the slider, but in __init__, self.x/y/w/h is the position of the background
        
        """
        options = {
            "slider_width": None,
            "slider_color": (200, 200, 200),
            "starting_value": None,
            "range": [0, 1],
            "slider_height": None,
            "step": 0,
            "direction": "horizontal",
            "slider_image": None,
            "slider_curve": 0,
        }

        options = super().__init__(x, y, w, h, "slider", params, options)


        self.direction = options["direction"]
        self.step = options["step"]
        if self.direction not in ["horizontal", "vertical"]:
            raise ValueError(
                "option 'direction' is not a direction, (%d)" % (self.direction)
            )
        self.val_range = options["range"]
        val_dif = self.val_range[1] - self.val_range[0]
        self.slider_bg = options["slider_color"]
        self.slider_image = options["slider_image"]
        self.round = self.step / val_dif

        if self.image is None:
            self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.image.blit(curve_square(self.w, self.h, self.curve, self.background_color), (0, 0))
        elif self.w == 0 or self.h == 0:
            self.w, self.h = self.image.get_size()

        # get slider width and height
        slider_h = options["slider_height"] # height of the slider is always the short side of the slider
        if slider_h is None:
            slider_h = self.h if self.direction == "horizontal" else self.w
        slider_w = (
            options["slider_width"] if options["slider_width"] is not None else slider_h
        )
        # get the starting value
        if options["starting_value"] is not None:
            self._val = constrain(
                options["starting_value"], self.val_range[0], self.val_range[1], 0, 1
            )
        else:
            self._val = 0.5
        # create the slider
        if self.slider_image is None:
            self.slider_image = pygame.Surface((slider_w, slider_h), pygame.SRCALPHA)
            self.slider_image.blit(curve_square(slider_w, slider_h, options['slider_curve'], self.slider_bg), (0, 0))
        else:
            slider_h = self.slider_image.get_height()
            slider_w = self.slider_image.get_width()

        #quick fix for clicking on the slider, not the background
        self.bg_rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.direction == "horizontal":
            self.y -= (slider_h - self.bg_rect.h) // 2
        else:
            self.x -= (slider_w - self.bg_rect.w) // 2
        # print(self.w, self.h, slider_w, slider_h)
        self.w, self.h = slider_w, slider_h
        self._calculate_slider_pos()

        self.slider_image.convert()
        self.image.convert()

    # draw the slider
    def _draw(self):
        self.surface.blit(self.image, self.bg_rect)
        self.surface.blit(self.slider_image, (self.x, self.y))
    
    def _calculate_slider_pos(self):
        self._val = round_to_num(self._val, self.round) if self.round != 0 else self._val
        if self.direction == "horizontal":
            self.x = self.bg_rect.x +  self._val * (self.bg_rect.w - self.w)
        else:
            self.y = self.bg_rect.y +  self._val * (self.bg_rect.h - self.h)

    # updates the slider, this should be called every frame
    def update(self):
        super().update((0, 0))
        if self.hold:
            mouse_pos = pygame.mouse.get_pos()
            if self.direction == "horizontal":
                self._val = (mouse_pos[0] - self.bg_rect.x) / self.bg_rect.w
                self._val = max(min(self._val, 1), 0)
                self._calculate_slider_pos()
            else:
                self._val = (mouse_pos[1] - self.bg_rect.y) / self.bg_rect.h
                self._val = max(min(self._val, 1), 0)
                self._calculate_slider_pos()
        self._draw()
        return self.value()


    #returns the value the slider is at
    def value(self) -> int:
        val = constrain(self._val, 0, 1, self.val_range[0], self.val_range[1])
        if isinstance(self.step, int) and self.step != 0:
            val = int(val)
        return val

    #sets the value of the slider, moveing the slider object to that position
    def set_value(self, val: Union[float, int]):
        self._val = constrain(val, self.val_range[0], self.val_range[1], 0, 1)
        self._calculate_slider_pos()


class TextBox(Base_Widget):
    def __init__(self, x, y, w, h=0, params={}):
        options = {
            "max_lines": 1,
            "text": "",
            "padding_x": 2,
            "padding_y": 2,
            "cursor": True,
            "on_return": None,
            "calculate_size": False,
            "typing": True,
        }
        options = super().__init__(x, y, w, h, "button", params, options)
        options.update(params)

        self.cursor = options["cursor"]
        self.current_line = 0
        self.current_col = len(options["text"])
        self.lines = options["max_lines"]
        if isinstance(options["text"], str):
            self.text = options["text"].split("\n")
        else:
            self.text = options["text"]
        self.margin = options["padding_x"]
        self.margin_y = options["padding_y"]
        self.Enter_action = options["on_enter"]
        if options["calculate_size"] or self.h == 0:
            self.h = self._get_font_height() + h
        self.typing = options["typing"]
        self.enter = False

        if self.image is None:
            surf = pygame.Surface((self.w, self.h*self.lines + self.margin_y//2), pygame.SRCALPHA)
            surf.blit(curve_square(self.w, self.h* self.lines + self.margin_y//2, self.curve, self.background_color), (0, 0))
            self.image = surf
        self.h = self.image.get_height()

    # get the width of the text using the font
    def _get_text_width(self, text):
        text = "".join(text)
        if len(text) == 0:
            return 0
        obj = self.font.render(text, True, (0, 0, 0))
        return obj.get_width()

    # returns the height of the font
    def _get_font_height(self):
        obj = self.font.render(" ", True, (0, 0, 0))
        return obj.get_height()

    def wrapper(self, change_cur=False):
        """
        Wraps the text in the text box.
        loop through each line, then loop through each character in the line,
        seeing if the next character is too far to the right. keep track of spaces
        to create new lines from there.
        
        """
        for cur_line, line in enumerate(self.text):
            for i in range(len("".join(line))):
                length = self._get_text_width("".join(line[:i]))
                if length > self.w - self.margin:
                    indexs = [
                        i for i, e in enumerate(self.text[cur_line][:i]) if e == " "
                    ]
                    if cur_line < self.lines - 1:
                        if len(indexs) == 0:
                            indexs.append(i - 1)
                        if change_cur and (self.current_line >= cur_line or self.current_col > len(self.text[self.current_line])):
                            self.current_line += 1
                            self.current_col -= indexs[-1] + 1
                        if cur_line == len(self.text) -1:
                            self.text.append(self.text[cur_line][indexs[-1]+1:])
                        else:
                            self.text[cur_line + 1] = (
                                self.text[cur_line][indexs[-1] + 1 :]
                                + self.text[cur_line+1]
                            )
                        self.text[cur_line] = self.text[cur_line][: indexs[-1]]
                        break

    # call this when the user presses a key down, supply the event from `pygame.event.get()`
    def key_down(self, e: pygame.event.Event):
        #if not selected, don't do anything
        if not self.typing:
            return
        # when backspace is pressed, delete last char
        if e.key == pygame.K_BACKSPACE:
            # if nothing in line, delete line
            if len(self.text[self.current_line]) == 0:
                if self.current_line > 0:
                    del self.text[self.current_line]
                    self.current_line -= 1
                    self.current_col = len(self.text[self.current_line])
            else:
                if self.current_col > 0:
                    self.text[self.current_line] = self.text[self.current_line][:self.current_col-1] + self.text[self.current_line][self.current_col:]
                    self.current_col -= 1
                else:
                    self.current_line -= 1
                    self.current_col = len(self.text[self.current_line])
                    self.text[self.current_line] = self.text[self.current_line] + self.text[self.current_line+1]
                    del self.text[self.current_line+1]
                    self.wrapper(True)
        # if key is enter, create line
        elif e.key == pygame.K_RETURN:
            self.enter = True
            if self.Enter_action is not None:
                self.Enter_action()
            elif self.current_line < self.lines - 1:
                self.text.insert(self.current_line+1, self.text[self.current_line][self.current_col:])
                self.current_line += 1
                self.current_col = len(self.text[self.current_line])
                if self.current_col > 0:
                    self.text[self.current_line-1] = self.text[self.current_line-1][:-self.current_col]
        # if key is a charachter, put on screen
        elif e.unicode != "":
            if len(self.text[self.current_line]) > 0:
                if self.text[self.current_line][-1] == "":
                    del self.text[self.current_line][-1]
            self.text[self.current_line] = (
                self.text[self.current_line][: self.current_col]
                + e.unicode
                + self.text[self.current_line][self.current_col :]
            )
            self.current_col += 1
            # wrapper
            if self._get_text_width(self.text[self.current_line]) > self.w:
                self.wrapper(True)
        # if the down arrow is pressed
        elif e.key == pygame.K_DOWN:
            self.current_line += 1 if self.current_line < len(self.text) - 1 else 0
            self.current_col = min(self.current_col, len(self.text[self.current_line]))
        # if the up arrow is pressed
        elif e.key == pygame.K_UP:
            self.current_line -= 1 if self.current_line > 0 else 0
            self.current_col = min(self.current_col, len(self.text[self.current_line]))
        # if the right arrow is pressed
        elif e.key == pygame.K_RIGHT:
            self.current_col += (
                1 if len(self.text[self.current_line]) > self.current_col else 0
            )
        # if the left arrow is pressed
        elif e.key == pygame.K_LEFT:
            self.current_col -= 1 if 0 < self.current_col else 0

    # draw the textbox
    def _draw(self):
        # draw background
        self.surface.blit(self.image, (self.x, self.y))
        # draw all text
        for line, text in enumerate(self.text):
            if len(text) != 0:
                txt = "".join(text)
                obj = self.font.render(txt, True, self.font_colour)
                self.surface.blit(obj, (self.x + self.margin//2, self.y + self.margin_y//2 + (self.h * line)))
        # draw cursor
        if self.cursor and self.typing:
            total = 0
            total = self._get_text_width(
                self.text[self.current_line][: self.current_col]
            )
            pygame.draw.line(
                self.surface,
                (0, 0, 0),
                (self.x + total + self.margin//2, self.y + self.margin_y//2 + (self.h * self.current_line)),
                (self.x + total + self.margin//2, self.y + self.margin_y//2 + self._get_font_height() + (self.h * (self.current_line))),
                2,
            )

    # update should be called every frame, it draws the textbox
    def update(self):
        super().update((0, 0))
        self._draw()
        if self.enter:
            self.enter = False
            return True
        return False

    # get the text of a specific line or lines
    def get_lines(self, lines=-1, return_as_string=False):
        # if user gives an int, check if it is -1 for all lines, else get specific line
        if isinstance(lines, int):
            if lines == -1:
                if len(self.text) > 1:
                    lines = (0, self.lines)
                else:
                    return self.text[0]
            else:
                if 0 > lines or self.lines < lines:
                    raise IndexError("line index not in range")
                if len(self.text) == 0:
                    return ""
                return "".join(self.text[lines])
        # if user wants a range of lines, get lines
        if isinstance(lines, tuple):
            if (
                lines[0] < 0
                or lines[0] > self.lines
                or lines[1] < 0
                or lines[1] > self.lines
                or lines[0] > lines[1]
            ):
                raise IndexError(
                    "line index is out of range: "
                    + str(lines)
                    + " (0, "
                    + str(str(self.lines))
                )
            string = []
            for x in range(lines[0], lines[1]):
                if len(self.text) > x:
                    string.append("".join(self.text[x]))
                else:
                    string.append("")
            if return_as_string:
                return "\n".join(string)
            return string


class slider_with_text:
    def __init__(self, hapi, slider, params={}):
        options = {
            "font": "calibri",
            "font_size": 20,
            "font_color": (0, 0, 0),
            "padding_y": 2,
            "padding_x": 0,
            "pivot": "top_left",
            "accuracy": 0,  # decimal points
        }

        if not isinstance(slider, Slider):
            raise TypeError("'Slider' argument is not a slider widget")

        check_params(params, options, "slider with text")

        options.update(params)

        self.font = pygame.font.Font(
            pygame.font.match_font(options["font"]), options["font_size"]
        )
        self.font_col = options["font_color"]
        self.rounder = options["accuracy"]
        self.pivot = options["pivot"]
        if self.pivot not in [
            "top_left",
            "top_right, bottom_left",
            "bottom_right",
            "top",
            "bottom",
            "left",
            "right",
        ]:
            raise TypeError("option: 'pivot' is not a valid pivot point")

        self.slider = slider
        self.hapi = hapi
        self.y = slider.y
        self._val = 0
        if "top" in self.pivot:
            self.y -= options["padding_y"] + self._get_text_height()
        elif "bottom" in self.pivot:
            self.y += options["padding_y"] + slider.h
        self.x = slider.x
        if "left" in self.pivot:
            self.x -= options["padding_x"]
        elif "right" in self.pivot:
            self.x += slider.w + options["padding_x"]
        else:
            self.x += slider.w // 2 + options["padding_x"]

    def update(self):
        self.slider.update()
        self._val = round(self.slider.value(), self.rounder)
        if self.rounder == 0:
            self._val = int(self._val)
        self._draw()

    def _draw(self):
        val = str(self._val)
        obj = self.font.render(val, True, self.font_col)
        if "left" in self.pivot:
            x = self.x - obj.get_width()
        elif not "right" in self.pivot:
            x = self.x - obj.get_width() // 2
        else:
            x = self.x
        if "top" in self.pivot:
            y = self.y - obj.get_height()
        y = self.y
        self.surface.blit(obj, (x, y))

    def _get_text_height(self):
        return self.font.render(" ", True, (0, 0, 0)).get_height()

    def value(self) -> int:
        return self.slider.value()


class Scroll:
    def __init__(self, hapi, params={}):
        options = {
            "starting_x": 0,
            "starting_y": 0,
            "range_x": 0,
            "range_y": 0,
            "bar_color": (200, 200, 200),
            "slider_color": (150, 150, 150),
        }
        check_params(params, options, "scroll")
        options.update(params)

        screen_size = pygame.display.get_surface().get_size()

        self.w, self.h = screen_size
        # create sliders for x and y axis
        self.x_slider = None
        self.y_slider = None
        if options["range_x"] > 0:
            self.x_slider = Slider(
                hapi,
                0,
                self.h - 20,
                self.w - 20,
                20,
                {
                    "starting_value": options["starting_x"],
                    "range": [0, options["range_x"]],
                    "slider_color": options["slider_color"],
                    "background_color": options["bar_color"],
                    "resize_slider": True,
                },
            )
        if options["range_y"] > 0:
            self.y_slider = Slider(
                hapi,
                self.w - 20,
                0,
                20,
                self.h - 20,
                {
                    "starting_value": options["starting_y"],
                    "range": [0, options["range_y"]],
                    "slider_color": options["slider_color"],
                    "background_color": options["bar_color"],
                    "direction": "vertical",
                    "resize_slider": True,
                },
            )

    # this is updates the sliders, this should be called every frame
    def update(self):
        if self.x_slider is not None:
            self.x_slider.update()
        if self.y_slider is not None:
            self.y_slider.update()
    
    #returns the scroll amount given an index e.g. 'scrollx = scroll[0]'
    def __getitem__(self, index : int):
        if index == 0:
            return -self.x_slider.value()
        elif index == 1:
            return -self.y_slider.value()
        return (-self.x_slider.value(), -self.y_slider.value())
