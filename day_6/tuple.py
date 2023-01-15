# Day 6: 30 Days of python programming

# Exercises: Level 1

# Question 1
tup = ()

# Question 2
sibling = ("Jhon", "Smith", "Ana")

# Question 3
brother = ("Jhon", "Smith")
sister = ("Ana", "Mikasa", "Yor")
sibling = brother + sister

# Question 4
print("I have", len(sibling), "Siblings")

# Question 5
parents = ("Levi", "Hinge")
family_member = parents + sibling
print(family_member) 

# Exercises: Level 2

# Question 1
parent_1, parent_2, *sibling = family_member
print("Unpack parent from family member", parent_1, parent_2)
print("Unpack sibling from family member", sibling)

# Question 2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
Animal_products = ('milk', 'meat', 'butter', 'yoghurt')
food_stuff_tp = fruits + vegetables + Animal_products
print("Food stuff tuple =", food_stuff_tp)

# Question 3
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list =", food_stuff_lt)

# Question 4
pos = food_stuff_lt[len(food_stuff_lt)//2]
food_stuff_lt.remove(pos)
print("After removing middle elemnt =", food_stuff_lt)

# Question 5
del food_stuff_lt[0:3]
del food_stuff_lt[-3:]
print("After removing first 3 and last 3 item =", food_stuff_lt)

# Question 6
food_stuff_tp = tuple(food_stuff_lt)
del food_stuff_tp

# Question 7
print("We delet full list")

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Question 7.1
print("Check weather Estonia in Nodic country:", "Estonia" in nordic_countries)

# Question 7.2
print("Check weather Iceland in Nodic country:", "Iceland" in nordic_countries)