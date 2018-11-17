import os
from collections import Counter
import pickle

def most_common():
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

    most_common = Counter(word_list).most_common()
    list_common=[]
    for w in most_common:
        list_common.append(w[0])

    with open('stop_words_common.pkl', 'wb') as f:
        pickle.dump(list_common, f, pickle.HIGHEST_PROTOCOL)

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

most_common()