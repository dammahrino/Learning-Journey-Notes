# Comparison operators
# <, >, <=, >=, ==, !=
print(1 < 1)
print(1 > 1)
print(1 <= 1)
print(1 >= 1)
print(1 == 1)
print(1 != 1)

# if, elif, else

name = input("What is your name? ")

if name == "Daniel":
    print("Hi Daniel!")    
elif name == "Alberto":
    print("Hi Alberto!")
else:
    print("Hello stranger ~.")
    
print("Thanks for entering your name {}.".format(name))
