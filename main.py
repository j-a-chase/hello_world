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

def guess_the_number(r_max: int = 100) -> None:
    '''
    Makes user play a simple guessing number game to print 'Hello world!' to the console.

    Parameters:
        - r_max: an integer representing the max range for secret number generation

    Returns: None
    '''
    # print message if user has shrunk range down to 1-1
    if r_max == 1:
        print_msg()
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
