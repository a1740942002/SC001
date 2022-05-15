"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO: Depend on user's input and print the correct complement of DNA.
    """
    userInput = input("Please give me a DNA strand and I'll find the complement: ")
    result = build_complement(userInput)
    print('The complement of ' + userInput + ' is ' + result)


def build_complement(string):
    """
    :param string: string, Should only be consist of 'a', 'A', 't', 'T', 'c', 'C', 'g', 'G'.
    :return : string
    """
    complement_string = ''

    for rawChar in string:
        char = rawChar.upper()
        if char == 'A':
            complement_string += 'T'
        elif char == 'T':
            complement_string += 'A'
        elif char == 'G':
            complement_string += 'C'
        elif char == 'C':
            complement_string += 'G'
        else:
            pass

    return complement_string

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
