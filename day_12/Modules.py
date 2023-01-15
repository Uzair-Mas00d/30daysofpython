# Day 12: 30 Days of python programming
from random import randint,sample,shuffle
from string import ascii_lowercase,digits
# Exercises: Level 1

# Question 1
def random_user_id():
    letter = ascii_lowercase
    number = str(digits)
    letter_n_digit = letter + number

    six_letter = ''.join(sample(letter_n_digit,6))
    
    return six_letter

print(random_user_id())

# Question 2
def user_id_gen_by_user():
    letter = ascii_lowercase
    number = str(digits)
    letter_n_digit = letter + number

    length = int(input("Enter length of password "))
    variant = int(input("Enter how many variant of password you needed "))
    
    for i in range(variant):
        six_letter = ''.join(sample(letter_n_digit,length))
        print(six_letter)
    
user_id_gen_by_user()

# Question 3
def rgb_color_gen():
    rgb = []
    for i in range(3):
        rgb.append(randint(0,255))
    return f"rgb{tuple(rgb)}"

print(rgb_color_gen())

# Exercises: Level 2

# Question 1
def list_of_hexa_colors(n):
    lst = []
    letter = ascii_lowercase[0:6]
    number = str(digits)
    letter_n_digit = letter + number
    for i in range(n):
        lst.append("#"+''.join(sample(letter_n_digit,6)))
    
    return lst

print(list_of_hexa_colors(3))

# Question 2
def list_of_rgb_colors(n):
    rgb = []
    for i in range(n):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        rgb.append(f"rgb({r},{g},{b})")
    return rgb

print(list_of_rgb_colors(2))

# Question 3
def generate_colors(color,n):
    color = str(color)
    lst = []
    if color == "hexa":
        letter = ascii_lowercase[0:6]
        number = str(digits)
        letter_n_digit = letter + number
        for i in range(n):
            lst.append("#"+''.join(sample(letter_n_digit,6)))

    if color == "rgb":
        for i in range(n):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            lst.append(f"rgb({r},{g},{b})")

    return lst       
    

print(generate_colors("hexa",2))
print(generate_colors("rgb",3))

# Exercises: Level 3

# Question 1
def shuffle_list(lst):
    lst = sample(lst,len(lst))
    return lst

print(shuffle_list([1,2,3,4,5]))

# Question 2
def ranNumber():
    number = str(digits)

    seven_number = ''.join(sample(number,7))
    return seven_number

print(ranNumber())