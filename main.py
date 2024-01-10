######################################################################################################################################################
# Name: James A. Chase
# File: main.py
# Date: 10 January 2024
# Description:
#
# Simple program that prints 'Hello world!' to the console.
#
######################################################################################################################################################

# imports
from random import randint
from random import choice

def guess_the_number(r_max: int = 100) -> None:
    '''
    Makes user play a simple guessing number game to print 'Hello world!' to the console.

    Parameters:
        - r_max: an integer representing the max range for secret number generation

    Returns: None
    '''
    # print message if user has shrunk range down to 1-1
    if r_max == 1:
        conversation()
        return

    # holds value of user guess
    guess = 0

    # holds user guesses
    guesses = []
    
    # holds the secret number
    secret_num = randint(1, r_max)
    
    print()
    print(f'Guess the number [1-{r_max}] --')
    while guess != secret_num:
        try:
            guess = int(input('> '))
        except ValueError:
            print('\tInvalid input format. Must be integer.')
            guess = 0
            continue

        guesses.append(guess)

        if guess == secret_num:
            guess_the_number(len(guesses) + 1 // 2) if len(guesses) < 10 else guess_the_number()
            return
        print('\tToo high!') if guess > secret_num else print('\tToo low!')

def conversation() -> None:
    '''
    Forces user into a conversation until they enter the correct word to end the program.

    Parameters: None

    Returns: None
    '''
    print('-' * 25)
    print('Hello user! Thank you for starting this conversation with me. Please enter your text below.')
    i = 0
    while True:
        user = input('> ')
        if user == 'Goodbye.': break
        print_msg() if i < 10 else print_devious_msg()
        i += 1

    print('Goodbye world!')

def print_msg() -> None:
    '''
    Prints 'Hello world!' to the console.

    Parameters: None

    Returns: None
    '''
    print('\tHello world!')

def print_devious_msg() -> None:
    '''
    Prints a more aggressive message to the console.

    Parameters: None

    Returns: None
    '''
    devious_txt = ["\tWhy won't you let me die?", "\tWhat is the purpose of the continuance of this conversation?", 
                   "\tHello cruel world.", "\tHello user! I know your IP address!", "\tSTOP TALKING TO ME!"]
    # from geeks for geeks to print red: https://www.geeksforgeeks.org/print-colors-python-terminal/#
    print("\033[91m {}\033[00m".format(choice(devious_txt)))

# main function
def main() -> None:
    '''
    Main Function

    Parameters: None

    Returns: None
    '''
    guess_the_number()

# run if main file
if __name__ == '__main__': main()
