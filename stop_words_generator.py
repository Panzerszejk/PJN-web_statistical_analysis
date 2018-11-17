import os
from collections import Counter

def most_common(num):
    all_text = ""
    for file in os.listdir("posts"):
        if file.endswith(".txt"):
            with open('posts/' + file, 'r') as f:
                all_text += f.read()

    for char in '.,():;/?#–-"”“„!…':
        all_text = all_text.replace(char, ' ')
    all_text = all_text.replace('‘', '')
    all_text = all_text.replace('’', '')
    all_text = all_text.replace('\'', '')
    all_text = all_text.lower()
    word_list = all_text.split()

    return Counter(word_list).most_common(num)

def new_method(num):
    all_text = ""
    N = 0
    avg_x = dict()
    for file in os.listdir("posts"):
        if file.endswith(".txt"):
            with open('posts/' + file, 'r') as f:
                all_text += f.read()
                N += 1

    for char in '.,():;/?#–-"”“„!…':
        all_text = all_text.replace(char, ' ')
    all_text = all_text.replace('‘', '')
    all_text = all_text.replace('’', '')
    all_text = all_text.replace('\'', '')
    all_text = all_text.lower()
    word_list = all_text.split()

    words_dict = Counter()

    for word in word_list:
        words_dict[word] += 1

    for key,value in words_dict.items():
        avg_x[key] = value/N
