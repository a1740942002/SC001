"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 10

def main():
    """
    TODO:
    """
    create_head(SIZE)
    create_belt(SIZE)
    create_upper(SIZE)
    create_lower(SIZE)
    create_belt(SIZE)
    create_head(SIZE)


def create_head(size):
    for i in range(size):
        row = i + 1
        inline_print(' ')
        create_head_by_direction(row, size,'left')
        create_head_by_direction(row, size,'right')
        inline_print(' ')
        print('')

def create_head_by_direction(row, size,direction):
    is_left = direction == 'left'
    is_right = direction == 'right'
    half_width = size - row

    if is_left:
        for i in range(half_width):
            inline_print(' ')

    for i in range(row):
        if is_left:
            inline_print('/')
        elif is_right:
            inline_print('\\')

    if is_right:
        for i in range(half_width):
            inline_print(' ')


def create_belt(size):
    inline_print('+')
    for i in range( 2 * size):
        inline_print('=')
    inline_print('+')
    print('')


def create_upper(size):
    for i in range(size):
        row = i + 1
        inline_print('|')
        create_upper_layer(row, size)
        inline_print('|')
        print('')


def create_lower(size):
    for i in range(size):
        row = i + 1
        inline_print('|')
        create_lower_layer(row, size)
        inline_print('|')
        print('')


def create_upper_layer(row, size):
    card_count = row
    dot_count = size * 2 - card_count * 2
    half_dot_count = int( dot_count / 2 )

    for i in range(half_dot_count):
        inline_print('.')

    for i in range(card_count):
        inline_print('/\\')

    for i in range(half_dot_count):
        inline_print('.')


def create_lower_layer(row, size):
    card_count = size - row + 1
    dot_count = size * 2 - card_count * 2
    half_dot_count = int( dot_count / 2 )

    for i in range(half_dot_count):
        inline_print('.')

    for i in range(card_count):
        inline_print('\\/')

    for i in range(half_dot_count):
        inline_print('.')


def inline_print(str):
    print(str, end='')

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
    main()
