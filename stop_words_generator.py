import os
from collections import Counter
import pickle
import math
from operator import itemgetter
import statistics

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


def new_method():
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
    words_count = len(word_list)
    word_counted = Counter(word_list).most_common()
    names, vals = map(list, zip(*word_counted))
    word_mean = statistics.mean(vals)
    measures = []
    for i, name in enumerate(names):
        q = (vals[i] - 1) / words_count
        measures.append((vals[i] / words_count,
                         math.sqrt(  ((vals[i] - q * words_count) * (((q+1) - word_mean)**2) +
                                     (words_count - (vals[i] - q * words_count)) * ((q - word_mean)**2) / (words_count - 1)))))
    means, sdvs = map(list, zip(*measures))
    maxavg = max(means)
    minavg = min(means)
    maxsdv = max(sdvs)
    minsdv = min(sdvs)
    result = dict()
    for i, name in enumerate(names):
        result[name] = ((means[i] - minavg)/(maxavg - minavg)) + (1 - ((sdvs[i] - minsdv) / (maxsdv - minsdv)))
    sorted_result = []
    for klucz, item in sorted(result.items(), key=itemgetter(1), reverse=True):
        sorted_result.append(klucz)
        
    with open('stop_words_new_common.pkl', 'wb') as f:
        pickle.dump(sorted_result, f, pickle.HIGHEST_PROTOCOL)


# most_common()
new_method()
