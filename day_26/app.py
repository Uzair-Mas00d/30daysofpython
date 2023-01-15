from flask import Flask, render_template,request,redirect, url_for
import os
from string import ascii_lowercase
from collections import Counter
import re

app = Flask(__name__)

def clean_texts(text):
    text = re.sub(r'[^A-Za-z0-9" "]+', "", text) 
    return text

def letter_freq(text):
    lst = []
    letter = ascii_lowercase
    for i in letter:
        letter_freq = text.count(i)
        lst.append((i,letter_freq))
    return lst

def total_letter(text):
    count = 0;  
    for i in range(0, len(text)):  
        if(text[i] != ' '):  
            count = count + 1;  
    return count

def word_freq(text):
    lst = []
    unique_words = []
    words = text.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
        else:
            pass
    for i in unique_words:
        word_freq = words.count(i)
        lst.append((i,word_freq))
    return lst

def total_word(text):
    word = text.split()
    words = len(word)
    return words

def find_most_common_words(text):
    sentence = text.split()
    word = Counter(sentence)
    words = word.most_common(1)
    return words

@app.route("/")
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    content = contents.lower()
    clean_text = clean_texts(content)
    letters_freq = letter_freq(clean_text)
    words_freq = word_freq(clean_text)
    len_words = total_word(clean_text)
    len_letter = total_letter(clean_text)
    most_used_word = find_most_common_words(clean_text)

    return render_template('result.html',clean_text=clean_text, letters_freq=letters_freq,words_freq=words_freq,len_words=len_words,len_letter=len_letter,
                            most_used_word=most_used_word)

@app.route('/post',methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        global contents
        contents = request.form['content']
        return redirect(url_for('result'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)