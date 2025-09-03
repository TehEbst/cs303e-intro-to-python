'''
Consider a country for which population is projected based on the following assumptions:

One birth every 6 seconds
One death every 15 seconds
One new immigrant every 45 seconds
Write a program to display the population for each of the next five years. Assume the current population is 373582814 and one year has 365 days.

Input Format

There is no input.

Constraints

N/A

Output Format

The populations for each of the next five years should be displayed, one per line.

Sample Output 0

377437214
381291614
385146014
389000414
392854814
'''

# Population = Initial Population + Babies Added - Deaths + Immigrants Added

# Babies addded = birth rate * time

# Seconds in a year = 365 days * 24 hours * 60 mins * 60 secs

year_to_secs = 31536000

initial_pop = 373582814

for i in range(5):
    years_to_secs = (i + 1) * year_to_secs
    babies_added = years_to_secs / 6
    immigrants_added = years_to_secs / 45
    deaths = years_to_secs / 15

    print(int(initial_pop + babies_added + immigrants_added - deaths))