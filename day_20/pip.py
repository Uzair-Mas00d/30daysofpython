# Day 20: 30 Days of python programming
import requests
from collections import Counter , defaultdict
import numpy
import bs4
# Exercises: Level 1

# Question 1 
def find_most_common_words():
    romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
    response = requests.get(romeo_and_juliet)

    response = str(response.text)
    sentence = response.split()
    word = Counter(sentence)
    words = word.most_common(10)
    return words

print(find_most_common_words())

# Question 2.1

def cat_weight():
    cats_api = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(cats_api)
    cat = response.json()

    lst = []
    for data in cat:
        lst.append((int(data["weight"]["metric"][0])+int(data["weight"]["metric"][-1]))/2)

    mean = numpy.mean(lst)
    median = numpy.median(lst)
    std_dev = numpy.std(lst)
    mins = min(lst)
    maxs = max(lst)

    print("Standard Deviation: %0.2f" % std_dev)
    print("Minimum:", mins)
    print("Maximum:", maxs)
    print("Median:", median)
    print("Mean: %0.2f" % mean)

cat_weight()

# Question 2.2
def cat_life_span():
    cats_api = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(cats_api)
    cat = response.json()
    lst = []
    for data in cat:
        lst.append((int(data["life_span"][0])+int(data["life_span"][-1]))/2)

    mean = numpy.mean(lst)
    median = numpy.median(lst)
    std_dev = numpy.std(lst)
    mins = min(lst)
    maxs = max(lst)
    
    print("Standard Deviation: %0.2f" % std_dev)
    print("Minimum:", mins)
    print("Maximum:", maxs)
    print("Median:", median)
    print("Mean: %0.2f" % mean)

cat_life_span()

# Question 2.3
def frequency_table():
    cats_api = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(cats_api)
    cat = response.json()

    lst = []
    for data in cat:
        lst.append((data["country_codes"],data["name"]))

    print(lst)

frequency_table()

# Question 3 
# country api link of 3rd question didn't work.

# Question 4
def read_content():
    contents = requests.get("https://archive.ics.uci.edu/ml/datasets.php")
    doc = bs4.BeautifulSoup(contents.content)

    print(doc.prettify())

read_content()