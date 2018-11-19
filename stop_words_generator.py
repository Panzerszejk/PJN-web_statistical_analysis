import os
from collections import Counter
import pickle
import math

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
    list_common = []
    for w in most_common:
        list_common.append(w[0])

    with open('stop_words_common.pkl', 'wb') as f:
        pickle.dump(list_common, f, pickle.HIGHEST_PROTOCOL)

def new_method(num):
    all_text = ""
    N = 0
    stop_words = dict()
    measures = dict()
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

    avg = 0
    std_dev = 0
    for key,value in words_dict.items():
        avg = value/N
        q = (value - 1) / N
        xqN = value - q * N
        std_dev = math.sqrt((xqN*(((q+1)-avg)**2) + (N - xqN)*((q-avg)**2))/(N-1))
        measures[key] = (avg, std_dev)

    min_avg = avg
    max_avg = min_avg
    min_dev = std_dev
    max_dev = min_dev

    for key, value in measures.items():
        if value[0] < min_avg:
            min_avg = value[0]
        else:
            if value[0] > max_avg:
                max_avg=value[0]

        if value[1] < min_dev:
            min_dev = value[1]
        else:
            if value[1] > max_dev:
                max_dev=value[1]


    for key, value in measures.items():
        stop_words[key]=(value[0]-min_avg)/max_avg + 1-(value[1]-min_dev)/max_dev



most_common()