"""
Given a list of integers and a target number, print all unique pairs that add up to the target.

Example: nums = [2, 4, 3, 5, 7, 8, 9] and target = 10
Output: (2, 8), (3, 7)
"""

new_list = list(map(int, input("Enter the numbers separated by commas: ").split(",")))
num = int(input("Enter the target number: "))

seen = set()
printed = set()

for item in new_list:
    complement = num - item
    if complement in seen and (min(item, complement), max(item, complement)) not in printed:
        print(complement, item)
        printed.add((min(item, complement), max(item, complement)))
    seen.add(item)
