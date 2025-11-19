# lists are used to store MULTIPLE items in a single variable.

my_list = [10,20,30,40,50]
print(my_list)

mixed_list = [10, "Hello", True, 25.5]
print(mixed_list)

# accessing list items by their INDEX number
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print(fruits[0])  # First item
print(fruits[2])  # Third item
print(fruits[-1]) # Last item

# You ncan also use NGATIVE INDEXING to access items from the end of the list
print(fruits[-1]) # Last item
print(fruits[-2]) # Second last item
print(fruits[-3]) # Third last item

#  MODIFY the list
fruits[1] = "Blueberry"
print(fruits) 

# ADD items to the list
fruits.append("Fig")  # Adds to the end
print(fruits)
fruits.insert(2, "Cantaloupe")  # Inserts at index 2
print(fruits)

# REMOVE items from the list
fruits.remove("Date")  # Removes by value
print(fruits)
del fruits[0]         # Removes by index
print(fruits)
fruits.pop()          # Removes the last item
print(fruits)

#  check if an item exists in the list
if "Cherry" in fruits:
    print("Cherry is in the list!")
else:
    print("Cherry is not in the list.")

# check the length of the list
print("Number of fruits:", len(fruits))
 