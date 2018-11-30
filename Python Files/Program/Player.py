from abc import ABC, abstractmethod
from random import shuffle
from Field import Field

import math
import copy

class Player(ABC):
	def __init__ (self, playerValue):
		pass

	@abstractmethod
	def play(self, field):
		pass

class HumanPlayer(Player):
	def __init__(self, playerValue):
		self.__playerValue = playerValue
	
	def play(self, field, pos):
		for x in range(0, 7):
			if pos[1] > 180 and pos[1] < 245:
				if pos[0] > 30 + x*70 and pos[0] < 90 + x*70:
					return x
		return None

class RandomPlayer(Player):
	def __init__(self, playerValue):
		self.__playerValue = playerValue

	def play(self, field, pos):
		possibleMoves = field.possibleMoves()
		shuffle(possibleMoves)

		return possibleMoves[0]

class KIPlayer(Player):
	def __init__(self, playerValue):
		self.__playerValue = playerValue

	def play(self, field, pos):
		maxVal = -math.inf
		maxIndex = 0
		possibleMoves = field.possibleMoves()
		shuffle(possibleMoves)

		for i in possibleMoves:
			f = copy.deepcopy(field)
			f.setStone(i)
			evaluation = self.__alphabeta(f, 5, -math.inf, math.inf, False)
			if maxVal < evaluation:
				maxVal = evaluation
				maxIndex = i

		return maxIndex

	def __alphabeta(self, field, depth, alpha, beta, maximizingPlayer):
		fieldValue = self.__evaluateField(field, depth)
		if abs(fieldValue) >= 512:
			return fieldValue
		if depth == 0 or fieldValue != 0:
			return fieldValue

		if maximizingPlayer:
			val = -math.inf
			for i in field.possibleMoves():
				f = copy.deepcopy(field)
				f.setStone(i)
				val = max(val, self.__alphabeta(f, depth-1, alpha, beta, False))
				alpha = max(alpha, val)
				if alpha >= beta:
					break
			return val
		else:
			val = math.inf
			for i in field.possibleMoves():
				f = copy.deepcopy(field)
				f.setStone(i)
				val = min(val, self.__alphabeta(f, depth-1, alpha, beta, True))
				beta = min(beta, val)
				if alpha >= beta:
					break
			return val

	def __evaluateField(self, field, depth):
		# Needs to improved ALOT
		winVal = field.checkWinner()
		looseVal = not winVal

		if winVal == None or winVal == 'draw':
			return 0
		elif winVal == self.__playerValue:
			return (512 * (depth +1))
		elif looseVal == self.__playerValue:
			return (-512 * (depth +1))
		return 0
