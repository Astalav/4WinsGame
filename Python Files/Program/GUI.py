import pgzrun
import math

from abc import ABC, abstractmethod
from Field import Field
import Player

class GUI(Field): 
    def __init__ (self): 
        Field.__init__(self) 
        self.__restart = Actor('restart', (540, 165))
        self.__undo = Actor('back', (575, 165))
        
    def __drawRed(self, field):
    # draws a red Stone in given field
        y = 6 - math.ceil((field +1) / 7)
        x = field - math.floor((field) / 7)*7
        screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 0, 0))

    def __drawYellow(self, field):
    # draws a yellow Stone in given field
        y = 6 - math.ceil((field +1) / 7)
        x = field - math.floor((field) / 7)*7
        screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255,215,0))

    def draw(self):
    # draws field with current status

        #draw white screen
        WIDTH = 900
        HEIGHT = 600
        screen.fill((255, 255, 255))

        #draw empty playground
        blue = 0, 50, 200
        box = Rect((20, HEIGHT-450), (500, 450))        
        screen.draw.filled_rect(box, blue)

        # circle radius = 30, space between = 10, startX = 60, startY = 565
        for y in range (0,6):    
            for x in range(0, 7):
                screen.draw.filled_circle((60 + x * 70, HEIGHT - 35 - 70 * y), 30, (255, 255, 255))

        # draw 'stone' appending to given field
        for x in self._yellow:
            self.__drawYellow(x)

        for x in self._red:
            self.__drawRed(x)

        self.__restart.draw()
        self.__undo.draw()

        # give message if there is a winner
        if self.checkWinner() == False:
            screen.draw.text("Red wins", (20, 115), color='red')
        elif self.checkWinner() == True:
            screen.draw.text("Yellow wins", (20, 115), color=(255,215,0))
        elif self.checkWinner() == 'draw':
            screen.draw.text("Draw", (20, 115), color='black')
        elif self.getActivePlayer():
            screen.draw.text("Yellows Turn", (20, 115), color='black')
        else:
            screen.draw.text("Reds Turn", (20, 115), color='black')


    def clicked(self,pos):
    # as long as there is no winner add a stone to a column by clicking on the field in the first row
        if self.checkWinner() != False and self.checkWinner() != True:
            if self._activePlayer == False:
                player = Player.HumanPlayer(True)
                clickval = player.play(self, pos)
                if clickval != None:
                    self.setStone(clickval)
            else:
                player = Player.KIPlayer(False)
                clickval = player.play(self, pos)
                self.setStone(clickval)

        if self.__restart.collidepoint(pos):
            self.__init__()

        if self.__undo.collidepoint(pos):
            self._undo()
  


a = GUI()

def draw():
    a.draw()

def on_mouse_down(pos):    
    a.clicked(pos)

pgzrun.go()