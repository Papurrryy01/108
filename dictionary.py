# Dictionary store data in key-value pairs {}

students = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
print(students)

# accessing values by their keys
print(students["name"])  # Alice
print(students.get("age"))  # 21

#  add a new key-value pair
students["graduation_year"] = 2023
print(students)

# modify an existing value
students["age"] = 23
print(students)

# removes item
students.pop("major")
print(students)

#  check if key exists
if "height" in students:
    print("Key 'name' is in the dictionary")

# nested dictionary
students = {
    "student1": {"name": "Leo", "age":"20"}, 
    "student2": {"name": "Alex", "age":"30"}
}
print(students["student1"]["name"]) 