"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: Given a offset and a ciphered message, find the deciphered message.
    """
    offset = int(input('Secret number: '))
    ciphered_message = input("What's the ciphered string? ")
    deciphered_message = get_deciphered_message(ALPHABET, offset, ciphered_message)
    print('The deciphered string is: ' + deciphered_message)

def get_deciphered_message(correct_map, offset, ciphered_message):
    """
    :param correct_map: string, the correct sequence of map.
    :param offset: int, how many character should be wrapped around.
    :param ciphered_message: string, a ciphered message which is human unreadable.
    :return : string, a deciphered message which is human readable.
    """
    deciphered_message = ''
    length = len(correct_map)
    cipher_map = correct_map[length - offset:] + correct_map[:length - offset]

    for raw_char in ciphered_message:
        char = raw_char.upper()
        char_index = cipher_map.find(char)
        is_char_on_map = correct_map.find(char) >= 0

        if is_char_on_map:
            # If char is on the correct_map, add the new char.
            deciphered_message += correct_map[char_index]
        else:
            # If char is not on the map, keep it.
            deciphered_message += char
            
    return deciphered_message





#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
