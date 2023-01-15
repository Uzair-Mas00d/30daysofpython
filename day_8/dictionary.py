# Day 8: 30 Days of python programming

# Question 1
dog = {}

# Question 2
dog["name"] = "light"
dog["color"] = "white"
dog["breed"] = "Bulldog"
dog["leg"] = "BowedLeg"
dog["age"] = 10
print(dog)

# Question 3
student = {
    'first_name':'Jhon',
    'last_name':'Smith',
    "gender":"Male",
    'age':420,
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Usa',
    "city":"LA",
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Grove street',
        'zipcode':'03310'
    }
}
print(student)

# Question 4
print("Length of Student dic is",len(student))

# Question 5
print("value of skill",student.get('skills'))
print("Type of skill",type(student['skills']))

# Question 6
student["skills"].append("Machine learning")
print(student.get("skills"))

# Question 7
print("Dic keys",student.keys())

# Question 8
print("Dic keys",student.values())

# Question 9
print("Change dic to list of tuple", student.items())

# Question 10
del student["city"]
print("After deleting item",student)

# Question 11
del dog