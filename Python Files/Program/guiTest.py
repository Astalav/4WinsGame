import pgzrun
import math

WIDTH = 900
HEIGHT = 600
BLUE = 0, 50, 200
BOX = Rect((20, 150), (500,450))

def draw():
    # draw empty field
    # circle radius = 30, space between = 10, startX = 60, startY = 565
    screen.fill((255, 255, 255))
    screen.draw.filled_rect(BOX, BLUE)
    for y in range (0,6):    
        for x in range(0, 7):
            screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 255, 255))

    # draw 'stone' appending to given field
    field = 13
    y = 6 - math.ceil((field +1) / 7)
    x = field - math.floor((field) / 7)*7
    screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 0, 0))

pgzrun.go()