"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    put_beeper()
    while not facing_north():
        put_beeper_by_two_steps()

def put_beeper_by_two_steps():
    for i in range(2):
        if front_is_clear():
            move()
        else:
            if facing_east():
                turn_left()
                if front_is_clear():
                    move()
                    turn_left()
            else:
                if facing_west():
                    turn_right()
                    if front_is_clear():
                        move()      
                        turn_right()
    if not facing_north():
        put_beeper()


def turn_right():
    """
    Karel will turn to its left 3 steps, which means it will end up turn to its original facing right.
    """
    for i in range(3):
        turn_left()


# def safe_move():
#     """
#     Karel will check if front is clear everytime, then decide to move or not.
#     This function can always prevent Karel run into wall.
#     """
#     if(front_is_clear()):
#         move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
