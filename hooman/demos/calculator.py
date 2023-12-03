from hooman import Hooman
import pygame

# Initialize Hooman and Pygame
h = Hooman(400, 600, "Calculator")
pygame.font.init()

# Set up fonts
font_big = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 36)

# Calculator variables
expression = ""
result = ""

# Store the previous state of the left mouse button
h.prev_left_button = False

# Function to evaluate the expression and update the result
def calculate():
    try:
        global result
        result = str(eval(expression))
    except:
        result = "Error"

# Function to handle button clicks
def handle_button_click(button_text):
    global expression, result
    if button_text == "=":
        calculate()
    elif button_text == "C":
        expression = ""
        result = ""
    else:
        expression += button_text

# Main loop
while h.is_running:
    h.background(h.color["white"])

    # Draw the input expression
    text_surface = font_big.render(expression, True, pygame.Color("black"))
    h.screen.blit(text_surface, (20, 50))

    # Draw the result
    text_surface = font_big.render(result, True, pygame.Color("green"))
    h.screen.blit(text_surface, (20, 100))

    # Draw calculator buttons
    buttons = [
        ("7", 20, 200), ("8", 120, 200), ("9", 220, 200), ("/", 320, 200),
        ("4", 20, 300), ("5", 120, 300), ("6", 220, 300), ("*", 320, 300),
        ("1", 20, 400), ("2", 120, 400), ("3", 220, 400), ("-", 320, 400),
        ("C", 20, 500), ("0", 120, 500), ("=", 220, 500),  # Removed the "." button
        ("+", 320, 500),
    ]
    button_size = 80

    for button in buttons:
        text, x, y = button
        pygame.draw.rect(h.screen, pygame.Color(200, 200, 200), (x, y, button_size, button_size))
        
        text_surface = font_small.render(text, True, pygame.Color("black"))
        text_rect = text_surface.get_rect(center=(x + button_size // 2, y + button_size // 2))
        h.screen.blit(text_surface, text_rect)
        
    # Check for left mouse button click
    mouse_x, mouse_y = pygame.mouse.get_pos()
    left_button, _, _ = pygame.mouse.get_pressed()

    if left_button and not h.prev_left_button:
        for button in buttons:
            text, x, y = button
            if x < mouse_x < x + button_size and y < mouse_y < y + button_size:
                handle_button_click(text)

    # Store the current state of the left button for the next iteration
    h.prev_left_button = left_button

    h.flip_display()
    h.event_loop()
