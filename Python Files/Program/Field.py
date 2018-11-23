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
        elif not self.getActivePlayer() and len(self._yellow) > 0:
            last = self._yellow[len(self._yellow)-1]
            self._playground[last] = None
            self._yellow.pop()
            self.__changePlayer()            

    def setStone(self, column):
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

    def possibleMoves(self):
        retVal = []

        for i in range(0, 7):
            if(self._playground[i] == None):
                retVal.append(i)

        return retVal

    def checkDraw(self):
        if self._playground.count(None) == 0:
            return True
        return False

    def checkWinner(self):
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
                    elif i != 1 and math.floor((last+(i*x))/7) == math.floor(last / 7) + x:
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
                    elif i != 1 and math.floor((last-(i*x))/7) == math.floor(last/7) - x:
                        win = win + 1
                    else:
                        break
                else:
                    break
                if win == 4:
                    return currentPlayground[last]
        
        if self._playground.count(None) == 0:
            return 'draw'