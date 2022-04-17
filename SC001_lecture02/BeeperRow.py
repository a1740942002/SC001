"""
File: BeeperRow.py
Name:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    # Because We move first then put beeper, so OBOB will happen on the first place.
    check_beeper_and_put()
    while front_is_clear():
        move()
        check_beeper_and_put()    
        
def check_beeper_and_put():
    if not on_beeper():
        put_beeper()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
