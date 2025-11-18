# Assignment: Project 2
# File: PrimeFactory.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date Created: 2025-11-06
# Date Last Modified: 2025-11-17
# Description of Program: This is a prime factory that creates a loop that
# continually asks the user what they want to do out of a list of several
# prime number related functions. It uses a recursive approach.

import math
import time

HIGHEST_NUM = 0
NUM_PRIMES = 0
ALL_NUMS = []
PRIMES = []

# Function 0 - Exit
def exitFunc():
    """ This is a function to exit the main program loop and print out a
    message """
    print('Thanks for visiting our factory! Goodbye.')
    return True

# Function 1 - Is input N a prime number?
def isPrime():
    """ Made to work with main loop function, this function tells you
    whether the input number is or isn't prime. """
    print('You\'ve asked if N is a prime.')
    while True:
        # User input and validation
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, 0)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        # Run our find primes function to make sure N is in our list. I
        #   honestly don't have a great solution so we just find the next
        #   1000000 numbers until the number of primes is bigger than N.
        while not HIGHEST_NUM > N:
            findPrimes(HIGHEST_NUM + 1000000)

        # Print out a response depending on whether N is prime or not
        if ALL_NUMS[N]:
            print(f'{N} is prime\n')
        else:
            print(f'{N} is not prime\n')
        return

# Function 2 - List N prime numbers
def listNPrime():
    """ Made to work with the main loop function, this function takes a user
    input N and prints out that many prime numbers """
    print('You\'ve asked to display the first N prime numbers.')
    while True:
        # Take user input and validate it
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, -1)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        # Run our find primes function to make sure N is in our list. I
        #   honestly don't have a great solution so we just find the next
        #   1000000 numbers until the number of primes is bigger than N.
        while not NUM_PRIMES > N:
            findPrimes(HIGHEST_NUM + 1000000)

        print(f'The first {N} primes are:', PRIMES[0:N], end='\n\n')

        return

# Function 3 - Display the Nth prime number
def dispNthPrime():
    """ Displays the user input Nth prime number. Made to work with the
    main loop. """
    print('You\'ve asked for the Nth prime number.')
    while True:
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, 0)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        # Run our find primes function to make sure N is in our list. I
        #   honestly don't have a great solution so we just find the next
        #   1000000 numbers until the number of primes is bigger than N.
        while not NUM_PRIMES > N:
            findPrimes(HIGHEST_NUM + 1000000)

        # Print out the Nth prime number
        print(f'The {N}th prime number is:', PRIMES[N-1], end='\n\n')

        return

# Function 4 - Find first prime after N
def firstPrime():
    """" This function displays the first prime number after N. """
    print('You\'ve asked for the first prime number after N.')
    while True:
        # Handle user input and validation
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, -math.inf)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        # Cover an edge case of a number less than 2
        if N < 2:
            print(f'The first prime after {N} is:', 2, end='\n\n')
            return

        # Run our find primes function to make sure N is in our list. I
        #   honestly don't have a great solution so we just find the next
        #   1000000 numbers until the number of primes is bigger than N.
        i = 1
        while not max(PRIMES) > N:
            findPrimes(N + 1000000*i)
            i += 1

        primeAfter = 0
        for i in range(0, NUM_PRIMES):
            if PRIMES[i] > N:
                primeAfter = PRIMES[i]
                break

        print(f'The first prime after {N} is:', primeAfter, end='\n\n')
        return

# Function 5 - Factor N
def factorN():
    """ This function finds the prime factorizations of the user input
    number N. """
    print('You\'ve asked for the prime factorization of N.')
    while True:
        # Take user inputs and validate them
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, 1)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        # Run our find primes function to make sure N is in our list. I
        #   honestly don't have a great solution so we just find the next
        #   1000000 numbers until the number of primes is bigger than N.
        if not HIGHEST_NUM > N:
            findPrimes(N)

        # Call prime factorization function and print out the result
        primeFactors = primeFactorization(N)
        print(f'The prime factorization of {N} is: {primeFactors}', end='\n\n')

        return

# Function 6 - Help message
def commandPrint():
    """ This function displays the list of commands that can be executed in
    the main loop. """
    print("The following commands are available:")
    print("  0: Exit.")
    print("  1: Is N a prime?")
    print("  2: List the first N prime numbers.")
    print("  3: Display the Nth prime number (1-based).")
    print("  4: Find first prime after N.")
    print("  5: Factor N.")
    print("  6: Display this help message.")
    print()


# HELPER FUNCTIONS
# Was stupidly removed in favor of recursive approach, but it is back. This
#   function is not implemented with the greatest efficiency since the
#   recursive approach was switched to this one kind of last minute.
def findPrimes(N=100000000):
    ''' This function uses the Sieve of Eratosthenes to find all prime
    numbers to any given limit N. By default it is set to 1000000. This
    function returns a list of length N denoting whether each number is
    prime or not prime with a True or False. '''
    global HIGHEST_NUM, NUM_PRIMES, ALL_NUMS, PRIMES

    if N < HIGHEST_NUM:
        return

    # Create a list of True from 0 through N
    ALL_NUMS = [True] * (N + 1)
    # Since first two values do not count as primes, set them to false
    ALL_NUMS[0] = ALL_NUMS[1] = False

    # Some time saving changes
    limit = int(N**0.5) + 1
    nums = ALL_NUMS

    # As per the formula, we go from 2  until sqrt(N)
    for i in range(2, limit):
        # As we go through the list, if it is considered prime
        if nums[i]:
            step = i
            start = i * i
            nums[start: N+1: step] = [False] * (((N - start) // step) + 1)

    # Reassign all of the global constants
    ALL_NUMS = nums
    HIGHEST_NUM = N
    PRIMES = [i for i, is_prime in enumerate(ALL_NUMS) if is_prime]
    NUM_PRIMES = len(PRIMES)
    return

def primeFactorization(N):
    """ A helper function that finds the prime factors for the input N. It
    will return a list of the prime factors. """
    factors = []

    # A counter to take us up the PRIMES list
    i = 0
    while i < NUM_PRIMES:
        if N == 1:
            break
        primeNumber = PRIMES[i]
        if N % primeNumber == 0:
            factors.append(primeNumber)
            N /= primeNumber
            i = 0
        else:
            i += 1

    return factors

def invalidChoice(command):
    """ This is a helper function that prints out a line warning the user of
    an invalid input followed by the list of commands that are valid. """
    print(f'Command {command} not recognized. Try Again!')
    commandPrint()

def validateN(userInput, cutoffNumber):
    """ A helper function that validates whether the input userInput is a
    valid N which is an integer greater than the cutoff number. Returns
    whether the number is valid with a tuple indicating True or False in the
    first position and either the number or None depending on if the input
    was valid. """
    # Handle empty string
    if not userInput:
        return False, None

    # Make sure there are no extraneous spaces
    userInput = userInput.strip()

    inputIsNegative = False
    # Handle negative numbers
    if userInput[0] == '-':
        inputIsNegative = True

    if inputIsNegative:
        if not userInput[1:].isdigit():
            print('Illegal value. Try again!')
            return False, None
    else:
        if not userInput.isdigit():
            print('Illegal value. Try again!')
            return False, None

    N = int(userInput)
    if not N > cutoffNumber:
        print('Illegal value. Try again!')
        return False, None
    return True, N

# A dictionary that creates a key: value pair between a string command and
# function call.
COMMANDS = {
    '0': exitFunc,
    '1': isPrime,
    '2': listNPrime,
    '3': dispNthPrime,
    '4': firstPrime,
    '5': factorN,
    '6': commandPrint
}

# A dictionary that creates a key: value pair between a string command and
# the appropriate command from the previous dictionary.
ALIASES = {
    'exit': '0',
    'leave': '0',
    'quit': '0',
    'info': '6',
    'help': '6',
}

# The main loop
def main():
    print('\nWelcome to the Prime Factory!')
    commandPrint()
    findPrimes()
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
            start_time = time.time()  # record start
            userFunction(userInput)
            end_time = time.time()  # record end
            elapsed = end_time - start_time
            print(f"Function took {elapsed:.6f} seconds")
            continue
        # Otherwise, run function without input
        else:
            start_time = time.time()  # record start
            result = userFunction()
            end_time = time.time()  # record end
            elapsed = end_time - start_time
            print(f"Function took {elapsed:.6f} seconds")

        # Decide whether to exit the loop
        if result:
            break
main()

# start_time = time.time()  # record start
# findPrimes()
# end_time = time.time()  # record end
# elapsed = end_time - start_time
# print(f"Function took {elapsed:.6f} seconds")