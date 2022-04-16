"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import turn_right, put

def main():
    for i in range(3):
        go_in()
        put(3)
        go_out()


def go_in():
    """
    pre: Karel facing East, and standing on the mountain.
    post: Karel in the hole, and facing South.
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre: Karel in the hole, and facing South.
    Post: Karel facing East, and standing on the mountain.
    """
    turn_back()
    move()
    turn_right()
    move()


def turn_back():
    turn_left()
    turn_left()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
