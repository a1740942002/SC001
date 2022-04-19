"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO: Karel need to go out of the box and pick the beeper, then go back to the inital position.
    Pre-condition: Karel is at [3, 4] and the beeper is at [6, 3].
    Post-condition: Karel is at [ 3,4 ] and the beeper is gone.
    """
    go_out()
    pick_beeper()
    go_back()


def go_out():
    """
    This function will make karel go out of the box.
    """
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()


def go_back():
    """
    This function will make karel go back to its original position from the beeper position.
    """
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()


def turn_right():
    """
    Karel will turn to its left 3 steps, which means it will end up turn to its original facing right.
    """
    for i in range(3):
        turn_left()

def turn_around():
    """
    Karel will turn to its left 2 steps, which means it will end up turn to its original facing back.
    """
    for i in range(2):
        turn_left()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
