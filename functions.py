# it is a block of code which only runs when is called

# simple function without parameters
def my_function(): #this is the function
    print("this is my function") #this line runs when function is called

my_function() # calling the functon


def other_function():
    print("This is my other function")
other_function()

# function with parameters
def print_full_name(fname, last_name):
    print(f"My name is: {fname} {last_name} ")
ful_name = print_full_name("Carlos", "Vera")

def full_name(fname,lname):
    return f"{fname} {lname}"
name = full_name("Cory", "canelo")
print(name)

# //// mini challenge 

def subtraction(a, b):
    return a - b

# print the result
result = subtraction(10, 3)
print("subtraction result:", result)