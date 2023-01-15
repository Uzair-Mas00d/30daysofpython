# Day 3: 30 Days of python programming
from cmath import sqrt

# Question 1-3
age = 20
height = 6.2
comp = 2 + 3j

# Question 4
base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
area = 0.5 * base * height
print("The area of the triangle is ", area)

# Question 5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is: ", perimeter)

# Question 6
length = int(input("Enter length of of rectangle: "))
width = int(input("Enter width of of rectangle: "))
area = length * width
print("The area of the rectangle is ", area)
perimeter = 2 * length + width
print("The perimeter of the rectangle is: ", perimeter)

# Question 7
radius = int(input("Enter radius of circle: "))
area = 3.14 * (radius ** 2)
print("Area of circle: ", area)
circum_of_circle = 2 * 3.14 * radius
print("circumference  of circle: ", circum_of_circle)

# Question 8
# y = 2x -2
slope = 2  # beacuse y = mx +c
print("slope is: ", slope)
# y-intercept
x = 0 # in y-intercept x = 0
y = (2 * x) - 2
print("y-intercept is: ", y)
# x-intercept
y = 0 # in x-intercept y = 0
x = (y + 2)/ 2
print("x-intercept is: ", x)

# Question 9
# (2, 2) and (6,10)
y1, y2, x2, x1 = 2, 10, 6, 2 
m = (y2-y1)/(x2-x1)
print("slope is: ", m)
d = sqrt((y2 - y1)**2 + (x2 - x1)**2)
print("Euclidian distance are", d)

# Question 10
print("comparizine of slope of 8 and 9 is: ", slope == m)

# Question 11
# y = x^2 + 6x + 9
x = -3 # y is zero at x = -3
y =  (x ** 2) + (6 * x) + 9
print("value of y is: ", y)

# Question 12
print("length of python is: ",len("python"))
print("length of dragon is: ",len("dragon"))
print("python" <= "dragon")

# Question 13
print("on" in "python" and "on" in "dragon")

# Question 14
print("jargon" in "I hope this course is not full of jargon")

# Question 15
print("on" not in "python" and "on" not in "dragon")

# Question 16
a = len("python")
tofloat = float(a)
print("convert string to float:", tofloat)
tostring = str(tofloat)
print("convert float to string:", tostring)

# Question 17
number = int(input("Enter number: "))
a = number % 2
print("if modolus of number is zero it is even so modulus of number =", a)

# Question 18
div = 7 / 3
Fdiv = 7 // 3
print("floor divison of 7 by 3 in int is:", Fdiv)
print("check if value convert from 2.7 to int: ", div == 2.7)

# Question 19
print("check \"10\" is equal to 10:", "10" == 10)

# Question 20
print("check int(\'9.8\') equal to 10:", int(float('9.8')) == 10)

# Question 21
hour = int(input("Enter hour: "))
rate_per_hour = int(input("Enter rate per hour: "))
earning = hour * rate_per_hour
print("Your weekly earning is: ", earning)

# Question 22
year = int(input("Enter number of year you lived:"))
second = year * 365 * 24 * 60 * 60
print("You have lived for:", second,"seconds")

# Question 23
x = [
    "1 1 1 1 1",
    "2 1 2 4 8",
    "3 1 3 9 27",
    "4 1 4 16 64",
    "5 1 5 25 125"
]
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])