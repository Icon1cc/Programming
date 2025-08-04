"""
Return n copies of the first 2 letters of a string
"""
def myfunc(x, n):
    return x[:2] * n

x = input("Enter the string: ")
n = int(input("Enter the number of copies: "))
result = myfunc(x, n)
print(result)
