# Day 13: 30 Days of python programming

# Exercises: Level 1

# Question 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_number = [i for i in numbers if i > 0]
print(positive_number)

# Question 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for rows in list_of_lists for row in rows for number in row]
print(flattened_list)

# Question 3
lst = ",\n".join([str((i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5)) for i in range(11)])
print(f"[{lst}]")

# Question 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new = [[country[0].upper(),country[0][:3].upper(),country[1].upper()] for row in countries for country in row]
print(new)

# Question 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dic_countries = [{"country" : country[0],"city" : country[1]} for row in countries for country in row]

print(dic_countries)

# Question 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_name = [name[0]+" "+name[1] for row in names for name in row]

print(new_name)

# Question 7
slope = lambda y2,y1,x2,x1: (y2-y1/x2-x1) if (x2-x1 != 0) else "Undefine"
y_intercept = lambda y2,y1,x2,x1: y1 - slope(y2,y1,x2,x1) * x1

print("Slope of value is",slope(32,16,8,4))
print("Y intercept of value is",y_intercept(32,16,8,4))