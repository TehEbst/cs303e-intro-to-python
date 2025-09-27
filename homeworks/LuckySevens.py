# Assignment: HW5
# File: LuckySevens.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-09-26
# Description of Program: This program is a simulation of the Lucky Sevens
#   dice game. The user begins with a chosen stake, then the program
#   repeatedly rolls two dice. If the sum is 7, the stake is increased by $4.
#   Otherwise, the stake is decreased by $1. The game keeps track of the number
#   of rolls and the max stake reached. The user can also choose to play
#   multiple rounds

#   Assignment Link:
#   https://www.cs.utexas.edu/~byoung/cs303e/hw5.html

# Import randint from random
from random import randint

# Variable that controls whether the game is running or not
gameRunning = True

# Variables to store number of dice rolls and maximum stake
numDiceRolls = 0
maxStake = 0

# Loop that determines whether game is running or not
while gameRunning:

    # Loop to handle stake input validation
    while True:

        # User specifies money (the stake)
        stake = input('How many dollars would you like to gamble? ')

        # Validate the input
        if not stake.isdigit():
            print('Answer must be a positive integer '
                  '(dollars to gamble). Try again!')
        else:
            # Game starting message
            print(f'You\'ve said you\'re going to gamble ${stake}. Good luck!')

            # Convert stake to int
            stake = int(stake)

            # This is the actual game loop
            # Repeatedly roll two dice until stake < 0.
            # I also put a number to limit max iterations juuuuuust in case
            while stake > 0 or numDiceRolls == 100000:

                # Each roll between [1,6]
                diceOne = randint(1,6)
                diceTwo = randint(1, 6)
                currSum = diceOne + diceTwo
                numDiceRolls += 1

                # Display the value and the sum
                print(f'{numDiceRolls}: rolled ({diceOne}, {diceTwo}), '
                      f'sum = {currSum}')

                # If the sum is 7, which is the win condition
                if currSum == 7:
                    # Increase stake by $4
                    stake += 4
                    print(f'Congratulations, you win $4! '
                          f'Your stake is ${stake}')
                    if stake > maxStake:
                        maxStake = stake
                else:
                    # Decrease stake by $1
                    stake -= 1
                    print(f'Sorry, you lost $1. Better luck next time! '
                          f'Your stake is ${stake}')

            break

    print()
    # Report how many dice rolls to deplete the stake
    print(f'You\'re out of money after {numDiceRolls} rolls.')

    # Report what the maximum stake is
    print(f'Your highest stake was: ${maxStake}')
    print()

    # Check if user wants to play again
    playAgain = input('Would you like to play again (yes or no)? ')

    # If user does not want to play again, end the loop,
    #   otherwise, do nothing
    if playAgain == 'no':
        gameRunning = False
        print('Thanks for playing!')
    # I am extra and included a catch-all in case of a bad input
    elif not playAgain == 'yes':
        gameRunning = False
        print('Invalid answer, game ending. Thanks for playing!')