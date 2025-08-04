"""
Write a program to find the LCM of two numbers.
"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = max(a, b)
while result <= a*b:
    if result % a == 0 and result % b == 0:
        break
    result += 1
print(f"LCM of {a} and {b} is {result}")


"""
Another usage:

gcd = math.gcd(a, b)
lcm = (a*b) / gcd
print(f"LCM of {a} and {b} is {lcm}")
"""