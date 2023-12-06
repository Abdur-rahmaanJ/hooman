import pygame
from hooman import Hooman

# Initialize Pygame and Hooman
pygame.init()
window_width, window_height = 600, 400
hapi = Hooman(window_width, window_height)

# Colors and Constants
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WORK_TIME = 25 * 60  # 25 minutes
BREAK_TIME = 5 * 60  # 5 minutes
FPS = 30

# Timer Class


class Timer:
    def __init__(self, work_duration, break_duration):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.reset()

    def reset(self):
        self.current_time = self.work_duration
        self.work_mode = True

    def update(self):
        self.current_time -= 1
        if self.current_time <= 0:
            if self.work_mode:
                self.current_time = self.break_duration
            else:
                self.current_time = self.work_duration
            self.work_mode = not self.work_mode

    def draw(self):
        time_str = "{:02d}:{:02d}".format(
            self.current_time // 60, self.current_time % 60)
        color = GREEN if self.work_mode else RED
        mode_str = "Work Time" if self.work_mode else "Break Time"

        hapi.fill(color)
        hapi.text(time_str, window_width//2 - 50, window_height//2 - 20)
        hapi.text(mode_str, window_width//2 - 50, window_height//2 + 20)


# Initialize Timer
timer = Timer(WORK_TIME, BREAK_TIME)

# Main Loop
while hapi.is_running:
    hapi.background(0, 0, 0)

    # Update and draw the timer
    timer.update()
    timer.draw()

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hapi.is_running = False

    # Update Display
    hapi.flip_display()
    hapi.event_loop()
    pygame.time.Clock().tick(FPS)

pygame.quit()
