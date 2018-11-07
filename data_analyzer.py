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

print(len(word_list))

labels = []
sizes = []
suma = 0
for i, element in enumerate(Counter(word_list).most_common()):
    if i < 19:
        labels.append(element[0])
        sizes.append(element[1])
    else:
        suma += element[1]
labels.append('INNE')
sizes.append(suma)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
