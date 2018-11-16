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
