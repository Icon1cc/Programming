"""
Write a program to build a calculator performing addition subtraction or multiplication of two numbers.
"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("""
Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
else:
    print("Choose a valid option")
