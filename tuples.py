# Tuples are like lists - they can store multiple items
# BUT!! tuples are IMUTABLE (you cant change them after creation)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# accessing items
print(my_tuple[0])
print(my_tuple[2])

# check if item exist
if "cherry" in my_tuple:
    print("yes it is")

# length of tuple
print(len(my_tuple))

# single item tuple
#  you mnust add a comma at the to recognize as a tuple
single = ("apple")
print(type(single)) #this is just a string
correct = ("apple",)
print(type(correct))

#  nested tuple
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
combine = (tuple1, tuple2)
print(combine)