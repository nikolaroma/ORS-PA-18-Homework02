"""
===================   TASK 2   ====================
* Name: Convert Kilometers To Miles
*
* Write a script that will convert kilometers to
* miles. Script should ask user for input and check
* if user input is valid. If not, the script should
* quit immediately with appropriate message.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You may use `can_string_be_float` function
* from previous task to validate user input.
===================================================
"""


kilometers = float(input("Enter value in kilometers"))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%f kilometers is equal to %f miles' %(kilometers, miles))