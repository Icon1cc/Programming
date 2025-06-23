"""
Write a program to print pyramid pattern.
Input: 3
Output:
  *
 ***
*****
"""

x = int(input("Enter a number greater than 0: "))

for i in range(x):
    for j in range(x - i - 1):  # spaces
        print(" ", end="")
    for k in range(2 * i + 1):  # stars
        print("*", end="")
    print()
