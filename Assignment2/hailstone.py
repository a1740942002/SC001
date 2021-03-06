"""
File: hailstone.py
Name: Brian Lai
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO: Print a Hailstore Sequence process and result.
    """
    n = int(input('Enter a number: '))
    step_count = 0

    while n != 1:
        if is_odd(n):
            new_n = get_odd_result(n)
            print(str(n) + ' is odd, so I make 3n+1: ' + str(new_n))
            n = new_n
        else:
            new_n = get_even_result(n)
            print(str(n) + ' is even, so I take half: ' + str(new_n))
            n = new_n
        step_count += 1
    print('It took ' + str(step_count) + ' steps to reach 1')


def is_odd(n):
    """
    Returns a Boolean result tell us whether this number is odd or not.

    :param n: int, a int number.
    """
    return n % 2 != 0


def get_odd_result(n):
    """
    Returns a Int result, do some calculate on the original input number.

    :param n: int, a int number.
    """
    return int(3*n + 1)


def get_even_result(n):
    """
    Returns a Int result, half the original input number.

    :param n: int, a int number.
    """
    return int(n / 2)

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
