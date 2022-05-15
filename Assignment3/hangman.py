"""
File: hangman.py
Name: Brian
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7

def main():
    """
    TODO: A Hangman or Wordle game which user can input a character to guess correct word in limited chances.
    """

    # Init Data
    left_life = N_TURNS
    answer = random_word()
    left_answer = answer
    guess = get_init_guess(len(answer))
    raw_guess_char = ''
    is_valid_input = False

    while True:
        # Lose Condition
        if left_life <= 0:
            print('You are completely hung : (')
            break

        # Win Condition
        elif guess == answer:
            print('You win!!')
            break
            
        # Normal Condition
        else:
            print('The word looks like ' + guess)
            print('You have ' + str(left_life) + ' wrong guesses left.')
            raw_guess_char = input('Your guess: ')
            is_valid_input = len(raw_guess_char) == 1 and raw_guess_char.isalpha()

            # If is not valid input, throw Error
            while not is_valid_input:
                print("Illegal format.")
                raw_guess_char = input('Your guess: ')
                is_valid_input = len(raw_guess_char) == 1 and raw_guess_char.isalpha()

            guess_char = raw_guess_char.upper()
            is_guess_correct = answer.find(guess_char) >= 0

            if is_guess_correct:
                print('You are correct!')
                guess = get_updated_guess(guess, answer, guess_char)
                left_answer = get_updated_left_answer(left_answer, guess_char)
            else:
                print("There is no " + guess_char + "'s in the word.")
                left_life -= 1

    print('The word was: ' + answer)


def get_updated_left_answer(left_answer, guess_char):
    """
    :param left_anser: string, initial left answer.
    :param guess_char: string, user's guess character in this round.
    :return : string, consist of left chars in answer which user haven't guessed.
    """
    updated_left_answer = ''
    for i in range(len(left_answer)):
        if left_answer[i] != guess_char:
            updated_left_answer += left_answer[i]

    return updated_left_answer


def get_updated_guess(guess, answer, guess_char):
    """
    :param guess: string, initial guess string.
    :param answer: string, this round's correct answer.
    :param guess_char: string, user's guess character in this round.
    :return : string, consist of left chars in answer which user have guessed.
    """
    updated_guess = ''
    for i in range(len(guess)):
        if answer[i] == guess_char:
            updated_guess += guess_char
        else:
            updated_guess += guess[i]

    return updated_guess


def get_init_guess(number):
    """
    :param number: int, how many dash will be created.
    :return : a string consist of '-' which length is equal to input number.
    """
    guess = ''
    for i in range(number):
        guess += '-'
    return guess


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
