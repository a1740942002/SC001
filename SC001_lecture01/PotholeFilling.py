"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import turn_right, put_beeper_by_number, turn_back

def main():
    for i in range(3):
        go_in()
        put_beeper_by_number(99)
        go_out()


def go_in():
    """
    pre-condition: Karel is facing East, and standing on the mountain.
    post-condition: Karel is in the hole, and facing South.
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition: Karel is in the hole, and facing South.
    post-condition: Karel is facing East, and standing on the mountain.
    """
    turn_back()
    move()
    turn_right()
    move()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
