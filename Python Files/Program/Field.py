from abc import ABC, abstractmethod
import pgzrun
import math

class Field(ABC):                      
    def __init__ (self):                
    #sets all values for initilization
        self._activePlayer = False
        self._playground = [None] * 42
        self._yellow = []
        self._red = []

    def getPlayground(self):
    # returns current Playground
        return self._playground

    def getActivePlayer(self):
    # returns current Player
        return self._activePlayer

    def __changePlayer(self):
    # changes current Player
        self._activePlayer = not self._activePlayer

    def _undo(self):
        if self.getActivePlayer() and len(self._red) > 0:
            last = self._red[len(self._red)-1]
            self._playground[last] = None
            self._red.pop()
            self.__changePlayer()
        elif len(self._yellow) > 0:
            last = self._yellow[len(self._yellow)-1]
            self._playground[last] = None
            self._yellow.pop()
            self.__changePlayer()            

    def _setStone(self, column):
    # Sets Stone by given column: 
    # Stone falls until he hits the ground or another Stone
    # If a field is filled the field above is filled with current Players Stone

        for x in range(1, 6):
            field = column + x*7

            if self._playground[field] != None and self._playground[column] == None:
                self._playground[field - 7] = self.getActivePlayer()
                if self.getActivePlayer():
                    self._yellow.append(field-7)
                else:
                    self._red.append(field-7)
                self.__changePlayer()
                break

            elif x == 5 and self._playground[column] == None:
                self._playground[field] = self.getActivePlayer()
                if self.getActivePlayer():
                    self._yellow.append(field)
                else:
                    self._red.append(field)
                self.__changePlayer()
                break

    def _checkWinner(self):
    # Checks if there is an row of four equal Stones according to the last set Stone
    # returns Winner if there is one

        # steps descripes the difference between two Fields to be in one line: 
        # horizontal: 1 vertically: 7 diagonal_up: 6 diagonal_down: 8
        steps = [1, 7, 6, 8]

        # get last added stone and current playground
        if len(self._red) == 0 and len(self._yellow) == 0:
            return
        elif self.getActivePlayer():
            last = self._red[len(self._red) -1]
        else:
            last = self._yellow[len(self._yellow) -1]
        currentPlayground = self._playground

        for i in steps:
            win = 1
            for x in range (1, 5):
                if last + (i*x) < 42 and currentPlayground[last + (i*x)] == currentPlayground[last]:
                    # check if all fields in one row (horizontal)
                    if i == 1 and math.floor((last+(i*x))/7) == math.floor(last/7):
                        win = win + 1
                    # check if all fields in successive rows
                    elif math.floor((last+(i*x))/7) == math.floor(last / 7) + x:
                        win = win + 1
                    else:
                        break
                else:
                    break
                if win == 4:
                    return currentPlayground[last]
            
            for x in range (1, 5):
                if last - (i*x) > -1 and currentPlayground[last - (i*x)] == currentPlayground[last]:
                    if i == 1 and math.floor((last-(i*x))/7) == math.floor(last/7):
                        win = win + 1
                    elif math.floor((last-(i*x))/7) == math.floor(last/7) - x:
                        win = win + 1
                    else:
                        break
                else:
                    break
                if win == 4:
                    return currentPlayground[last]
        

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
        if self._checkWinner() == False:
            screen.draw.text("Red wins", (20, 115), color='red')
        elif self._checkWinner() == True:
            screen.draw.text("Yellow wins", (20, 115), color=(255,215,0))
        elif self.getActivePlayer():
            screen.draw.text("Yellows Turn", (20, 115), color='black')
        else:
            screen.draw.text("Reds Turn", (20, 115), color='black')


    def clicked(self,pos):
    # as long as there is no winner add a stone to a column by clicking on the field in the first row
        if self._checkWinner() != False and self._checkWinner() != True:
            for x in range(0, 7):
                if pos[1] > 180 and pos[1] < 245:
                    if pos[0] > 30 + x*70 and pos[0] < 90 + x*70:
                        self._setStone(x)

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