import os
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


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

print("File read complete")

labels = []
sizes = []
for i, element in enumerate(Counter(word_list).most_common()):
    if i < 20:
        labels.append(element[0])
        sizes.append(element[1])

print("Most common complete")

words_used = []
isthere = True
word_count =0
word_unique_count = 0
plot_count_list =[]

for word in word_list:
    isthere = False
    word_count += 1
    for element in words_used:
        if element == word:
            isthere = True
            break

    if not isthere:
        word_unique_count += 1
        words_used.append(word)

    if word_count % 10000:
       plot_count_list.append(word_unique_count)


print("Unique word complete w_count: "+str(word_count)+' unique_count: '+str(word_unique_count))
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.axis('equal')
plt.show()

plot_count_labels = np.arange(0,word_count,1000)

plt.plot(plot_count_list, plot_count_labels, 'ro')