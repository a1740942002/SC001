"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double()
    move_beepers_back()


def move_beepers_back():
    pass

def double():
    while on_beeper():
        pick_beeper()
        put_two_beeper_next_door()


def put_two_beeper_next_door():
    move()
    put_beeper()
    put_beeper()
    move_back()


def move_back():
    turn_around()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
