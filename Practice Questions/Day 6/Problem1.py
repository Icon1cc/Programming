"""
Function with default argument (e.g., greet someone with default "User")
"""

def greet(name = "user"):
    return "Hello " + name

x = input("Enter the name: ")
if not x.strip():
    result = greet()
else:
    result = greet(x)
print(result)