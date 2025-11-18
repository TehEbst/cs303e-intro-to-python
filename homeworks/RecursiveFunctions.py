# File: RecursiveFunctions.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-11-14
# Description of Program: A collection of functions to help teach me how to
# think recursively. Each function is recursive and all return their answers
# allowing them to be used easily in future programs.


def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Return the sum of the non-negative integers to n.
   E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5 """

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer.
   E.g., findSumOfDigits( 1234 ) = 10 """

def integerToBinary( n ):
   """ Given a nonnegative integer n, return the
   binary representation as a string. E.g.,
   integerToBinary( 10 ) = '1010' """

def integerToList( n ):
   """ Given a nonnegative integer, return a list of the
   digits (as strings).
   E.g., integerToList( 123 ) = ['1', '2', '3'] """

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome.
   Case counts: 'abA' is not a palindrome. """

def findFirstUppercase( s ):
   """ Return the first uppercase letter in
   string s, if any. Return None if there
   is none. """

# for this one, don't reverse the string.
def findLastUppercase( s ):
   """ Return the last uppercase letter in
   string s, if any. Return None if there
   is none. """

def negateItems( lst ):
   """Assume lst is a list of numbers.  Return a list
   of the negations of those numbers."""

def findLargest( lst ):
   """Assume lst is a list of numbers. Recursively find
   and return the largest element."""