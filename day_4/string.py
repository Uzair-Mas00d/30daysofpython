# Day 4: 30 Days of python programming

# Question 1
a, b, c, d = "Thirty", "Days", "Of", "Python"
print(a + b + c + d)

# Question 2
a, b, c = "Coding", "For", "All"
print(a + b + c)

# Question 3
company = "Coding For All"

# Question 4
print(company)

# Question 5
print(company,"and length of company:",len(company))

# Question 6
print(company.upper())

# Question 7
print(company.lower())

# Question 8
print(company.capitalize())
print(company.swapcase())
print(company.title())

# Question 9
print(company[1:])

# Question 10
print("Coding" in company) # return true if Coding in company

# Question 11
print(company.replace("Coding","Python"))

# Question 12
print("Python for Everyone".replace("Everyone", "All"))

# Question 13
print("Coding For All".split(" "))

# Question 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# Question 15
a = "Coding For All"
print("At index zero it is:", a[0])

# Question 16
print("At last index it is:", a[-1])

# Question 17
print("At index 10 it is:", a[10],"space character")

# Question 18
b = 'Python For Everyone'
print(b[0].capitalize()+b[7].capitalize()+b[11].capitalize())

# Question 19
c = "Coding For All"
print(c[0].upper() + c[7].upper() + c[11].upper())

# Question 20
print("First occurance C is at index zero:",c[0])

# Question 21
print("First occurance F is at index seven:",c[7])

# Question 22
print("Last l is at position of:",c.rfind("l"))

# Question 23
sentence = "You cannot end a sentence with because because because is a conjunction"
print("First occurance \'beacuse\' is at position of:",sentence.find("because"))

# Question 24
print("Last occurance \'beacuse\' is at position of:",sentence.rfind("because"))

# Question 25
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[0:30], sentence[55:])
print(sentence.replace("because",""))

# Question 24 and 26 are same
# Question 25 and 27 are same

# Question 28
a = "Coding For All" 
sub_string = "Coding"
print(sub_string in a[0:6],"string start wit sub string")

# Question 29
print(sub_string in a[10:],"string doesn\'t end with sub string")

# Question 30
print("   Coding For All      ".strip())

# Question 31
challenge = '30DaysOfPython'
print('30DaysOfPython return',challenge.isidentifier())
challenge = 'thirty_days_of_python'
print('thirty_days_of_python return',challenge.isidentifier())

# Question 32
lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(lib[0].join("# "),lib[1].join("# "), lib[2].join("# "),lib[3].join("# "),lib[4].join("# "))

# Question 33
print("I am enjoying this challenge. \nI just wonder what is next.")

# Question 34
print("Name\t\tAge\tCountry\t  City")
print("Asabeneh\t250\tFinland\t  Helsinki")

# Question 35
radius = 10
area = int(3.14 * radius ** 2)
print("The area of a circle with radius {} is {} meters square.".format(radius,area))
print("The area of a circle with radius %d is %d meters square." %(radius,area))
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Question 36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
