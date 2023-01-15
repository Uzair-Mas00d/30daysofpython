# Day 1 - 30DaysOfPython Challenge
from cmath import sqrt

#Question 2
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

#Question 4
print(type(10))                                   # Int
print(type(9.8))                                  # Float
print(type(3.14))                                 # Float
print(type(4 - 4j))                               # Complex number
print(type(['Asabeneh', 'Python', 'Finland']))    # Dictionary
print(type("jhon"))                               # String
print(type("smith"))                              # String
print(type("USA"))                                # String
print()
# Exercise 3
# Question 1
print(type(10))                   # Int
print(type(3.14))                 # Float
print(type(1 + 3j))               # Complex number
print(type('Asabeneh'))           # String
print(type([1, 2, 3]))            # List
print(type({'name':'Asabeneh'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))     # Set
print(type((9.8, 3.14, 2.7)))     # Tuple
print()

# Question 2
d = sqrt((10 - 2)**2 + (8 - 3)**2)
print("Euclidian distance between (2, 3) and (10, 8) are", d)