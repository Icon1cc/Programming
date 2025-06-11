"""
Create a dictionary for a student with name, age, grade
"""
Name = input("Please enter the name: ")
Age = int(input("Please enter the age: "))
Grade = float(input("Please enter the grade: "))

my_dict_student = {"Name": Name, "Age": Age, "Grade": Grade}

print("The dictionary is created and the name of the student is {}, with age {}, and grade {}".format(Name, Age, Grade))