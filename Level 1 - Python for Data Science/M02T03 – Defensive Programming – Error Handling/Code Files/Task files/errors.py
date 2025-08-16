# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program,
# look at the error messages, and find and fix the errors.


print("Welcome to the error program")  # Syntax error fixed: print needs brackets
print("\n")  # No indent required, also needs brackets

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24 years old"  # Fixed variable name and no indent was required, and would get a run time error
age = int(age_str[0:3]) #syntax error and run time error since code was indented, need to pull the age out of the age_str using indexes
print("I'm " + str(age) + " years old.")  # Age must be cast to string

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) #cast years_from_now to int, run time errror
print(f"The total number of years: {total_years}")  #syntax error

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 #syntax error, since total variable does not exist
print(f"In 3 years and 6 months, I'll be {total_months + 6} months old.") #logical error

# HINT: 330 months is the correct answer
