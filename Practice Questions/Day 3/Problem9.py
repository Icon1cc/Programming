"""
Find the second largest number in a list
"""
mylist = input("Please enter the numbers separated by comma: ")
x = [int(i.strip()) for i in mylist.split(',')]

first = second = float('-inf')

for num in x:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

if second == float('-inf'):
    print("No second largest number found.")
else:
    print(f"The second largest number is: {second}")
