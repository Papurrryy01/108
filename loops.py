# while loops
# a while loops reapets a block of code as long as a condition is true
# be careful - if the condition never becomes False, youll get INFINITE loop

count = 1

while count <= 5:
    print("count is: ", count)
    count += 1 # Assignment operator which adds one untill it equals to 5

print("---------------")

# using break to stop the loop

count = 1

while count<=10: #loops until cout is 10
    if count == 5: #checks when count is 5
        print("Break at 5")
        break #exits loop early
    print(count)
    count += 1

print("---------------")

# using CONTINUE to skip and interact

count = 0 #initializes the count at 0

while count < 5:
    count += 1
    if count == 3: #skips 3
        continue
    print(count)

print("---------------")

# else with while
# the esle block run when the loop condition becomes false(not using break)

count = 1 
while count < 3:
    print(count)
    count += 1
else:
    print("loop is finished!")

# for loops
# a for loop is used for looping over sequence:
#  a list, tuple, dictionary, etc...

# loop through a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits: #for each fruit in the list fruits
    print(fruit)

# loop through a string
for letter in "Hello":
    print(letter)

print("-----------------------------------")

# using range()
# range() generates a sequence of numbers

for x in range(5):
    print(x)

print("-----------------------------------")


# start and end range
for x in range(2, 6):
    print(x)

print("-----------------------------------")


# step (skip numbers)
for x in range(0,10,2):
    print(x)

print("-----------------------------------")

# else in for loop

for x in range(3):
    print(x)
else:    #runs when loop is done
    print("loop is done")

print("-----------------------------------")

# break and Continue in for loops

for x in range(10):
    if x == 5:
        continue #skips 5
    if x == 8:
        break   #stops loops at 8
    print(x)