# Assignment: Project 2
# File: PrimeFactory.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date Created: 2025-11-06
# Date Last Modified:
# Description of Program:

import math
import time

_PRIMES = []
_MAX_COMPUTED = 0

# Function 0 - Exit
def exitFunc():
    print('Thanks for visiting our factory! Goodbye.')
    return True

# Function 1 - Is input N a prime number?
def isPrime():
    print('You\'ve asked if N is a prime.')
    while True:
        userInput = input('What is N? ')
        if not userInput.isdigit():
            print('Illegal value. Try again!')
            continue
        N = int(userInput)
        if 0 == N:
            print('Illegal value. Try again!')
            continue

        findPrimes(N)

        if _PRIMES[N]:
            print(f'{N} is prime\n')
        else:
            print(f'{N} is not prime\n')
        return

# Function 2 - List N prime numbers
def listNPrime():
    pass

# Function 3 - Display the Nth prime number
def dispNthPrime():
    print('You\'ve asked if N is a prime.')
    while True:
        userInput = input('What is N? ')
        if not userInput.isdigit():
            print('Illegal value. Try again!')
            continue
        userInput = int(userInput)
        print('were here')
        if 0 == userInput:
            print('Illegal value. Try again!')
            continue

# Function 4 - Find first prime after N
def firstPrime():
    pass

# Function 5 - Factor N
def factorN():
    pass

# Function 6 - Help message
def commandPrint():
    print("The following commands are available:")
    print("  0: Exit.")
    print("  1: Is N a prime?")
    print("  2: List the first N prime numbers.")
    print("  3: Display the Nth prime number (1-based).")
    print("  4: Find first prime after N.")
    print("  5: Factor N.")
    print("  6: Display this help message.")
    print()

def findPrimes(N):
    """Return a list of all prime numbers up to N using the Sieve of Eratosthenes."""
    global _PRIMES, _MAX_COMPUTED

    if N <= _MAX_COMPUTED:
        return _PRIMES

    # Handle some edge cases
    if N < 2:
        return []
    if N == 2:
        return [2]

    # Create a list of True from 0 through N
    primes = [True] * (N + 1)
    # Since first two values do not count as primes, set them to false
    primes[0] = primes[1] = False

    # As per the formula, we go from 2  until sqrt(N)
    for i in range(2, int(N**0.5) + 1):
        # As we go through the list, if it is considered prime
        if primes[i]:
            # Start j at i*i, end at N, step by i (as per the formula)
            for j in range(i*i, N + 1, i):
                # Make sure the multiple is not considered prime
                primes[j] = False

    _MAX_COMPUTED = N
    _PRIMES = primes
    # Return the full list of values that can be used for other functions
    return _PRIMES

def invalidChoice(command):
    print(f'Command {command} not recognized. Try Again!')
    commandPrint()

COMMANDS = {
    '0': exitFunc,
    '1': isPrime,
    '2': listNPrime,
    '3': dispNthPrime,
    '4': firstPrime,
    '5': factorN,
    '6': commandPrint
}

ALIASES = {
    'exit': '0',
    'leave': '0',
    'quit': '0',
    'info': '6',
    'help': '6',
}

def main():
    print('\nWelcome to the Prime Factory!')
    commandPrint()
    while True:
        # Get user input
        userInput = input('Please enter a command: ').strip().lower()

        # Check if user input is in ALIASES
        userKey = ALIASES.get(userInput, userInput)
        # Then check if key is in COMMANDS, if not, choice is return
        #   invalidChoice function
        userFunction = COMMANDS.get(userKey, invalidChoice)

        # If user input is invalid, run with userInput and continue
        if userFunction == invalidChoice:
            userFunction(userInput)
            continue
        # Otherwise, run function without input
        else:
            result = userFunction()

        # Decide whether to exit the loop
        if result:
            break

main()

# # Replaced by more efficient function!
# def findPrimes(N):
#     '''This function uses the Sieve of Eratosthenes to find all prime
#     numbers to any given limit N'''
#
#     # This is a list of Trues ranging from 2 to N, inclusive
#     primes = {num: True for num in range(2, N+1)}
#
#     # Go through each number in the dict
#     for key in primes.keys():
#         # If the number is true, it is a prime, so we need to make sure
#         #   there are no multiples contained within the dict
#         if primes[key]:
#             # j is just a counter to get j * i multiples
#             j = 0
#             # While the current multiple is less or equal to N
#             while (key**2) + (j * key) <= N:
#                 primes[(key**2) + (j * key)] = False
#                 j += 1
#
#     return list(key for key, value in primes.items() if value)