import random
import pygame  # Import pygame
from hooman import Hooman

# Balloon class
class Balloon:
    def __init__(self, window_width, window_height):
        self.x = random.randint(0, window_width)
        self.y = window_height
        self.size = random.randint(20, 50)
        self.speed = random.uniform(1.0, 3.0)

    def update(self):
        self.y -= self.speed

    def is_clicked(self, mouse_x, mouse_y):
        return ((self.x - mouse_x) ** 2 + (self.y - mouse_y) ** 2) ** 0.5 <= self.size

# Initialize Hooman
hapi = Hooman(600, 800)

# Define event handling function
def handle_events(event):
    print("Event detected:", event)
    if event.type == pygame.QUIT:
        hapi.is_running = False

# Assign the event handling function
hapi.handle_events = handle_events

# Initialize balloons
balloons = [Balloon(600, 800) for _ in range(10)]

# Initialize score
score = 0

# Game loop
while hapi.is_running:
    # Handle mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hapi.is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = event.pos
            for balloon in balloons:
                if balloon.is_clicked(mouse_x, mouse_y):
                    score += int(100 / balloon.size)  # Score based on balloon size
                    balloons.remove(balloon)
                    balloons.append(Balloon(600, 800))  # Add new balloon

    # Update balloons
    for balloon in list(balloons):  # Iterate over a copy of the list
        balloon.update()
        if balloon.y + balloon.size < 0:  # Remove balloon if off-screen
            balloons.remove(balloon)
            balloons.append(Balloon(600, 800))  # Add new balloon

    # Draw
    hapi.background(135, 206, 250)
    for balloon in balloons:
        hapi.fill(255, 0, 0)
        hapi.ellipse(balloon.x, balloon.y, balloon.size, balloon.size)

    # Draw score
    hapi.fill(0)
    hapi.text(f"Score: {score}", 20, 20)

    # Refresh the screen
    hapi.flip_display()

pygame.quit()
