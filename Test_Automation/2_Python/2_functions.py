# Function: Unit of code that can be reused throughout a program.
'''
Declaration - function name - parameters in parenthesis
def function():
    // Indented 4 spaces
'''

def addition():
    a = 10
    b = 14
    print(a + b)
    
# Calling the function
addition()

# input. Reads information from the user
# int. Converts the data into an integer
def addition2():
    a = int(input("Enter a number: "))
    b = int(input("Enter the second number: "))
    print(a + b)
    
addition2()