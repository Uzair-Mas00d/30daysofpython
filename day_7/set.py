# Day 7: 30 Days of python programming

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Question 1
print("Length of it copmanies:",len(it_companies))

# Question 2
it_companies.add('Twitter')
print(it_companies)

# Question 3
it_companies.update(["Nvidia", "OpenAi"])
print(it_companies)

# Question 4
it_companies.pop()
print(it_companies)

# Question 5
# remove function remove specific value from set but if value doesn't exist it thrown error
# discard function remove specific calue from set but if value doesn;t exist it return original set

# Exercises: Level 2
# Question 1
C = A.union(B)
print("Union of A and B is",C)

# Question 2
C = A.intersection(B)
print("Intesection of A and B is",C)

# Question 3
print("Checking A is subset of B",A.issubset(B))

# Question 4
print("Checking A is disjoint of B",A.isdisjoint(B))

# Question 5
C = A.union(B)
print("Union of A and B is",C)
D = B.union(A)
print("Union of B and A is",D)

# Question 6
print("Symmetic DIfferece of A and B is",A.symmetric_difference(B))

# Question 7
del A , B , it_companies

# Exercises: Level 3

# Question 1
set_age = set(age)
print("Comparing len of list and set age",len(age) >= len(set_age))

# Question 2
# string is sequnce of character. reption is allowed
# list is collection of data type in order manner. we can modifie list as we want.reption is allowed
# tuple is collection of data type in order manner. we cannot modifies tuple.reption is allowed
# set is collection of data type in unorder manner. we can modifies set.reption is not allowed

# Question 3
sentence = "I am a teacher and I love to inspire and teach people"
print("After using split function",sentence.split(" "))
a = set(sentence)
print("Number of unique word use in a sentence",a)