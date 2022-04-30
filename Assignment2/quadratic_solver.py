"""
File: quadratic_solver.py
Name: Brian Lai
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
		TODO: Ask user to input 3 variables, and to display the root result.
		"""

    # Greeting
    print('stanCode Quadratic Solver!')

    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    discriminantResult = getDiscriminant(a, b, c)
    result = ''

    if discriminantResult > 0:
        answer1 = getRoot(a, b, c, '+')
        answer2 = getRoot(a, b, c, '-')
        result = 'Two roots: ' + str(answer1) + ', ' + str(answer2)
    elif discriminantResult == 0:
        answer = getRoot(a, b, c, '+')
        result = 'One root: ' + str(answer)
    else:
        result = 'No real roots'

    print(result)


def getDiscriminant(a, b, c):
    """
		Returns a discriminant result ( int ).

    :param a: int, x^2's variable.
    :param b: int, x^1's variable.
    :param c: int, x^0's variable.
    """
    return b * b - 4 * a * c


def getRoot(a, b, c, operator):
    """
		Returns a root result ( int ).

		:param a: int, x^2's variable.
		:param b: int, x^1's variable.
		:param c: int, x^0's variable.
		:param operator: str, should be '+' or '-'.
		"""
    result = -INFINITY
    if operator == '+':
        result = (-b + math.sqrt(getDiscriminant(a, b, c))) / 2 * a
    elif operator == '-':
        result = (-b - math.sqrt(getDiscriminant(a, b, c))) / 2 * a
    return result


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
