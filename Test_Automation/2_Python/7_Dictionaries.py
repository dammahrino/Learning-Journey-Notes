# Dictionaries
# Python Data Collection that stores the data in key-value pairs
# Mutable structure - Can be changes
# Order - Maintain order of entry as of Python 3.7
# Syntax - Curly braces containes keys and values, separated by a colon :
# Keys need to be unique and immutable

stuff = {"Food": 15, "Energy": 100, "Enemies": 33}
print(stuff)

# Retrieve the value of a key
# dictionary.get(key)
print("Food value: {}".format(stuff.get("Food")))

# dictionary.items()
# Takes the name of the dictionary and outputs the key-value pairs.
print("dictionary.items()")
print(stuff.items()) # -> Ordered

# dictionary.keys()
# Outputs all the keys of the dictionary
print("dictionary.keys()")
print(stuff.keys())

# dictionary.popitem() 
# Removes the last item in the dictionary
print(stuff.popitem())
print(stuff)

# dictionary.setdefault()
# What the value is of a key that is in the dictionary,
# but more importantly allows us to set the value of a key
# that it's not in the dictionary
print("\ndictionary.setdefault(value)")
print(stuff)
print(stuff.setdefault("Food"))
print(stuff.setdefault("Friends", 42))
print(stuff)

print("\n========= SEPARATOR =========\n")

new_items = {"Rocks": 4, "Arrows": 100}
# dictionary.update(dictionary)
# Updates the information of a dictionary with another dictionary
print("dictionary.update(dictionary)")
print(stuff)
print(new_items)
stuff.update(new_items)
print(stuff)

# Update existing items in a dictionary
new_items = {"Rocks": 2, "Arrows": 0}
stuff.update(new_items)
print(stuff)

# Update can add new items as well
new_items2 = {"Food": 24, "Frienship": 9000}
stuff.update(new_items2)
print(stuff)

# Update keys directly with update
stuff.update(Food = 300)
print(stuff)

