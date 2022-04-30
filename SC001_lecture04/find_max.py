"""
File: find_max.py
Name:
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 4
in Assignment 2
"""

# This constant controls when to stop
EXIT = -1 # Sentinel Value / 哨兵不能玩


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print('This program finds the max, input -1 to exit.')

    # Init
    data = int(input('Data: '))
    max = data

    while True:
        # Early Return
        if data == EXIT:
            print('Exit!')
            break

        # Ask Data
        data = int(input('Data: '))

        # Compare
        if(data > max):
            max = data

    # Result
    if(max != EXIT):
        print('max: ' + str(max))



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
