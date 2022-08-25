# List
# Collection of items
# Can contain any / all data types in a single list
# Can contain other collections (lists, dictionaries, tuples) as list items
# Mutable - Items can be added, removed, modified
# Maintain order - Can use index to find an item

fruits = ["Apple", "Banana", "Cucumber"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years) 

# list.append(item) - adds single item to the list
print("Append")
fruits.append("Oranges")
print(fruits)

# list.extend(iterable) - adds another list of items to the list
print("Extend")
fruits.extend(years)
print(fruits)

# list.remove(item) - must be an exact item match
print("Remove")
# fruits.remove("orange") -> throws error since "orange" is not in the list (sensitive)
fruits.remove("Oranges")
print(fruits)

# Remove item from the list by index
# list.pop(item_index)
print("Pop 0")
fruits.pop(0)
print(fruits)

# To remove the last item, if you don't know the size of the list, you can use negative index
print("Pop -1")
fruits.pop(-1)
print(fruits)

# list.sort() - Only works with lists with items of the same type (can combine int and float)
# fruit.sort() -> will error out, since there are multiple types of items
print("Unsorted")
numbers = [1, 42, 403, -24, 0.01, 3.141592]
print(numbers)
print("Sorted")
numbers.sort()
print(numbers)

print("\n========= SEPARATOR =========\n")

fruits2 = ["Apple", "Banana", "Cucumber", "Apple", "Apple"]
years2 = [3, "1998", 2.5, 987, "1994"]

# Check membership in a list
print("apple" in fruits2) # Returns True or False
print("Apple" in fruits2)

# Check membership and number of items with count
# list.count
print("list.count")
print("Apple : {}".format(fruits2.count("Apple")))
print("Apples : {}".format(fruits2.count("Apples")))

# Check membership and the index position
# list.index(item)
print("Where is the Apple? Position {}".format(fruits2.index("Apple")))