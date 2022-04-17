"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """

    #### while loop version
    # while is_not_end():
    #     check_front_and_move()
    #     if is_face_obstacle():
    #         jump()


    # for loop version
    for i in range(11):
        if not front_is_clear():
            jump()
        else:
            move()


def is_not_end():
    # Warning!
    # Don't use it, until Karel provide API
    return True

def check_front_and_move():
    if front_is_clear():
        move()

def is_face_obstacle():
    return not front_is_clear()

def jump():
    """
    Pre-condition: Karel is at left side of the wall, facing East
    Post-condition: Karel is at the right side of the wall, facing East
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition: Karel is at the bottom of the wall, facing East
    Post-condition: Karel is at the top of the wall, facing East
    """
    turn_left()
    while not right_is_clear():
        move()
    turn_right()


def cross():
    """
    Pre-condition: Karel is at the top of the wall, facing East
    Post-condition: Karel step one forward crossing the obstacle, facing East
    """
    move()


def down():
    """
    Pre-condition: Karel step one forward crossing the obstacle, facing East
    Post-condition: Karel is back to the bottom of world, facing East
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
