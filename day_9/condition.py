# Day 9: 30 Days of python programming

# Exercises: Level 1

# Question 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive")
elif age > 0 and age < 18:
    year = 18 - age
    print("You need", year, "more years to learn to drive")
else:
    print("Invalid age")

# Question 2
my_age = 22
your_age = int(input("Enter your age: "))

if my_age == your_age:
    print("We were born in same year")
elif your_age > my_age:
    year = your_age - my_age
    if year == 1:
        print("You are year older than me")
    else:    
        print("You are", year, "years older than me")
else:
    year = my_age - your_age
    if year == 1:
        print("You are little smaller than me")
    else:
        print("You are", year, "years smaller than me")

# Question 3
n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))

if n1 > n2:
    print(n1, "Greater than", n2)
elif n1 < n2:
    print(n1, "Smaller than", n2)
else:
    print(n1, "Are Same", n2)

# Exercises: Level 2

# Question 1

marks = int(input("Enter your marks:"))

if marks >= 80 and marks <= 100:
    print("A")
elif marks >= 70 and marks <= 79:
    print("B")
elif marks >= 60 and marks <= 69:
    print("C")
elif marks >= 50 and marks <= 59:
    print("D")
elif marks >= 0 and marks <= 49:
    print("F")
else:
    print("Invalid Marks")

# Question 2
month = input("Enter month:").lower()

if month in ["september", "october",  "november"]:
    print("Autumn")
elif month in ["december", "january", "february"]:
    print("Winter")
elif month in ["march", "april", "may"]:
    print("Spring")
elif month in ["june", "july", "august"]:
    print("summer")
else:
    print("Invalid Month")

# Question 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter Fruit:").lower()

if fruit in fruits:
    print("Fruit already exists")

if fruit not in fruits:
    fruits.append(fruit)
    print("After adding fruit:",fruits)

# Exercises: Level 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Question 1
if "skills" in person.keys():
    pos = len("skills")//2
    print("Middle skill:",person["skills"][pos])

# Question 2
if "skills" in person.keys() and "Python" in person["skills"]:
    print("python is present in skills")

# Question 3
if "JavaScript" in person["skills"]:
    if "React" in person["skills"]:
        print("He is a front end developer")
        if "Node" and "MongoDB" in person["skills"]:
            print("He is a fullstack developer")
    else:
            print("unknown title")
    if "Node" in person["skills"]:
        if "Python" and "MongoDB" in person["skills"]:
            print("He is a backend developer")
    else:
        print("unknown title")

# Question 4
if person["is_marred"] == True and person["country"] == "Finland":
    print(person['first_name'], person['last_name'],"Lives in Finland.","He is married")