'''
Write a program that reads in the radius and length of a cylinder and computes
the area and volume using the following formulas:

Input Format

The first line will contain the radius of the cylinder
(a floating point value), and the second line will contain the length of the
cylinder (a floating point value).

Constraints

Output Format

The first line of output should be the area of the cylinder, and the second
line of output should be the volume of the cylinder. Both values should be
rounded to two decimal places.

Sample Input 0

5.5
12
Sample Output 0

95.03
1140.40
Sample Input 1

3
8
Sample Output 1

28.27
226.19
'''

from math import pi

# gather 2 inputs
#   radius
#   length
radius = float( input() )
length = float( input() )

# compute area
area = pi * radius ** 2

# compute volume
volume = area * length

# output area
print( format(area, '.2f') )

# output volume
print( format(volume, '.2f') )