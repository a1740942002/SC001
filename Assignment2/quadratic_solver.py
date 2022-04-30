"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

from json.encoder import INFINITY
import math


def main():
	"""
	TODO:
	"""
	greeting()

	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminantResult = getDiscriminant(a, b, c)
	result = ''

	if discriminantResult > 0:
		answer1 = getRoot(a,b,c, '+')
		answer2 = getRoot(a,b,c, '-')
		result = 'Two roots: ' + answer1  + ', ' + answer2
	elif discriminantResult == 0:
		answer = getRoot(a,b,c, '+')
		result = 'One root: ' + answer
	else:
		result = 'No real roots'

	print(result)


def greeting():
	print('stanCode Quadratic Solver!')


def getDiscriminant(a, b, c):
	return b^2 - 4 * a * c


def getRoot(a, b, c, operator):
	result = -INFINITY
	if operator == '+':
		result = (-b + math.sqrt(getDiscriminant(a, b, c))) / 2 * a
	elif operator == '-':
		result = (-b - math.sqrt(getDiscriminant(a, b, c))) / 2 * a
	return result

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
