# For Loop
fruits = ["Apple", "Orange", "Mango", "Strawberry"]

for fruit in fruits:
    print("Would you like {}?".format(fruit))
    
# Range(initial number inclusive, limit number non inclusive)
for number in range(1, 11):
    print("Number {}".format(number))
    
temp_f = 40

while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if (temp_f == 33):
        break
    
# Loop controls 
# BREAK - end the loop, go to the next statement in the program (outside the loop)
# CONTINUE - skips current part of the loop, moves to the next part of the loop
# PASS - skips any part of the loop where "pass" appears (used for testing code)

for number in range(1, 11):
    if number == 7:
        print("We're skipping number 7")
        continue
    print("This is the number {}".format(number))
    
for number in range(1, 11):
    if number == 3:
        pass
    else:
        print("The number is {}".format(number))
        
# Calculator v2
on = True

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
    
while(on):
    option = int(input("What you want to do?\n1. Add\n2. Substract\n3. Multiplication\n4. Division\n5. Off to quit\n\nSelected option: "))
    if option == 1:
        add()
    elif option == 2:
        substract()
    elif option == 3:
        multiply()
    elif option == 4:
        divide()
    elif option == 5:
        print("Goodbye! 👋🏽")
        on = False
    else:
        print("That option doesn't exists.")