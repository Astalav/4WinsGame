import pgzrun
import math

from abc import ABC, abstractmethod
from Field import Field
import Player

class GUI(): 
    def __init__ (self): 
        self.__restart = Actor('restart', (540, 165))
        self.__undo = Actor('back', (575, 165))
        self.__playground = Field()
        self.__PLAYER1_VALUE = True #red
        self.__PLAYER2_VALUE = False #yellow
        self.player1 = Player.HumanPlayer(self.__PLAYER1_VALUE)
        # self.player2 = Player.HumanPlayer(self.__PLAYER2_VALUE)
        # self.player1 = Player.KIPlayer(self.__PLAYER1_VALUE)
        self.player2 = Player.KIPlayer(self.__PLAYER2_VALUE)
        
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
        for x in self.__playground._yellow:
            self.__drawYellow(x)

        for x in self.__playground._red:
            self.__drawRed(x)

        self.__restart.draw()
        self.__undo.draw()

        # give message if there is a winner
        if self.__playground.checkWinner() == False:
            screen.draw.text("Red wins", (20, 115), color='red')
        elif self.__playground.checkWinner() == True:
            screen.draw.text("Yellow wins", (20, 115), color=(255,215,0))
        elif self.__playground.checkWinner() == 'draw':
            screen.draw.text("Draw", (20, 115), color='black')
        elif self.__playground.getActivePlayer():
            screen.draw.text("Yellows Turn", (20, 115), color='black')
        else:
            screen.draw.text("Reds Turn", (20, 115), color='black')


    def clicked(self,pos):
    # as long as there is no winner add a stone to a column by clicking on the field in the first row
        if self.__playground.checkWinner() != False and self.__playground.checkWinner() != True:
            if self.__playground._activePlayer == self.__PLAYER1_VALUE:
                clickval = self.player1.play(self.__playground, pos)
                if clickval != None:
                    self.__playground.setStone(clickval)
            else:
                clickval = self.player2.play(self.__playground, pos)
                if clickval != None:
                    self.__playground.setStone(clickval)

        if self.__restart.collidepoint(pos):
            self.__playground = Field()

        if self.__undo.collidepoint(pos):
            self.__playground.undo()
  


a = GUI()

def draw():
    a.draw()

def on_mouse_down(pos):    
    a.clicked(pos)

pgzrun.go()