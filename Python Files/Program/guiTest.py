import pgzrun
import math


def draw():
    # draw empty field
    # circle radius = 30, space between = 10, startX = 60, startY = 565
    WIDTH = 900
    HEIGHT = 600
    blue = 0, 50, 200
    box = Rect((20, 150), (500,450))
    
    screen.fill((255, 255, 255))
    screen.draw.filled_rect(box, blue)
    for y in range (0,6):    
        for x in range(0, 7):
            screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 255, 255))

    # draw 'stone' appending to given field
    drawRed(13)
    drawYellow(12)


def drawRed(field):
    y = 6 - math.ceil((field +1) / 7)
    x = field - math.floor((field) / 7)*7
    circle = screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 0, 0))

def drawYellow(field):
    y = 6 - math.ceil((field +1) / 7)
    x = field - math.floor((field) / 7)*7
    screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 255, 0))


pgzrun.go()