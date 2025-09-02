'''
The mathematical constant pi can be computed using the following formula

π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

Write a program that displays the result of

π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)

and

π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15)

Input Format

There is no input.

Constraints

N/A

Output Format

The results of each expression should be displayed, one per line.

Sample Output 0

2.9760461760461765
3.017071817071818
Explanation 0

The result of each expression is printed.
'''

# Define how many summations we should do of Leibniz Formula for Pi
oscillations = (6, 8)

# For each option given in the question stem
for summations in oscillations:

    # Variables to store summation from the inside of the parenthesis
    sum = 1
    denom = 3
    sign = -1

    # iterate through each summation in the parenthesis besides 1
    for i in range(summations - 1):
        denom = 3 + (2 * i)
        sum = sum + (1 / denom) * sign
        sign *= -1

    print(4 * (sum))