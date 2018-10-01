from abc import ABC, abstractmethod


class Field(ABC):                      
    def __init__ (self):                
    #sets all values to false for initilization
        self.__activePlayer = False
        self.__field = [None] * 42

    def getField(self):
        return self.__field

    def getActivePlayer(self):
        return self.__activePlayer

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

