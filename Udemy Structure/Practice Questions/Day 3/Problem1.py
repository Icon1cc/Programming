"""
Create a list of first 10 even numbers using a loop
"""

# x = []
# for numbers in range(1,25):
#     if numbers % 2 == 0:
#         x.append(numbers)
#         if len(x) == 10:
#             break
# print(x)

x = []
num = 2
while len(x) < 10:
    x.append(num)
    num += 2
print(x)