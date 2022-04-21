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
    Karel need to put beepers on the world, and each beeper should have 1 space next to others.
    So Karel just have to put beeper every two step, then could fit its need.
    Because Karel will eventually mpve and put beeper from South to North, so Karel when meet the edge, it must be facing North.

    pre-condition: Karel will start at [1, 1], facing East.
    post-condition: Karel will end at last line of the world, facing North.
    """
    put_beeper()
    while not facing_north():
        put_beeper_by_two_steps()

def put_beeper_by_two_steps():
    """
    Because Our algorithm is "Karel should put beeper every two step", so we just need to focus on how to move 2 step without hitting the wall.

    When hit the edge, safe_step will make Karel face North, so Karel should not put beeper when it's facing North.
    """
    for i in range(2):
        safe_step()
    if not facing_north():
        put_beeper()


def safe_step():
    """
    In normal situation, Karel will move 1 step, and if it hit the wall he will automatically turn to left or right ( depend on where it's facing, if it's facing East, it will turn left; if it's facing West, it will turn right, because it eventually want to move toward North ).

    But if Karel hit the edge, it will face North and stand still without move any step.

    pre-condition: Karel should face East or West, no matter where it is.
    post-condition:
        1. Karel might face West or East, and 1 step away from it's start posiiton.
        2. Karel face North, and stand still from it's start position.
    """
    if front_is_clear():
        move()
    else:
        # Because front is not clear, so let's turn!
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
