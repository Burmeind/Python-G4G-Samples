# Number guessing game in Python 3

import random

max_number = 1000
min_number = 0
max_guesses = 10

while True:

    print('Welcome to the Number Game!\nType Exit to quit the game.\nType Settings to change the settings.\nType Start to begin a game.\n' )

    entry = input()

    if entry.upper() == 'Settings'.upper():

        try:
            max_number = int(input('Set the maximum number:\t'))
            min_number = int(input('Set the minimum number:\t'))
            max_guesses = int(input('Set the maximum number of guesses:\t'))
        except ValueError:
            print(f'Please enter numbers only!')

    elif entry.upper() == 'Exit'.upper():
        print('Buh-bye!')
        break

    elif entry.upper() == 'Start'.upper():
        remaining_guesses = max_guesses
        number = random.randint(min_number, max_number)
        while remaining_guesses:
            while True:
                print(f'You have {remaining_guesses} guesses remaining.\nEnter a number between {min_number} and {max_number}.')
                guess = input()

                try:
                    guess = int(guess)
                    if guess < min_number or guess > max_number:
                        raise ValueError
                except ValueError:
                    print(f'Please enter a number between {min_number} and {max_number}.\n')
                else:
                    break

            remaining_guesses -= 1

            if guess == number:
                print(f'You win with {remaining_guesses} guesses remaining!')
                break

            elif guess > number:
                max_number = guess - 1

            elif guess < number:
                min_number = guess + 1

        max_number = 1000
        min_number = 0
        max_guesses = 10

        if not remaining_guesses:
            print('You lose!')

    else:
        print('Please enter a valid value!')
        
