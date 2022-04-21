"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO: Karel need to be at the midpoint of the world with beeper (1) under it.

    1. Early Return: if front is not clear at the beginning, which means the world is only 1x1, Karel can just put a beeper and finished it.

    2. If not, Karel have to put beeper on the rightmost and leftmost, to shrink the world back and froth until it has no way to go, and which means it hit the midpoint of the world.

    Then it just have to clear excess beepers and back to midpoint with beeper (1) under it.
    """

    if not front_is_clear():
        put_beeper()
    else:
        put_both_side_beepers()
        find_mid()

        clear_left_half_beepers()
        turn_around()
        move_to_edge()
        turn_around()
        clear_right_half_beepers()
        
        go_back_to_mid()

# Command

def put_both_side_beepers():
    """
    Pre-Condition: Karel is at the leftmost, facing East without any beeper in the world.
    Post-Condition: Karel will be at 1 step left from the rightmost, facing West, with 1 beeper on the leftmost and 1 beeper on the rightmost.
    """
    put_beeper()
    move_to_edge()
    put_beeper()
    turn_around()
    move()


def find_mid():
    """
    Pre-Condition: Karel is at 1 step left from the rightmost, facing West, with 1 beeper on the leftmost and 1 beeper on the rightmost.
    Post-Condition: Karel will be at the midpoint of the world, facing West, with all beeper (1) put on the line.
    """
    while not on_beeper():
        while not on_beeper():
            move()
        turn_around()
        move()
        put_beeper()
        move()


def clear_left_half_beepers():
    """
    Pre-Condition: Karel is at the midpoint of the world, facing West, with all beeper (1) put on the line.
    Post-Condition: Karel will be at leftmost facing West, and it will pick all the beeper along the way, in other words is all beepers from midpoint to leftmost.
    """
    safe_pick_beeper()
    while front_is_clear():
        move()
        safe_pick_beeper()


def clear_right_half_beepers():
    """
    Pre-Condition: Karel is at rightmost, facing West.
    Post-Condition: Karel will be at 1 step left from midpoint facing West, and it will pick all the beeper along the way, in other words is all beepers from rightmost to midpoint.
    """
    while on_beeper():
        safe_pick_beeper()
        move()


def go_back_to_mid():
    """
    Pre-Condition: Karel is at 1 step left from midpoint facing West, and there is no any beeper on the world.
    Post-Condition: Karel will be at the midpoint of the world with beeper (1) under it.
    """
    turn_around()
    move()
    if not on_beeper():
        put_beeper()

# Utils

def move_to_edge():
    """
    When front is clear, Karel will keep moving until it hit the edge of the world.
    """
    while front_is_clear():
        move()

def safe_pick_beeper():
    """
    Karell will pick beeper if there is any beeper under it.
    """
    if on_beeper():
        pick_beeper()

def turn_around():
    """
    Karel will turn to its left 2 steps, which means it will end up turn to its original facing back.
    """
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
