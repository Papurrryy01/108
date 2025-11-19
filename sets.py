# Sets are UNORDERED, UNDEFINED, and have NO DIPLICATE

fruits = {"apple", "banana", "cherry"}
print(fruits)

fruits = {"apple", "banana", "apple"}
print(fruits)

# check if item exist
print("banana" in fruits)

# add item
fruits.add("orange")
print(fruits)

# add multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

# remove item
fruits.remove("banana")
print(fruits)

# if you are not sure in item exists, use discard() to avoid errors
fruits.discard("papaya")

# set operations (like math)
set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2)) #combines boths with no duplicate
print(set1.intersection(set2)) # common elements (returns duplicates)
print(set1.difference(set2)) # non duplicates in set1