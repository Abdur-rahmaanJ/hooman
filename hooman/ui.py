"""
Author: https://github.com/TheBigKahuna353
Edit: https://github.com/Abdur-rahmaanJ
"""

import pygame
from .formula import constrain
from typing import Union
from .check import check_params


class Button:
    def __init__(self, x, y, w, h, text, params={}):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

        options = {
            "surface": None,
            "hover_background_color": None,
            "font": "Calibri",
            "font_size": 30,
            "outline": False,
            "outline_thickness": 2,
            "outline_color": (0, 0, 0),
            "outline_half": False,
            "on_click": None,
            "on_hover_enter": None,
            "on_hover_exit": None,
            "on_hover": None,
            "on_hold": None,
            "image": None,
            "hover_image": None,
            "enlarge": False,
            "enlarge_amount": 1.1,
            "calculate_size": False,
            "dont_generate": False,
            "font_colour": (0, 0, 0),
            "background_color": (255, 255, 255),
            "curve": 0,
            "padding_x": 0,
            "padding_y": 0,
            "centered": False,
        }
        check_params(params, options, "button")
        options.update(params)

        for key, val in options.items():
            if key not in options:
                raise TypeError(key + " is not an option, have you spelt it correctly")

        self.padding_x = options["padding_x"]
        self.padding_y = options["padding_y"]
        self.surface = options["surface"]
        self.text_colour = options["font_colour"]
        self.background_color = options["background_color"]
        self.hover_bg_colour = options["hover_background_color"]
        self.curve = options["curve"]
        font = options["font"]
        font_size = options["font_size"]
        self.outline = options["outline"]
        self.outline_col = options["outline_color"]
        self.outline_half = options["outline_half"]
        self.outline_amount = options["outline_thickness"]
        self.on_click = options["on_click"]
        self.on_hover_enter = options["on_hover_enter"]
        self.on_hover_exit = options["on_hover_exit"]
        self.on_hover = options["on_hover"]
        self.on_hold = options["on_hold"]
        image = options["image"]
        dont_generate = options["dont_generate"]
        self.caclulateSize = options["calculate_size"]
        self.hover_image = options["hover_image"]
        self.enlarge = options["enlarge"]
        self.enlarge_amount = options["enlarge_amount"]
        self.center = options["centered"]

        # if no surface is supplied, try getting main screen
        if self.surface is None:
            self.surface = pygame.display.get_surface()
            if self.surface is None:
                raise ValueError("No surface to blit to")

        if self.hover_bg_colour is None:
            self.hover_bg_colour = self.background_color
        
        self.font = pygame.font.Font(pygame.font.match_font(font), font_size)

        self.image = image.copy() if image else None
        self.clicked_on = False
        self.draw = False

        if self.enlarge:
            if self.text != "":
                self.enlarge_font = pygame.font.Font(
                    pygame.font.match_font(font), int(font_size * self.enlarge_amount)
                )
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
                        raise ValueError(
                            "cannot calculate width and height without text"
                        )
            self._Generate_images()
        if self.center:
            self.x -= self.w // 2
            self.y -= self.h // 2

    def _Generate_images(self):
        # generate images
        # if no image, create the button by drawing
        if self.image is None or self.draw:
            self.draw = True
            self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.hover_image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.image.blit(
                curve_square(self.w, self.h, self.curve, self.background_color), (0, 0)
            )
            self.hover_image.blit(
                curve_square(self.w, self.h, self.curve, self.hover_bg_colour), (0, 0)
            )
            # self.hover_image.fill(self.background_color)
            if self.outline:
                self.hover_image.blit(
                    curve_square(self.w, self.h, self.curve, self.outline_col), (0, 0)
                )
                self.hover_image.blit(
                    curve_square(
                        self.w - self.outline_amount * 2,
                        self.h - self.outline_amount * 2,
                        self.curve,
                        self.hover_bg_colour,
                    ),
                    (self.outline_amount, self.outline_amount),
                )
            elif self.outline_half:
                self.hover_image.blit(
                    curve_square(self.w, self.h, self.curve, self.outline_col), (0, 0)
                )
            self.hover_image.convert()
            self.image.convert()
        # if the user gives an image, create the image when the mouse hovers over
        elif self.hover_image is None or self.draw:
            self.hover_image = self.image.copy()
            if not self.outline is None:
                pygame.draw.rect(
                    self.hover_image,
                    (0, 0, 0, 255),
                    (0, 0, self.w, self.outline_amount),
                )
                pygame.draw.rect(
                    self.hover_image,
                    (0, 0, 0, 255),
                    (0, 0, self.outline_amount, self.h),
                )
                pygame.draw.rect(
                    self.hover_image,
                    (0, 0, 0, 255),
                    (self.w, self.h, -self.w, -self.outline_amount),
                )
                pygame.draw.rect(
                    self.hover_image,
                    (0, 0, 0, 255),
                    (self.w, self.h, -self.outline_amount, -self.h),
                )
            self.hover_image.convert_alpha()
            self.image.convert_alpha()
        # enlarge the image, no matter if user gives an image or not
        if self.enlarge:
            size = (
                int(self.w * self.enlarge_amount),
                int(self.h * self.enlarge_amount),
            )
            self.dx, self.dy = size[0] - self.w, size[1] - self.h
            self.hover_image = pygame.transform.scale(self.image, size)
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
        self.w = txt.get_width() + self.w + self.padding_x * 2
        self.h = txt.get_height() + self.h + self.padding_y * 2

    # return a pygame.Rect of the button
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.w, self.h)

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
    def update(self) -> bool:
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        returnee = False
        # check if mouse over button
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
                # on_hover_enter event
                if self.hover == False:
                    if self.on_hover_enter:
                        self.on_hover_enter(self)

                self.hover = True
                # on_hover event
                if self.on_hover:
                    self.on_hover(self)

                # check for click, if held down, action only gets called once AT MOUSEUP

                #check to see if the click started on the button
                if click and not self.prev_clicked_state:
                    self.clicked_on = True

                # wait till the user stops clicking to call on_click
                if self.prev_clicked_state and self.clicked_on and click == False:
                    if self.on_click:
                        """
                        if self.on_click_arg:
                            self.on_click(self.on_click_arg)
                        else:
                            self.on_click()
                        """
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
                self.surface.blit(
                    self.hover_image, (self.x - self.dx // 2, self.y - self.dy // 2)
                )
            else:
                self.surface.blit(self.hover_image, (self.x, self.y))
        else:
            self.surface.blit(self.image, (self.x, self.y))

    def width(self) -> int:
        txt = self.font.render(self.text, False, (0, 0, 0))
        w = txt.get_width() + self.w + self.padding_x * 2
        return w

    def height(self) -> int:
        txt = self.font.render(self.text, False, (0, 0, 0))
        h = txt.get_height() + self.h + self.padding_y * 2
        return


# this creates a curved rect, given a w,h and the curve amount, bewtween 0 and 1
def curve_square(width, height, curve, color=(0, 0, 0)):
    if not 0 <= curve <= 1:
        raise ValueError("curve value out of range, must be between 0 and 1")
    curve /= 2
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


class Slider:
    def __init__(self, hapi, x, y, w, h, params={}):
        options = {
            "background_color": (100, 100, 100),
            "slider_width": None,
            "slider_color": (200, 200, 200),
            "starting_value": None,
            "value_range": [0, 1],
            "slider_height": None,
            "step": 0,
            "image": None,
            "direction": "horizontal",
            "resize_slider": False,
            "curve": 0,
        }
        check_params(params, options, "slider")
        options.update(params)

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hapi = hapi
        self.direction = options["direction"]
        if self.direction not in ["horizontal", "vertical"]:
            raise ValueError(
                "option 'direction' is not a direction, (%d)" % (self.direction)
            )
        self.bg = options["background_color"]
        # if the user gives an image for slider background, use that instead of drawing one
        if options["image"] is not None:
            self.image = pygame.Surface((self.w, self.h))
            self.image.blit(options["image"], (0, 0))
        else:
            self.image = None
        self.val_range = options["value_range"]
        self.curve = options["curve"]
        self.resize = options["resize_slider"]
        val_dif = self.val_range[1] - self.val_range[0]
        self.slider_bg = options["slider_color"]
        self.slider_h = options["slider_height"]
        if self.slider_h is None:
            if self.direction == "horizontal":
                self.slider_h = h
            else:
                self.slider_h = w
        self.step = options["step"]
        if self.direction == "horizontal":
            self.slider_w = (
                options["slider_width"] if options["slider_width"] is not None else h
            )
        else:
            self.slider_w = (
                options["slider_width"] if options["slider_width"] is not None else w
            )
        if options["starting_value"] is not None:
            self.val = constrain(
                options["starting_value"], self.val_range[0], self.val_range[1], 0, 1
            )
        else:
            self.val = 0.5
        if self.resize:
            range_ = self.val_range[1] - self.val_range[0]
            if self.direction == "horizontal":
                if range_ < self.w:
                    self.slider_w = self.w - range_
            else:
                if range_ < self.h:
                    self.slider_h = self.h - range_
        self.screen = pygame.display.get_surface()
        if self.direction == "horizontal":
            self.slider_rect = pygame.Rect(
                self.x + self.val * (self.w - self.slider_w),
                self.y + (self.h - self.slider_h) // 2,
                self.slider_w,
                self.slider_h,
            )
        else:
            self.slider_rect = pygame.Rect(
                self.x + (self.w - self.slider_w) // 2,
                self.y + self.val * (self.h - self.slider_h),
                self.slider_w,
                self.slider_h,
            )
        self.clicked_on = False
        self.prev_click = False

    # draw the slider
    def _draw(self):
        if self.image is not None:
            self.hapi.screen.blit(self.image, (self.x, self.y))
        elif self.curve == 0:
            pygame.draw.rect(
                self.hapi.screen, self.bg, (self.x, self.y, self.w, self.h)
            )
        else:
            self.hapi.screen.blit(
                curve_square(self.w, self.h, self.curve, self.bg), (self.x, self.y)
            )
        if self.curve == 0:
            pygame.draw.rect(self.hapi.screen, self.slider_bg, self.slider_rect)
        else:
            self.hapi.screen.blit(
                curve_square(self.slider_w, self.slider_h, self.curve, self.slider_bg),
                self.slider_rect,
            )

    # updates the slider, this should be called every frame
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if self.slider_rect.collidepoint(mouse_pos):
            # check for click, if held down, action only gets called once
            if click and not self.prev_click:
                self.clicked_on = True
        if self.clicked_on:
            if self.direction == "horizontal":
                self.val = (mouse_pos[0] - self.x) / self.w
                self.val = max(min(self.val, 1), 0)
                self.val = self._get_val(self.val)
                self.slider_rect.x = self.x + self.val * (self.w - self.slider_w)
            else:
                self.val = (mouse_pos[1] - self.y) / self.h
                self.val = max(min(self.val, 1), 0)
                self.val = self._get_val(self.val)
                self.slider_rect.y = self.y + self.val * (self.h - self.slider_h)
        if not click:
            self.clicked_on = False
        self.prev_click = click
        self._draw()

    def Move(self, x=0, y=0, dx=0, dy=0):
        self.x = x if x != 0 else self.x
        self.y = y if y != 0 else self.y
        self.x += dx
        self.y += dy
        if self.direction == "horizontal":
            self.slider_rect = pygame.Rect(
                self.x + self.val * (self.w - self.slider_w),
                self.y + (self.h - self.slider_h) // 2,
                self.slider_w,
                self.slider_h,
            )
        else:
            self.slider_rect = pygame.Rect(
                self.x + (self.w - self.slider_w) // 2,
                self.y + self.val * (self.h - self.slider_h),
                self.slider_w,
                self.slider_h,
            )

    #returns the value the slider is at
    def value(self) -> int:
        val = constrain(self.val, 0, 1, self.val_range[0], self.val_range[1])
        if isinstance(self.step, int) and self.step != 0:
            val = int(val)
        return val

    #sets the value of the slider, moveing the slider object to that position
    def set_value(self, val: Union[float, int]):
        self.val = constrain(val, self.val_range[0], self.val_range[1], 0, 1)
        if self.direction == "horizontal":
            self.slider_rect.x = self.x + self.val * (self.w - self.slider_w)
        else:
            self.slider_rect.y = self.y + self.val * (self.h - self.slider_h)

    # if the slider has a step and is not contineous, round to nearest step size
    def _get_val(self, val):
        if self.step == 0:
            return val
        else:
            a = constrain(val, 0, 1, self.val_range[0], self.val_range[1])
            b = self.hapi.round_to(a, self.step)
            c = constrain(b, self.val_range[0], self.val_range[1], 0, 1)
            # print(val, a, b, c)
            return c


class TextBox:
    def __init__(self, x, y, w, h=0, params={}):
        options = {
            "max_lines": 1000,
            "text": "",
            "background_color": (255, 255, 255),
            "font_size": 30,
            "font": "Calibri",
            "text_colour": (0, 0, 0),
            "surface": None,
            "margin": 2,
            "cursor": True,
            "on_enter": None,
            "calculate_size": False,
        }
        check_params(params, options, "text box")
        options.update(params)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cursor = options["cursor"]
        self.current_line = 0
        self.current_col = len(options["text"])
        self.lines = options["lines"]
        self.font = pygame.font.Font(
            pygame.font.match_font(options["font"]), options["font_size"]
        )
        self.text_colour = options["text_colour"]
        self.text = [list(options["text"])]
        self.char_length = [self._get_text_width(x) for x in self.text]
        self.background = options["background_color"]
        self.surface = (
            options["surface"]
            if options["surface"] is not None
            else pygame.display.get_surface()
        )
        self.margin = options["margin"]
        self.Enter_action = options["on_enter"]
        if self.surface == None:
            raise ValueError("No surface to blit to")
        # if no surface is supplied, get window
        if self.surface == None:
            self.surface = pygame.display.get_surface()
            if self.surface == None:
                raise ValueError("No surface to blit to")
        if options["calculateSize"] or self.h == 0:
            self.h = self._get_font_height() + h

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
        for cur_line, line in enumerate(self.text):
            for i in range(len("".join(line))):
                length = self._get_text_width("".join(line[:i]))
                if length > self.w:
                    indexs = [
                        i for i, e in enumerate(self.text[cur_line][:i]) if e == " "
                    ]
                    if cur_line < self.lines - 1:
                        if len(indexs) == 0:
                            indexs.append(i - 1)
                        if change_cur:
                            self.current_line += 1
                            self.current_col = len(self.text[cur_line]) - indexs[-1] - 1
                        if cur_line < len(self.text):
                            self.text.append(self.text[cur_line][indexs[-1] + 1 :])
                        else:
                            self.text[cur_line + 1] = (
                                self.text[cur_line][indexs[-1] + 1 :]
                                + self.text[cur_line]
                            )
                        self.text[cur_line] = self.text[cur_line][: indexs[-1]]
                        break

    # call this when the user presses a key down, supply the event from `pygame.event.get()`
    def key_down(self, e: pygame.event.Event):
        # when backspace is pressed, delete last char
        if e.key == pygame.K_BACKSPACE:
            # if nothing in line, delete line
            if len(self.text[self.current_line]) == 0:
                if self.current_line > 0:
                    del self.text[self.current_line]
                    self.current_line -= 1
                    self.current_col = len(self.text[self.current_line])
            else:
                del self.text[self.current_line][-1]
                self.current_col -= 1
        # if key is enter, create line
        elif e.key == pygame.K_RETURN:
            if self.Enter_action is not None:
                self.Enter_action()
            elif self.current_line < self.lines - 1:
                self.current_line += 1
                self.text.append([""])
                self.char_length.append([0])
                self.current_col = 0
        # if key is a charachter, put on screen
        elif e.unicode != "":
            if len(self.text[self.current_line]) > 0:
                if self.text[self.current_line][-1] == "":
                    del self.text[self.current_line][-1]
            self.text[self.current_line] = (
                self.text[self.current_line][: self.current_col]
                + [e.unicode]
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
        pygame.draw.rect(
            self.surface, self.background, (self.x, self.y, self.w, self.h * self.lines)
        )
        # draw all text
        for line, text in enumerate(self.text):
            if len(text) != 0:
                txt = "".join(text)
                obj = self.font.render(txt, True, self.text_colour)
                self.surface.blit(obj, (self.x + self.margin, self.y + (self.h * line)))
        # draw cursor
        if self.cursor:
            total = 0
            total = self._get_text_width(
                self.text[self.current_line][: self.current_col]
            )
            pygame.draw.line(
                self.surface,
                (0, 0, 0),
                (self.x + total, self.y + (self.h * self.current_line)),
                (self.x + total, self.y + self._get_font_height() + (self.h * (self.current_line))),
                2,
            )

    # update should be called every frame, it draws the textbox
    def update(self):
        self._draw()

    # get the text of a specific line or lines
    def get_lines(self, lines=-1, return_as_string=False):
        pas = False
        # if user gives an int, check if it is -1 for all lines, else get specific line
        if isinstance(lines, int):
            if lines == -1:
                lines = (0, self.lines)
                pas = True
            if not pas:
                if 0 > lines or self.lines < lines:
                    raise IndexError("line index not in range")
                if len(self.text) < lines:
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
        self.val = 0
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
        self.val = round(self.slider.value(), self.rounder)
        if self.rounder == 0:
            self.val = int(self.val)
        self._draw()

    def _draw(self):
        val = str(self.val)
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
        self.hapi.screen.blit(obj, (x, y))

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
                    "value_range": [0, options["range_x"]],
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
                    "value_range": [0, options["range_y"]],
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
