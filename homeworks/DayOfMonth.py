# File: DayOfMonth.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 09-12-2025
# Description of Program:

# define constants
JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

(JAN_DAYS, MAR_DAYS, APR_DAYS, MAY_DAYS, JUN_DAYS, JUL_DAYS, AUG_DAYS,
 SEP_DAYS, OCT_DAYS, NOV_DAYS, DEC_DAYS) = (
    31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def computeOrdinalDate():
    # take user input for year
    inputYear = input("Specify a year: ")

    # validate user input for year
    if inputYear.isdigit() and int(inputYear) > 1752:
        year = int(inputYear)
    else:
        print("Bad year entered:", inputYear)
        return

    # check if leap year
    isLeapYear = (year % 4 == 0) and ( not (year % 100 == 0) or (year % 400 == 0) )

    # specify number of days in february
    FEB_DAYS = 29 if isLeapYear else 28

    # take user input for month
    inputMonth = input("Specify a month (1-12): ")

    # validate user input for month
    if inputMonth.isdigit() and 1 <= int(inputMonth) <= 12:
        month = int(inputYear)
    else:
        print("Bad month entered:", inputMonth)
        return

    # take user input for day
    inputDay = input("Specify a day of the month: ")

    # validate user input for day
    if inputDay.isdigit():
        day = int(inputDay)

        # make sure function is within range of each possible month
        if not (
                (month == FEB and 1 <= day <= FEB_DAYS)
            or ((month == JAN) or (month == MAR) or (month == MAY) or (month == JUL) or
                (month == AUG) or (month == OCT) or (month == DEC) or (1 <= day <= 31))
            or (

                )
        ):
            print("Bad day entered", inputDay)
            return
        else:
            return

    else:
        print("Bad day entered", inputDay)
        return

    # take day component and add sum of the number of days in previous months

    # print day

computeOrdinalDate()