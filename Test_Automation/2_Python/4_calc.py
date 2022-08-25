def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a + b)
    
def substract():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a - b)
    
def multiply():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a * b)
    
def divide():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a / b)
    
option = int(input("What you want to do?\n1. Add\n2. Substract\n3. Multiplication\n4. Division\n\nSelected option: "))
if option == 1:
    add()
elif option == 2:
    substract()
elif option == 3:
    multiply()
elif option == 4:
    divide()
else:
    print("That option doesn't exists.")