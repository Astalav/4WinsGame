from abc import ABC, abstractmethod
import pgzrun
import math

class Field(ABC):                      
    def __init__ (self):                
    #sets all values to false for initilization
        self.__activePlayer = False
        self.__field = [None] * 42
        self.__yellow = []
        self.__red = []

    def getField(self):
        return self.__field

    def getActivePlayer(self):
        return self.__activePlayer

    def draw(self):
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
        for x in self.__yellow:
            self.drawYellow(x)

        for x in self.__red:
            self.drawRed(x)

    def drawRed(self, field):
        y = 6 - math.ceil((field +1) / 7)
        x = field - math.floor((field) / 7)*7
        screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 0, 0))

    def drawYellow(self, field):
        y = 6 - math.ceil((field +1) / 7)
        x = field - math.floor((field) / 7)*7
        screen.draw.filled_circle((60 + x * 70, 565 - 70 * y), 30, (255, 255, 0))

    def changePlayer(self):
        self.__activePlayer = not self.__activePlayer

    def setStone(self, column):
        for x in range(0, 6):
            field = column + x*7
            if self.__field[field] != None:
                self.__field[field-7] = self.getActivePlayer()
                if self.getActivePlayer():
                    self.__yellow.append(field)
                else
                    self.__red.append(field)
                self.changePlayer()
                return field
            elif self.__field[field] == None and x == 5:
                self.__field[field] = self.getActivePlayer()
                if self.getActivePlayer():
                    self.__yellow.append(field)
                else
                    self.__red.append(field)
                self.changePlayer()
                return field

    def checkWinner(self, last, currentField):
        steps = [1, 7, 6, 8]

        for i in steps:
            win = 1
            for x in range (1, 5):
                if last + (i*x) < 42 and currentField[last + (i*x)] == currentField[last]:
                    win = win + 1
                else:
                    break
              
                if win == 4:
                    return currentField[last]
            
            for x in range (1, 5):
                if last + (i*x) > -1 and currentField[last - (i*x)] == currentField[last]:
                    win = win + 1
                else:
                    break
            
                if win == 4:
                    return currentField[last]
        
        return 'fail'

a = Field()

def draw():
    a.draw()

pgzrun.go()