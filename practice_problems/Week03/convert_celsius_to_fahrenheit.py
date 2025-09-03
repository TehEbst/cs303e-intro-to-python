'''
Write a program that reads a temperature in Celsius, converts it to Fahrenheit,
and displays the result, rounded to the nearest tenth of a degree.
The formula for the conversion is as follows:

fahrenheit = 9/5 * celsius + 32

Input Format

There will be a single floating point value, the temperature in celsius.

Constraints

-273 <= celsius <= 10000

Output Format

The temperature in Fahrenheit should be displayed, rounded to a single decimal place.

Sample Input 0

37

Sample Output 0

98.6

Explanation 0

(9 / 5) * 37 + 32 = 98.6 rounded to the nearest tenth

Sample Input 1

20
Sample Output 1

68.0
Explanation 1

(9 / 5) * 20 + 32 = 68.0 rounded to the nearest tenth
'''

# input in Celsius within range
c_temp = float( input() )

# convert Celsius to Fahrenheit
f_temp = 9/5 * c_temp + 32

# output temp in Fahrenheit rounded to nearest tenth
print( format(f_temp, '.1f') )