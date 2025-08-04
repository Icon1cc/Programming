"""
Return the absolute difference from 17 (double it if input > 17)
"""

num = float(input("Please enter the number : "))
if num > 17:
    result = (num - 17) * 2
else:
    result = 17 - num
print(f"Absolute from 17 is :{result}")