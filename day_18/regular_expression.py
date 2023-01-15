# Day 18: 30 Days of python programming
import re
from collections import Counter
# Exercises: Level 1

# Question 1
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love " \
            "something which can give you all the capabilities to develop an application what else can you love. "

def most_common_word(text):
    words = re.findall(r'[a-zA-Z]*', text)

    word_counts = Counter(words)
    most_common = word_counts.most_common()

    return most_common[1:]

print(most_common_word(paragraph))

# Question 2
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 " \
            "in the negative direction, 0 at origin, 4 and 8 in the positive direction."

point = list(map(int, re.findall(r"-[\d]|[\d]+", text)))
point.sort()
difference = point[-1] - point[0]
print("Difference between two furthest point is",difference)

# Exercises: Level 2

# Question 1
def is_valid_variable(strings):
    if re.search(r"^[a-zA-z_]*$", strings):
        return True
    else:
        return False
print(is_valid_variable('_name'))
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))

# Exercises: Level 3

# Question 1
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(strings):
    text = re.sub(r'[^A-Za-z0-9" "]+', "", strings) 
    return text

print(clean_text(sentence))
print(most_common_word(clean_text(sentence))[0:5:2])