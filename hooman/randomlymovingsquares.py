from hooman import Hooman
import random


window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

bg_col = (0, 0, 0)


num_squares = 5
squares = []

for _ in range(num_squares):
    square_x = random.randint(50, window_width - 50)
    square_y = random.randint(50, window_height - 50)
    square_size = 30
    square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    square_speed = random.uniform(1, 3)
    square_direction = random.uniform(0, 2 * 3.1416)  
    squares.append((square_x, square_y, square_size, square_color, square_speed, square_direction))

def move_squares():
    for i, square in enumerate(squares):
        square_x, square_y, square_size, _, square_speed, square_direction = square
        square_x += square_speed * hapi.cos(square_direction)
        square_y += square_speed * hapi.sin(square_direction)

       
        if square_x < 0 or square_x > window_width - square_size:
            square_direction = hapi.PI - square_direction
        if square_y < 0 or square_y > window_height - square_size:
            square_direction = -square_direction

        squares[i] = (square_x, square_y, square_size, square_color, square_speed, square_direction)

hapi.handle_events = lambda event: None  

while hapi.is_running:
    hapi.background(bg_col)

   
    move_squares()

   
    for square in squares:
        square_x, square_y, square_size, square_color, _, _ = square
        hapi.fill(square_color)
        hapi.rect(int(square_x), int(square_y), int(square_size), int(square_size))

    
    hapi.flip_display()
    hapi.event_loop()

hapi.quit()