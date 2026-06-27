# Working with variables, data types, and basic input/output operations in Python

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"
favorite_color = input("Enter your favorite color: ")

print()
print("Summary of your input:")
print("Name:", name)
print("Age:", age, "(type:", type(age).__name__ + ")")
print("Height:", height, "m (type:", type(height).__name__ + ")")
print("Student:", is_student, "(type:", type(is_student).__name__ + ")")
print("Favorite color:", favorite_color, "(type:", type(favorite_color).__name__ + ")")

print()
print("Example of basic data types:")
message = "Hello, Python!"
count = 5
price = 12.99
valid = True
print("message =", message, "->", type(message).__name__)
print("count =", count, "->", type(count).__name__)
print("price =", price, "->", type(price).__name__)
print("valid =", valid, "->", type(valid).__name__)
