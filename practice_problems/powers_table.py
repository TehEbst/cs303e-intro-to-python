'''
Write a program that displays the following table:

a    a^2   a^3
1    1     1
2    4     8
3    9     27
4    16    64
Input Format

There is no input.

Constraints

N/A

Output Format

The table of powers should be displayed exactly as shown.

Sample Output 0

a    a^2   a^3
1    1     1
2    4     8
3    9     27
4    16    64
Explanation 0

The table is printed exactly as shown.
'''


# Define a list of inputs for the matrix
a_inputs = [1, 2, 3, 4]

# print the first line of the table
print("a    a^2   a^3")

# Iterate through each number in the list
for a in a_inputs:

    # Check if the second column has more than one digit
    if a**2 > 10:
        print(f'{a}    {a**2}    {a**3}')
    else:
        print((f'{a}    {a**2}     {a**3}'))