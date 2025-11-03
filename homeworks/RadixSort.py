# Assignment: HW10
# File: RadixSort.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-11-02
# Description of Program: This program implements a radix sort method for a
#   one dimensional list. The user can specify how many rounds of radix
#   should be completed. This program does not return anything, it only
#   prints out the unsorted input data, the sorted output list,
#   and optionally the 2D sort list of buckets. The input must be a one
#   dimensional list of positive integer values.

import random

def radixSort( testData, rounds, seeRounds=False ):
    # Given a list testData of random integers, none of more than rounds
    # digits, use radix sort to sort them.

    # Print input data
    print( "\nInput data:" )
    print( testData )

    # Run for n rounds, where each round should be a digit for the element
    for i in range( rounds ):

        # Generate a sort list of 10 empty lists
        sortLists = [[] for _ in range(10)]

        # Loop through each item in testData
        for item in testData:
            # print(f'    DEBUG: {item}')

            digitList = listOfDigits(item)

            # print(f'    DEBUG: {digitList}')

            # append item to sortList[d], d is the current round's digit
            sortLists[getDigit(digitList, i)].append(item)

        # Optional printing of each bucket sorted list per round
        if seeRounds:
            print(f'\nRound: {i}')
            nestedListPrint(sortLists)

        testData = flatten(sortLists)

    # Print output data
    print( "\nFinal sorted list:" )
    print( testData )
    return testData

def listOfDigits( num ):
    # Given a non-negative integer num, return a list of its digits,
    # from least to most significant.

    digitList = []

    while True:
        # print(f"DEBUG: Current num is: {num}")
        if 10 > num:
            digitList.append(num)
            return digitList
        # Num mod 10 returns the rightmost digit value
        digitList.append(num % 10)

        # Num floor division 10 removes the rightmost digit
        num //= 10

def getDigit( num, k ):
    # Given a list of digits, select the kth one, if any.  Otherwise,
    # return 0.

    if k > len(num) - 1:
        return 0
    else:
        return num[k]

def flatten( nestedList ):
    # Flattens a 2D list into a 1D one
    flatList = []

    for lst in nestedList:
        for element in lst:
            flatList.append(element)

    return flatList

def nestedListPrint( nestedList ):
    # A function to make printing a nested list simple, clean, and aesthetic
    print('[ ', end="")
    for i, sublist in enumerate(nestedList):
        if i == 0:
            print(sublist)
        elif i == len(nestedList) - 1:
            print(f'  {sublist} ]')
        else:
            print(f'  {sublist}')

def main():
    # This is just for testing; it generates a list of 50 random integers
    # between 0 and 999.
    testData = [random.randint(0, 9999) for i in range(20)]
    rounds = 4

    # This calls radixSort on the randomly generated test data for 3 rounds.
    # It would be a good idea to test your code on different size data.

    radixSort(testData, rounds)

# main()
