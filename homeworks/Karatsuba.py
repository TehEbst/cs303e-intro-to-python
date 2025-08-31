# File: Karatsuba.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 08-30-2025
# Description of Program: This program asks the user for 2 4-digit integers.
#   It then calculates and prints out the results of Karatsuba Multiplication
#   as "computed result" and the default python multiplication as "expected
#   result."

#   Assignment Link:
#   https://www.cs.utexas.edu/~byoung/cs303e/hw2.html

# The following are steps of the Karatsuba Multiplication method as provided
#   in the assignment instructions

# Step 1
n1 = int( input("Enter a 4-digit integer: ") )
n2 = int( input("Enter a 4-digit integer: ") )

# Step 2
a = n1 // 100
b = n1 % 100

# Step 3
c = n2 // 100
d = n2 % 100

# Step 4
e = a * c

# Step 5
f = b * d

# Step 6
g = (a + b) * (c + d)

# Step 7
h = g - (e + f)

# Step 8
i = e * 10**4

# Step 9
j = h * 10**2

# Step 10
k = i + j + f

# Compute answer using the default method
ans = n1 * n2

print('Computed result:', k)
print('Expected result:', ans)