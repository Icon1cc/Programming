"""
Write a function that accepts **kwargs and prints all key-value pairs
"""
def myfunc(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

mylist = {}

while True:
    key = input("Enter a key or stop to finish: ")
    if key.lower() == 'stop':
        break
    value = input("Enter the value for the key: ")
    mylist[key] = value

myfunc(**mylist)
