from hooman import Hooman
import pygame
import ctypes


h = Hooman(600, 800)  
pygame.font.init()


font_big = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 36)


expression = ""
result = ""


h.prev_left_button = False


def calculate():
    try:
        global result
        result = str(eval(expression))
    except:
        result = "Error"


def handle_button_click(button_text):
    global expression, result
    if button_text == "=":
        calculate()
    elif button_text == "C":
        expression = ""
        result = ""
    else:
        expression += button_text


while h.is_running:
    h.background(h.color["grey"])  

    
    text_surface = font_big.render(expression, True, pygame.Color("white"))
    h.screen.blit(text_surface, (20, 50))

    
    text_surface = font_big.render(result, True, pygame.Color("black"))
    h.screen.blit(text_surface, (20, 100))

    
    buttons = [
        ("7", 20, 200, 120, 80), ("8", 160, 200, 120, 80), ("9", 300, 200, 120, 80), ("/", 440, 200, 120, 80),
        ("4", 20, 300, 120, 80), ("5", 160, 300, 120, 80), ("6", 300, 300, 120, 80), ("*", 440, 300, 120, 80),
        ("1", 20, 400, 120, 80), ("2", 160, 400, 120, 80), ("3", 300, 400, 120, 80), ("-", 440, 400, 120, 80),
        ("C", 20, 500, 120, 80), ("0", 160, 500, 120, 80), ("=", 300, 500, 120, 80),  # Removed the "." button
        ("+", 440, 500, 120, 80),
    ]

    for button in buttons:
        text, x, y, width, height = button
        pygame.draw.rect(h.screen, pygame.Color(200, 200, 200), (x, y, width, height))
        
        text_surface = font_small.render(text, True, pygame.Color("blue"))
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        h.screen.blit(text_surface, text_rect)
        
   
    mouse_x, mouse_y = pygame.mouse.get_pos()
    left_button, _, _ = pygame.mouse.get_pressed()

    if left_button and not h.prev_left_button:
        for button in buttons:
            text, x, y, width, height = button
            if x < mouse_x < x + width and y < mouse_y < y + height:
                handle_button_click(text)

   
    h.prev_left_button = left_button

    h.flip_display()
    h.event_loop()
