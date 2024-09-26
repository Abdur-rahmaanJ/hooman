import random
import pygame
from hooman import Hooman

# Target class
class Target:
    def __init__(self, window_width, window_height):
        self.size = 50
        self.x = random.randint(0, window_width - self.size)
        self.y = random.randint(0, window_height - self.size)
        self.window_width = window_width
        self.window_height = window_height

    def update_position(self):
        self.x = random.randint(0, self.window_width - self.size)
        self.y = random.randint(0, self.window_height - self.size)

    def draw(self):
        # Concentric circles to form a target
        scale = 1
        hapi.fill(255, 0, 0)
        hapi.circle(self.x - (self.size / (2.0 / scale)), self.y - (self.size / (2.0 / scale)), self.size * scale)

        scale = 0.8
        hapi.fill(255, 255, 255)
        hapi.circle(self.x - (self.size / (2.0 / scale)), self.y - (self.size / (2.0 / scale)), self.size * scale)

        scale = 0.6
        hapi.fill(255, 0, 0)
        hapi.circle(self.x - (self.size / (2.0 / scale)), self.y - (self.size / (2.0 / scale)), self.size * scale)

        scale = 0.4
        hapi.fill(255, 255, 255)
        hapi.circle(self.x - (self.size / (2.0 / scale)), self.y - (self.size / (2.0 / scale)), self.size * scale)

    # Get if clicked using signed distance function
    def is_clicked(self, mouse_x, mouse_y):
        return ((self.x - mouse_x) ** 2 + (self.y - mouse_y) ** 2) ** 0.6 <= self.size

# Setup game window and game variables
score = 1
clicks = 1
time = 0
width, height = 600, 600
hapi = Hooman(width, height)
clock = pygame.time.Clock()

# Define event handling function
def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events

# Game loop
target = Target(width, height)

while hapi.is_running:
    # Handle mouse clicks
    clock.tick(30)
    time += (clock.get_time() / 1000.0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hapi.is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = event.pos
            if target.is_clicked(mouse_x, mouse_y):
                target.update_position()
                score += 1
            clicks += 1
            
    # Draw
    hapi.background(141, 141, 141)
    target.draw()
    hapi.text(f"Accuracy: %{round(score * 100 / clicks, 2)}", 20, 20)
    hapi.text(f"TPS: {round((score - 1) / time, 2)}", 20, 40)
    hapi.text(f"Time: {round(time, 2)}", 20, 60)

    # Refresh screen
    hapi.flip_display()