"""
Write a function to perform the binary to decimal conversion
"""

def binToDecimal(n):
    s = n[::-1]
    res = 0
    power = 0
    for items in s:
        res = res + int(items) * (2 ** power)
        power += 1
    return res

n = input("Enter the binary number: ")
result = binToDecimal(n)
print("The decimal result is:", result)