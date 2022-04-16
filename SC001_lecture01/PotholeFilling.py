"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def main():
    for i in range(3):
        go_in()
        put(3)
        go_out()


def go_in():
    move()
    turn_right()
    move()


def go_out():
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
