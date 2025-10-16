# Assignment: HW6
# File: FunctionExamples.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date Created:
# Description of Program: This python program is a collection of multiple
#   mathematical utility functions to learn how to create functions in Python.
#   It makes use of a couple functions from the math library to perform a few
#   basic mathematical computations.
#   The program includes 16 different functions that each solve a unique
#   computational problem.

# Assignment Link:
#   https://www.cs.utexas.edu/~byoung/cs303e/hw6.html

from math import sqrt, pi

#----------------------------------------------------------------------
# 1. Write a function to return the sum of three numbers.  I did this
#    one for you.

def sum3Numbers (x, y, z):
    """Return the sum of the three parameters."""

    return x + y + z

#----------------------------------------------------------------------
# 2. Write a function to return the product of three numbers.

def multiply3Numbers( x, y, z ):
    """Multiply x * y * z."""

    return x * y * z

#----------------------------------------------------------------------
# 3. Write a function to return the sum of up to 3 numbers.  It should
#    accept 1, 2, or 3 parameters.  Hint: any parameter not given
#    defaults to 0.

def sumUpTo3Numbers (x, y = 0, z = 0):
    """
    Sum x * y * z but if y and z are not given, they default to 0.
    Accepts a minimum of 1 parameter and a max of 3
    """

    return x + y + z

#----------------------------------------------------------------------
# 4. Write a function to return the product of up to 3 numbers.  It
#    should accept 1, 2, or 3 parameters.  Hint: what should the
#    default be in this case?

def multiplyUpTo3Numbers (x, y = 1, z = 1 ):  # supply default args
    """
    Multiply up to three numbers with default being 0 for y and z.
    Accepts a minimum of one parameter and a max of 3.
    """

    return x * y * z

#----------------------------------------------------------------------
# 5. Write a function that takes 2 numbers as input and prints them
#    out in ascending order.  Make sure it works if they are equal.
#    Don't use lists or the sort function.

def printInOrder( x, y ):
    """Prints two input numbers in ascending order"""

    if x > y:
        print(y, x)
    else:
        print(x, y)

#----------------------------------------------------------------------
# 6. Write a function that returns the area of a square, given the length
#    of a side. Print an error message if side is negative.

def areaOfSquare( side ):
    """Returns are of a square given length of a non-negative side"""

    if side < 0:
        print('Negative value entered')
    else:
        return side**2

#----------------------------------------------------------------------
# 7. Write a function that returns the perimeter of a regular 2D
#    figure of k sides, given the length of a side.  (Regular means all k
#    sides are the same length.)  Print an error message if side or k is
#    negative.

def perimeterOfFigure( k, side ):
    """
    This function returns the perimeter a figure given equal side lengths.
    It takes the number of sides and the side length as inputs and it
    validates whether the input is a positive number.
    """

    if side < 0 or k < 0:
        print('Negative value entered')
    else:
        return k * side

#----------------------------------------------------------------------
# 8. Write a function that returns the length of the diagonal of a
#    rectangle of given height and width.  This is computed as the square
#    root of the sum of the squares of h and w.

def diagonalOfRectangle( h, w ):
    """
    Returns the diagonal of a rectangle with the following formula:
    sqrt(h^2 + w^2). Also validates whether both inputs are positive
    """

    if h < 0 or w < 0:
        print('Negative value entered')
    else:
        return sqrt(h**2 + w**2)

#----------------------------------------------------------------------
# 9. Write a function that returns the area of a circle, given the
#    radius.  Use math.pi. Print an error message if radius is negative.

def areaOfCircle( radius ):
    """
    Returns the area of a circle. Uses pi from math library. Also
    validates whether radius is a positive number
    """

    if radius < 0:
        print('Negative value entered')
    else:
        return pi * radius**2

#----------------------------------------------------------------------
# 10. Write a function that returns the circumference of a circle given
#    the radius.  Use math.pi. Print an error if radius is negative.

def circumferenceOfCircle( radius ):
    """
    This function returns the circumference of a circle given the
    radius as an input. It validates that the input is a positive
    number. Makes use of pi from the math library
    """

    if radius < 0:
        print('Negative value entered')
    else:
        return 2 * pi * radius

#----------------------------------------------------------------------
# 11. Write a function: given parameters d1, d2, x, returns whether
#    both d1 and d2 are both factors of (evenly divide) x.  You can
#    assume all values are integers.

def bothFactors( d1, d2, x ):
    """
    This function checks if d1 and d2 can both evenly divide into
    x. Returns True or False.
    """

    if x % d1 == 0 and x % d2 == 0:
        return True
    else:
        return False

#----------------------------------------------------------------------
# 12. Given a value x, compute and print out the area and circumference of a circle with
#    radius x and the area and perimeter of a square with side x.  Call your previous
#    functions for these computations.  Leave a blank line above and below the printing.

def squareAndCircle( x ):
    """
    Given an input of x, will call on previous functions to print out the area
    and circumference of a circle along with the area and perimeter of a square.
    """

    # Compute area and circumference of a circle and print
    print(f'\n'
          f'Circle with radius {x} has: \n'
          f'\t Area: {areaOfCircle( x )} \n'
          f'\t Circumference: {circumferenceOfCircle( x )}')

    # Compute area of square and print
    print(f'Square with side {x} has: \n'
          f'\t Area: {areaOfSquare( x )} \n'
          f'\t Perimeter: {perimeterOfFigure( 4, x)}'
          f'\n')

#----------------------------------------------------------------------
# 13. Write a function that returns the factorial of a positive
#     integer n.  Use a for loop to compute the factorial.  You can
#     assume the input is an integer, but print an error message if
#     it's not positive and return None.

def factorial( n ):
    """
    This function computes the factorial of a positive integer n. It
    validates that the integer is positive. It then returns the
    computed factorial value.
    """

    if n < 0:
        print('Input must be positive.')
    else:
        compFact = 1
        for i in reversed( range( n ) ):
            compFact *= i + 1
        return compFact

#----------------------------------------------------------------------
# 14. Write a function that returns the number of digits in the
#     decimal representation of an integer n.  You can assume that
#     n is positive.  E.g., numberLength( 12345 ) = 5.  Don't convert
#     the argument to a string.

def numberLength( n ):
    """
    This function determines the number of digits in an integer
    without typecasting into a string. It then returns the number of
    digits
    """

    # Variable to store the number of digits
    count = 0

    # This works by doing integer division, which is floor division
    #   Basically, if we divide by 10, it moves the right most digit to the
    #   decimal place, but since this is floor division, the decimal is
    #   eliminated, and the number becomes one digit shorter. We can keep
    #   doing this until the number becomes zero, and we don't have to account
    #   for negative numbers.
    while n > 0:
        n //= 10
        count += 1

    return count

#----------------------------------------------------------------------
# 15. Write a function that sums positive numbers entered by the user
#     and returns the sum.  You can assume that user inputs are
#     numbers (float or int).  If the number entered is negative, print
#     an error message and continue;  don't add it to the sum.  There
#     can be any number of inputs.  Stop when the user enters 0.
#     (Note: This was a problem from Exam1 in an earlier semester.)

def sumPositiveNumbers():
    """
    This function continuously asks the user for inputs and will add the
    number they inter to a running sum. It works with both floats and
    integers. The function will alert the user of an illegal negative input
    but will continue running. The function continues until the user inputs
    a 0.
    """

    # This is the number that stores the sum
    sumOfInputs = 0

    # Since function allows floating point, I am adding a slight
    #   tolerance so function doesn't fail (not sure if this is necessary)
    tol = 1e-9

    # Loop until user enters 0
    while True:
        userInput = float( input('Enter a number: ') )

        # Check if input is negative
        if userInput < 0:
            print('Illegal input.')
        elif abs( userInput) < tol:
            break
        else:
            sumOfInputs += userInput

    return sumOfInputs

#----------------------------------------------------------------------
# 16. Complete the function below that sums the following series:
#
#      (1 * 2) + (2 * 3) + (3 * 4) + ... + (n-1 * n)
#
#    Your function should use a for loop to compute the answer. Return,
#    don't print, the answer.  You can assume that n is a positive integer
#    greater than 1.  For example if n is 4, this is the series (1 * 2) +
#    (2 * 3) + (3 * 4) and your function should return 20.

def sumSeries( n ):
    """
    This function calculates and returns a summation series of (n-1 * n) +
    (n-2 * n-1) +...
    """

    sumOfSeries = 0

    for i in range(1, n):
        sumOfSeries += ( (i) * (i + 1) )

    return sumOfSeries
