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
import sys
sys.setrecursionlimit(1000000)

# Function 0 - Exit
def exitFunc():
    print('Thanks for visiting our factory! Goodbye.')
    return True

# Function 1 - Is input N a prime number?
def isPrime():
    print('You\'ve asked if N is a prime.')
    while True:
        userInput = input('What is N? ')

        inputValidation = validateN(userInput, 0)

        if not inputValidation[0]:
            continue

        N = inputValidation[1]

        if isNumPrime(N):
            print(f'{N} is prime\n')
        else:
            print(f'{N} is not prime\n')
        return

# Function 2 - List N prime numbers
def listNPrime():
    print('You\'ve asked to display the first N prime numbers.')
    while True:
        # Take user input and validate it
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, -1)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        # Variable to store the prime numbers
        primes = []
        # Counter variable to go through numbers
        i = 0

        while len(primes) != N:
            is_i_prime = isNumPrime(i)
            if is_i_prime:
                primes.append(i)
            i += 1

        print(f'The first {N} primes are:', primes, end='\n\n')

        return

# Function 3 - Display the Nth prime number
def dispNthPrime():
    print('You\'ve asked for the Nth prime number.')
    while True:
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, 0)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        # Variable to store the prime numbers
        primes = []
        # Counter variable to go through numbers
        i = 0

        while len(primes) <= N:
            is_i_prime = isNumPrime(i)
            if is_i_prime:
                primes.append(i)
            i += 1

        print(f'The {N}th prime number is:', primes[N-1], end='\n\n')

        return

# Function 4 - Find first prime after N
def firstPrime():
    print('You\'ve asked for the first prime number after N.')
    while True:
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, -math.inf)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        if N < 2:
            print(f'The first prime after {N} is:', 2, end='\n\n')
            return

        # Variable to store the prime numbers
        primes = []
        # Counter variable to go through numbers
        i = 0

        while max(primes, default=0) < N:
            is_i_prime = isNumPrime(i)
            if is_i_prime:
                primes.append(i)
            i += 1

        print(f'The first prime after {N} is:', primes[-1], end='\n\n')

# Function 5 - Factor N
def factorN():
    print('You\'ve asked for the prime factorization of N.')
    while True:
        userInput = input('What is N? ')
        inputValidation = validateN(userInput, 1)
        if not inputValidation[0]:
            continue
        N = inputValidation[1]

        primeFactors = primeFactorization(N)

        print(f'The prime factorization of {N} is: {primeFactors}', end='\n\n')

        return

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

# HELPER FUNCTIONS
def isNumPrime(num, divisor=2):
    # Make the base cases
    if num <= 1:
        return False
    if num == 2:
        return True

    # Create the stopping criteria. Apparently math says if we haven't found
    #   a divisor up to sqrt(num), then it's prime
    if divisor * divisor > num:
        return True
    elif num % divisor == 0:
        return False
    else:
        # Make the function recursive
        return isNumPrime(num, divisor + 1)

def primeFactorization(N):
    factors = []
    d = 2
    while N > 1 and not isNumPrime(N):
        if N % d == 0:
            if isNumPrime(d):
                factors.append(d)
                N //= d
                d = 2
        else:
            d += 1

    # If N is prime, we need to add it
    if isNumPrime(N):
        factors.append(N)
        return factors

    return factors

def invalidChoice(command):
    print(f'Command {command} not recognized. Try Again!')
    commandPrint()

def validateN(userInput, cutoffNumber):
    # Handle empty string
    if not userInput:
        return False, None

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

# # Replaced by recursive function to work better with program
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