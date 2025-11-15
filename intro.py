print("Hello World from Python!")
print(2)
print(2+2)
print(True)

# create a variable
name = "Carlos"
age = 23
middle_name = "Antonio"
last_name = "Vera"
found = False
print(name)
print(age)

# concatenation
print("My name is " + name + " " + middle_name + " " + last_name + " and I am " + str(age) + " years old.")
print("Did he find it? " + str(found))

# Storytelling
story = "Once upon a time, there was a young programmer named " + name + ". "
story += "He was " + str(age) + " years old and was an immigrant from Cuba. "
story += "Every day, he would code for hours, dreaming of creating amazing applications. "
story += "One day, he decided to embark on a journey to learn more about programming. "
story += "With determination and passion, " + name + " set out to conquer the world of code."
print(story)

# F format
# f""    F"""

print(f"My name is {name} {middle_name} {last_name} and I am {age} years old.")
print(f"""
Carlos
    is learning Python.
        He is {age} years old.
""")

# type function() function helps us to know the type of a variable
print(type(name))
print(type(age))
print(type(found))

# casting
# helps us to convert one data type to another
print(20+int("20"))
print(20+age)

# input method
# is going to allow us to get data from the user
# print(input("What is your name? "))
# print(type(input("What is your name? ")))

# new_age = int(input("How old are you? "))
# print(new_age + age)
# print(str(age) + new_age)

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"The sum of {x} and {y} is {x + y}")