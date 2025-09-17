# File: DecisionTree.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-09-17
# Description of Program: The purpose of this program is for the algorithm to
#   tell the user whether they should purchase a computer or not based on the
#   table given in the assignment instructions.

# Assignment Link
# https://www.cs.utexas.edu/~byoung/cs303e/hw4.html

buy_str = 'This person will purchase a computer'
not_buy_str = 'This person will not purchase a computer'

age = int(input('Please enter person\'s age: '))
income = input('Person\'s income (High, Medium, Low): ')
student = input('Is this person a student (Yes or No)? ')
credit = input('Does this person have good credit (Yes or No)? ')
print()

if age <= 30:
    if income == 'Low':
        print(buy_str)
    elif income == 'Medium':
        if student == 'Yes':
            print(buy_str)
        else:
            print(not_buy_str)
    else:
        print(not_buy_str)
elif 30 < age <= 40:
    print(buy_str)
else:
    if credit == 'No':
        print(buy_str)
    else:
        print(not_buy_str)