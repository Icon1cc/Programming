"""
Take a name and age and save it as JSON
"""

import json

name = input("Enter your Name: ")
age = input("Enter your age: ")

data = {
    "name": name,
    "age": age
}

with open("userdata.json","w") as f:
    json.dump(data, f, indent = 4)

print("Data save to JSON")