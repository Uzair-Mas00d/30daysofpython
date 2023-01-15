# Day 19: 30 Days of python programming
import json
import csv
from collections import Counter
import re
import stop_word
# Exercises: Level 1

# Question 1 
def count_lines(fname):
    lines = 0
    with open(fname) as f:
        for i in f:
             lines += 1
        return lines

def count_words(fname):
    with open(fname) as f:
        data = f.read()
        words = data.split()
    return len(words)

# 1.a
print("Number of lines is obama speech",count_lines("obama_speech.txt"))
print("Number of word in obama speech",count_words("obama_speech.txt"))

#1.b
print("Number of lines in michallel speech",count_lines("michalle_speech.txt"))
print("Number o word in michallel speech",count_words("michalle_speech.txt"))

#1.c
print("Number of lines in donaland speech",count_lines("donalad_speech.txt"))
print("Number of word in donaland speech",count_words("donalad_speech.txt"))

# Question 2
def most_spoken_languague(fname,value):
    with open(fname,"r", encoding='utf-8') as f:
        data = json.load(f)
    
    lst = []
    count = {}
    output = []
    for country in data:
        for language in country["languages"]:
            lst.append(language)

    for language in lst:
        if not language in count:
            count[language] = 1
        else:
            count[language] +=1
    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True)) 
    for i in list((count.items()))[:value]:
        output.append(i)
    return [(sub[1], sub[0]) for sub in output]
   
print( most_spoken_languague("country_data.json",3))

# Question 3
def most_populated_countries(fname,value):
    with open(fname,"r", encoding='utf-8') as f:
        datas= json.load(f)
    lst = []
    for data in datas:
        lst.append({"country":data["name"],"population":data["population"]})
    lst.sort(key=lambda x: x["population"], reverse=True)
    return lst[:value]

print(most_populated_countries("country_data.json",3))
print()
# Exercises: Level 2

# Question 4
def email_address(fname):
    regx = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    with open(fname) as f:
        data = f.read()
    recived = re.findall(regx,data)

    return (recived)

print(email_address("email_exchange.txt"))

# Question 5
def find_most_common_words(fname,value):
    output = []
    with open(fname) as f:
        sentences = f.read()
    sentence = sentences.split()
    word = Counter(sentence)
    words = word.most_common(value)
    return [(sub[1], sub[0]) for sub in words]

# Question 6
print(find_most_common_words("obama_speech.txt",10))
print(find_most_common_words("michalle_speech.txt",10))
print(find_most_common_words("donalad_speech.txt",10))
print(find_most_common_words("melina_speech.txt",10))  
print()
# Question 7
def clean_text(fname):
    with open(fname) as f:
        data = f.read()
    text = re.sub(r'[^A-Za-z" "]+', "", data) 
    return text

clean_text1 = clean_text("melina_speech.txt").lower()
clean_text2 = clean_text("michalle_speech.txt").lower()

def reomve_stop_word(text):
    texts = text.split()
    lst = stop_word.stop_words()
    for word1 in lst:
        for word2 in texts:
            if word1 == word2:
                texts.remove(word1)
    return(texts)
    
clean_stop_word_text1 = reomve_stop_word(clean_text1)
clean_stop_word_text2 = reomve_stop_word(clean_text2)

def check_text_similarity(text1,text2):
    score = 0
    lst = []
    for i in text1:
        if i in text2:
            lst.append(i)
            score +=1
    print("Similar word between to files is:",lst)
    return score
print("Similirty between two file is:",check_text_similarity(clean_stop_word_text1,clean_stop_word_text2))

# Question 8
print(find_most_common_words("romeo_and_juliet.txt",10))

# Question 9
python = 0
javascript = 0
java = 0
with open("hacker_news.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        if "python" in str(row).lower():
            python +=1
        if "javascript" in str(row).lower():
            javascript += 1
        if re.search(r"[Jj]ava",str(row)):
            java += 1
print(python,javascript,java)
