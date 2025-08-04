"""
Write a function to convert a non-negative number to binary number
"""

def decToBinary(n):

    if n == 0:
        return "0"

    res = " "

    while n > 0:
        res = res + str(n % 2)
        n = n // 2

    return res[::-1]

n = int(input("Enter a positive number: "))
result = decToBinary(n)
print("The converted number is:",result)

# Direct method

# def decToBin(n):
#     res = bin(n)
#     return res[2::]
