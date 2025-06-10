"""
Count the number 4 in a list
"""

x = input("Please enter the numbers separated by commas : ")
lst = [int(i.strip()) for i in x.split(',')]
count = 0

for item in lst:
    if item == 4:
        count += 1
print(count)