# Assignment: RockPaperScissors
# File: RockPaperScissors.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-10-10
# Description of Program: Its the game of rock paper scissors.

import random
import sys

# Global variable that indexes into the 'oracle' to select the next machine play
machinePlayCounter = 0

# Constants for rock, paper, and scissors
ROCK = "1"
PAPER = "2"
SCISSORS = "3"

# Global stats
GAMESPLAYED = 0
GAMESWON = 0
GAMESLOST = 0
GAMESTIED = 0


def machinePlay():
    """The machine chooses one of the three moves randomly,
    unless there's an oracle passed on the command line."""
    global machinePlayCounter
    hasOracle = (len(sys.argv) > 1)
    if hasOracle:
        machineOracle = sys.argv[1]
    if hasOracle and machinePlayCounter < len(machineOracle):
        play = machineOracle[machinePlayCounter]
        machinePlayCounter += 1
    else:
        play = random.choice([ROCK, PAPER, SCISSORS])
    return play


def inputValidation(userInput):
    """Ensure user enters 1-4 as per the game parameters."""
    return userInput in ['1', '2', '3', '4']


def defeats(play1, play2):
    """Return outcome message ('win', 'lose', 'tie')."""
    if play1 == play2:
        return "tie"
    elif (play1 == ROCK and play2 == SCISSORS) or \
            (play1 == PAPER and play2 == ROCK) or \
            (play1 == SCISSORS and play2 == PAPER):
        return "win"
    else:
        return "lose"


def playName(play):
    """Return the name to print for each possible move."""
    if play == ROCK:
        return "rock"
    elif play == PAPER:
        return "paper"
    elif play == SCISSORS:
        return "scissors"


def gameFunction(userInput):
    """Handle a single round of the game."""
    global GAMESPLAYED, GAMESWON, GAMESLOST, GAMESTIED

    opponentMove = machinePlay()
    print(f"You played {playName(userInput)}; your opponent played {playName(opponentMove)}")

    result = defeats(userInput, opponentMove)
    GAMESPLAYED += 1

    if result == "win":
        print("Congratulations, you won!\n")
        GAMESWON += 1
    elif result == "lose":
        print("Sorry, you lost!\n")
        GAMESLOST += 1
    else:
        print("There's no winner. Try again!\n")
        GAMESTIED += 1


# Loop as long as the game is running
while True:
    print('Choose your play:')
    print('  Enter 1 for rock;')
    print('  Enter 2 for paper;')
    print('  Enter 3 for scissors;')
    userInput = input('  Enter 4 to exit: ')

    # Validate input
    if inputValidation(userInput):
        if userInput == '4':
            # Display statistics upon exit
            if GAMESPLAYED == 0:
                print('No games were completed.')
            else:
                print(f"\nGame statistics:")
                print(f'  Games played: {GAMESPLAYED:>1}')

                # "You won" statistics with percentage
                print(f'  You won:     {GAMESWON:>2}', end='')
                if GAMESPLAYED > 0:
                    print(f' ({(GAMESWON / GAMESPLAYED) * 100:.1f}%)')
                else:
                    print(f' (0.0%)')

                # "You lost" statistics with percentage
                print(f'  You lost:    {GAMESLOST:>2}', end='')
                if GAMESPLAYED > 0:
                    print(f' ({(GAMESLOST / GAMESPLAYED) * 100:.1f}%)')
                else:
                    print(f' (0.0%)')

                # "No winner" statistics with percentage
                print(f'  No winner:   {GAMESTIED:>2}', end='')
                if GAMESPLAYED > 0:
                    print(f' ({(GAMESTIED / GAMESPLAYED) * 100:.1f}%)')
                else:
                    print(f' (0.0%)')

            print(f'Thanks for playing. Goodbye!')
            break
        else:
            gameFunction(userInput)
    else:
        print('Illegal play entered. Try again!\n')