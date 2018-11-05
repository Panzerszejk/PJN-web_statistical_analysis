import os
import matplotlib.pyplot as plt
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


labels = []
sizes = []
for i, element in enumerate(Counter(word_list).most_common()):
    if i < 20:
        labels.append(element[0])
        sizes.append(element[1])

#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.axis('equal')
plt.show()
