####### VARIABLES

# Python comments are marked with the # symbol
# Variables are case sensitive.
cAr = 21
CaR = 22

# Variables can start with _
_car = 'Mazda'

# Variables should be descriptive
car = 24

# If a variable is repeated, will take the last value assigned to it.
car = 99

# Multi underscore for descriptive variables
number_of_cars = 25

# Print used to output into the console the values
print(cAr)
print(CaR)
print(_car)
print(car)
print(number_of_cars)

####### Variable types
### Strings
# Enclosed in single or double quotes, you must be consistent on its use
# Immutable (operations cannot be performed on Strings)
# 'Pedro' - "Pedro"

### Number
# Mathematical operations can be performed with integers
# 22, 24, 42, 30894

### Floating Point numbers
# Fractional or decimal numbers
# Mathematical operations can be performed on these type of variables
# Python calculates the number of decimal places for you
# 3.141592, 42.24, 0.01

print("\n========== Line break ==========\n")

"""
This is a multi-line comment.
You can use this kind of comment to make longer
notes as you are learning.

In Python, these are often used as doctrings.
We will do formatting now.
"""

name = "Daniel Cadena"
type_of_car = "Mazda"
school = "UVEG"

# Concatenating the variables in output
print(name + type_of_car + school)

print(name + " " + school)

print(name + " studies at " + school + ".")

# Python string.format()
print("{} studies at {}.".format(name, school))