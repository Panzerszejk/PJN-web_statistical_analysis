import os
from math import log
from collections import Counter
from sys import getsizeof
import pickle
import time
start_time = time.time()

documents_number = len(os.listdir('posts/'))

documents_with_term = dict()
docs_list = []
for file in os.listdir("posts"):
    if file.endswith(".txt"):
        with open('posts/' + file, 'r') as f:
            temp = f.read()
            for char in '.,():;/?#–-"”“„!…':
                temp = temp.replace(char, ' ')
            temp = temp.replace('‘', '')
            temp = temp.replace('’', '')
            temp = temp.replace('\'', '')
            temp = temp.lower()
            temp_list = temp.split()
            temp_set = set(temp_list)
            for term in temp_set:
                if term not in documents_with_term:
                    documents_with_term[term] = 1
                else:
                    documents_with_term[term] += 1
            docs_list.append([file, temp_list])

idf_term = dict()
term_weight = dict()

for term in documents_with_term:
    idf_term[term] = log(documents_number / documents_with_term[term])
    term_weight[term] = dict()

del documents_with_term

for document in docs_list:
    for term in Counter(document[1]).most_common():
        term_weight[term[0]][document[0]] = term[1] * idf_term[term[0]]

del docs_list
del idf_term

with open('dictionary.pkl', 'wb') as f:
    pickle.dump(term_weight, f, pickle.HIGHEST_PROTOCOL)

#print(term_weight['w'])
print(len(term_weight))
print("--- %s seconds ---" % (time.time() - start_time))
