'''
Write a program that reads the number of minutes and displays the number of
years and days for the minutes. For simplicity, assume a year has 365 days.
Round down to the nearest day. (Hint: consider using the // and % operators)

Input Format

The only line of input will contain the number of minutes (an integer).

Constraints

Output Format

The only line of output should contain the number of years and days, formatted
as shown in the sample outputs.

Sample Input 0

1000000000
Sample Output 0

1000000000 minutes is approximately 1902 year(s) and 214 day(s)
Sample Input 1

527040
Sample Output 1

527040 minutes is approximately 1 year(s) and 1 day(s)
'''

# input number of minutes
minutes = int( input() )

# convert minutes to years; minutes in a year: 525600
years = minutes // 525600

# convert remainder to days: minutes in a day
days = (minutes % 525600) // 1440

# output number of years and days
# sample: 1000000000 minutes is approximately 1902 year(s) and 214 day(s)

print( f'{minutes} minutes is approximately '
       f'{years} year(s) and {days} day(s)' )