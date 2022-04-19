"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    Karel should fill all pillars no matter how many pillars on the world.

    Pre-condition: Karel is at [1, 1] and facing East, with all pillar unfilled.
    Post-condition: Karel is at [x_axis_end, 1] and facing East, with all pillar filled.
    
    Reminder:
    * Each pillar is 5 column height and 3 column width.
    * Karel need to fill all the pillar by beeper (1).
    * Be careful of OBOB problem while using while loop.
    """
    while(front_is_clear()):
        check_and_fill_pillar()
        cross()

    # Because OBOB Problem
    check_and_fill_pillar()


def check_and_fill_pillar():
    """
    Pre-condition: Karel is facing East, with pillar unfilled.
    Post-condition: Karel is facing East, with pillar filled.

    Karel will reposition to fill the pillar depend on where it's facing, then reset it's facing to the East.
    """
    if(left_is_clear()):
        turn_left()
    else:
        if(right_is_clear()):
            turn_right()

    fill_pillar()

    if(facing_north()):
        turn_right()
    if(facing_south()):
        turn_left()


def fill_pillar():
    """
    When front is clear, Karel will keep checking beeper and moving forward one step.
    Because of OBOB problem, we need to manually check beeper at the last step.
    """
    while(front_is_clear()):
        check_beeper()
        move()
    
    # Because OBOB Problem
    check_beeper()


def check_beeper():
    """
    Karel will check whether it's on the beeper, if not, it will put a beeper.
    """
    if(not on_beeper()):
        put_beeper()        

def cross():
    """
    Karel will move forward 4 steps, used to cross between pillars.
    """
    for i in range(4):
        move()


def turn_right():
    """
    Karel will turn to its left 3 steps, which means it will end up turn to its original facing right.
    """
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
