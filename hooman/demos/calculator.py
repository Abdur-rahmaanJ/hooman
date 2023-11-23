import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 300, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

# Set up colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Initialize calculator state
calculator_state = {
    'input': '',
    'output': ''
}

def draw_button(x, y, width, height, color, label):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text = font.render(label, True, BLACK)
    screen.blit(text, (x + 20, y + 20))

def update_display():
    pygame.draw.rect(screen, WHITE, (10, 10, 280, 50))
    font = pygame.font.Font(None, 24)
    input_text = font.render(calculator_state['input'], True, BLACK)
    output_text = font.render(calculator_state['output'], True, BLACK)
    screen.blit(input_text, (20, 30))
    screen.blit(output_text, (20, 50))

def main():
    # Define button positions
    button_positions = [
        (10, 80), (90, 80), (170, 80), (250, 80),
        (10, 160), (90, 160), (170, 160), (250, 160),
        (10, 240), (90, 240), (170, 240), (250, 240),
        (10, 320), (90, 320), (170, 320), (250, 320),
    ]

    # Define button labels
    button_labels = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    # Create calculator buttons
    buttons = []
    for label, (x, y) in zip(button_labels, button_positions):
        draw_button(x, y, 70, 70, GRAY, label)
        buttons.append((x, y, 70, 70, label))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for button in buttons:
                    bx, by, bwidth, bheight, blabel = button
                    if x >= bx and x <= bx + bwidth and y >= by and y <= by + bheight:
                        handle_button_click(blabel)

        # Update the display
        update_display()
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()

def handle_button_click(label):
    global calculator_state

    if label == 'C':
        calculator_state['input'] = ''
        calculator_state['output'] = ''
    elif label == '=':
        try:
            calculator_state['output'] = str(eval(calculator_state['input']))
        except Exception as e:
            calculator_state['output'] = 'Error'
    else:
        calculator_state['input'] += label

if __name__ == "__main__":
    main()
