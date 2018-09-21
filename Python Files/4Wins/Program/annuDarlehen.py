# -*- coding: utf8 -*-

from decimal import *
import locale
import math


def run():
	welcomeMessage(20)

	locale.setlocale(locale.LC_ALL, '')

	while True:
		while True:
			creditSum = getUserDecimalInput("Please enter your credit sum: ", minValue=0)
			if not math.isnan(creditSum):
				break

		while True:
			interest = getUserDecimalInput("Please enter your interest in %: ", minValue=0, maxValue=10, maxAsWarning=True)
			if not math.isnan(interest):
				interest = interest/Decimal(100)
				break
				
		while True:
			time = getUserDecimalInput("Please enter the time your credit runs in years: ", minValue=0, maxValue=50, maxAsWarning=True)
			if not math.isnan(time):
				break

		print(locale.currency(calcAnnuDarlehen(creditSum, interest, time), grouping=True))

		if input("Möchten sie eine weitere Rechnung starten?(Y/N): ") != "Y":
			break
	
	print("Goodbye")


def calcAnnuDarlehen(creditSum, interest, time):
	annu = creditSum * ((((1+interest)**time)*interest) / (((1+interest)**time)-1))
	return annu

def getUserDecimalInput(inputString, minValue=Decimal("-Infinity"), minAsWarning=False, maxValue=Decimal("Infinity"), maxAsWarning=False):
	userInputDecimal = input(inputString)
	try:
		userInputDecimal = Decimal(userInputDecimal)       
	except InvalidOperation:
		print("Error: Your input was not a number! Please enter a number next time!")
		return Decimal("NaN")

	if userInputDecimal < minValue:
		if minAsWarning:
			print("Warning: Your input was smaller than or equal to %s!"% minValue)
		else:
			print("Error: Your input was smaller than or equal to %s! Please enter a valid number next time!"% minValue)
			return Decimal("NaN")

	if userInputDecimal > maxValue:
		if maxAsWarning:
			print("Warning: Your input was greater than or equal to %s!"% str(maxValue))
		else:
			print("Error: Your input was greater than or equal to %s! Please enter a valid number next time!"% maxValue)
			return Decimal(NaN)

	return userInputDecimal


def welcomeMessage(size):
	startEndStars = 2 * "* "
	
	if size < 16:
		size = 16

	line1n7 = startEndStars + size * "* " + startEndStars
	line2n6 = startEndStars + size * "  " + startEndStars

	line3   = startEndStars + ("{:^" + str(size*2) + "}").format("Welcome to this Calculator      ") + startEndStars
	line4   = startEndStars + ("{:^" + str(size*2) + "}").format("Version: 0.1 vom 23.11.2017     ") + startEndStars
	line5   = startEndStars + ("{:^" + str(size*2) + "}").format("Fehler bitte an david@tbs1.de   ") + startEndStars

	print(line1n7)
	print(line2n6)
	print(line3)
	print(line4)
	print(line5)
	print(line2n6)
	print(line1n7)