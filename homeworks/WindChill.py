# File: WindChill.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 09-02-2025
# Description of Program:

# Inputs
# Fahrenheit Temperature
# Wind speed in mph

# Compute two wind speed reports
# Fahrenheit
#   T_wc = 35.74 + 0.6215*T - 35.75*V**0.16 + 0.4275*T*V**0.16
#   -58 <= T <= 41
#   2 <= V
# Celsius
#   C = (F - 32) * 5/9
#   kilometers = miles * 1.60934

# User input Fahrenheit temperature and miles per hour wind speed
#   stored as a float
f_temp = 41 # float(input('Enter Fahrenheit temperature: '))
if -58 <= f_temp <= 41:
    mph_ws = 1 # float(input('Enter wind speed in miles per hour: '))
    if 2 <= mph_ws:
        # Calculate wind chill temperature using given formula
        f_wc_temp = (35.74 +
                     0.6215 * f_temp -
                     35.75 * mph_ws ** 0.16 +
                     0.4275 * f_temp * mph_ws ** 0.16)

        # Convert all values into Celsius and kilometers per hour
        c_temp = (f_temp - 32) * 5 / 9
        kph_ws = mph_ws * 1.60934
        c_wc_temp = (f_wc_temp - 32) * 5 / 9

        # Print out Fahrenheit report
        print('Fahrenheit report')
        print('  Temperature: ' + format(f_temp, "8.3f") + ' \u00B0' + 'F')
        print('  Wind speed: ' + format(mph_ws, "9.3f") + ' mph')
        print('  Wind chill: ' + format(f_wc_temp, "9.3f") + ' \u00B0' + 'F')

        # Print out Celsius report
        print('Celsius report')
        print('  Temperature: ' + format(c_temp, "8.3f") + ' \u00B0' + 'C')
        print('  Wind speed: ' + format(kph_ws, "9.3f") + ' kph')
        print('  Wind chill: ' + format(c_wc_temp, "9.3f") + ' \u00B0' + 'C')
    else:
        print('Wind speed must be at least 2 mph.')

else:
    print('Temperature should be in range [-58 .. 41].')