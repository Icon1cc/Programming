"""
Format a string to say: "Hello, NAME. You are AGE years old"
"""
name = input("Please enter your name : ")
age = int(input("Please enter your age: "))
print("Hello, {}. you are {} years old ".format(name,age))