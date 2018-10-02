# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/.."))
from Program import FourWinsGame
from Program import Field
import pytest
import random

def testStart():
	empty_field = [None] * 42
	a = Field.Field()
	assert a.getActivePlayer() == False
	assert a.getField() == empty_field

def testCheckWinner():
	# generate Fields
	a = Field.Field()
	horizontal = [[0, 1, 2, 3], [15, 16, 17, 18], [30, 31, 32, 33]]
	vertically = [[0, 7, 14, 21], [17, 24, 31, 38], [20, 27, 34, 41]]
	diagonal = [[35, 29, 23, 17], [40, 32, 24, 16], [31, 25, 19, 13], [31, 23, 15, 7]]

	for i in horizontal:
		field = [None] * 42
		for y in i:
			field[y] = 1 
		current = i[random.randint(0, 3)]
		assert a.checkWinner(current, field) == 1
	
	for i in vertically:
		field = [None] * 42
		for y in i:
			field[y] = 1 
		current = i[random.randint(0, 3)]
		assert a.checkWinner(current, field) == 1

	for i in diagonal:
		field = [None] * 42
		for y in i:
			field[y] = 1 
		current = i[random.randint(0, 3)]
		assert a.checkWinner(current, field) == 1

def testchangePlayer():
	a = Field.Field()
	player = a.getActivePlayer()
	a.changePlayer()
	assert a.getActivePlayer() != player

def testsetStone():
	a = Field.Field()
	a.setStone(0)
	assert a.getField()[35] == False
	a.setStone(0)
	assert a.getField()[28] == True
