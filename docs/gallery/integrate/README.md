integrate

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/integrate.gif)

```python
# from https://pythonguides.com/create-a-game-using-python-pygame/
# Hooman >= 0.8.2

'''
Integrating hooman with existing codebase
'''

import pygame


from hooman import Hooman # <-- this


black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 5
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0) 
grid[1][5] = 1
pygame.init()
window_size = [255, 255]
scr = pygame.display.set_mode(window_size)
hapi = Hooman(integrate=True, screen=scr) # <-- this
pygame.display.set_caption("Grid")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
    scr.fill(black)
    for row in range(10):
        for column in range(10):
            color = white
            if grid[row][column] == 1:
                color = red
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(50)
    pygame.display.flip()
    hapi.record() # <-- this
pygame.quit()
hapi.save_record('integrate.mp4') # <-- this
```