import os
import matplotlib.pyplot as plt
import numpy as np
import bisect
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

words_dict = Counter()
word_count = 0
word_unique_count = 0
plot_count_list =[0]

for word in word_list:
    word_count += 1

    words_dict[word] += 1

    if word_count%50000 == 0:
        word_unique_count = len(words_dict)
        plot_count_list.append(word_unique_count)

print("Words growth")


print("Words total: "+str(word_count)+' unique: '+str(word_unique_count))
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.axis('equal')
plt.show()

plot_count_labels = np.arange(0,word_count,50000)
plt.plot(plot_count_labels,plot_count_list, 'ro')
plt.show()