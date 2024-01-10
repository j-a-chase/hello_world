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

# define constants
SECRET_NUM = randint(1, 100)

def guess_the_number() -> None:
    '''
    Makes user play a simple guessing number game to print 'Hello world!' to the console.

    Parameters: None

    Returns: None
    '''
    guess = 0
    print('Guess the number [1-100] --')
    while guess != SECRET_NUM:
        try:
            guess = int(input('> '))
        except ValueError:
            print('\tInvalid input format. Must be integer.')
            guess = 0
            continue

        if guess == SECRET_NUM:
            print_msg()
            break
        print('\tToo high!') if guess > SECRET_NUM else print('\tToo low!')

def print_msg() -> None:
    '''
    Prints 'Hello world!' to the console.

    Parameters: None

    Returns: None
    '''
    print()
    print('Hello world!')
    print()

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
