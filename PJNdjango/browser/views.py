from django.shortcuts import render
import pickle
import operator


def index(request):
    error = []
    result_result = []
    if request.GET.get('submit'):
        if request.GET.get('search') == "":
            error = "Nie wpisano frazy w wyszukiwarkę"
        else:
            words = set(request.GET.get('search').lower().split())

            if request.GET.get('stopwords') != 'Stop słowa włączone':
                stop_list = pickle.load(open("./../stop_words_common.pkl", "rb"))
                num = 20
                if request.GET.get('stopwordscount'):
                    num = int(request.GET.get('stopwordscount'))
                for w in words.copy():
                    if w in stop_list[0:num]:
                        error = "W frazie znajduje się stop słowo"
                        words.remove(w)

            if len(words) == 0:
                error = "W szukanej frazie znajdują się same stop słowa"
            else:
                dict_list = []
                term_weights = dict()
                if request.GET.get('lemmatization') == 'on':
                    term_weights = pickle.load(open("./../dictionary_lemmas.pkl", "rb"))
                    lemmas = dict()
                    with open('./../lematy.txt', 'r') as f:
                        for line in f:
                            lemmas[line.split('|')[0].lower()] = line.split('|')[1].lower()
                    words_c = words.copy()
                    words.clear()
                    for element in words_c:
                        if element in lemmas:
                            words.add(lemmas[element])
                        else:
                            words.add(element)
                else:
                    term_weights = pickle.load(open("./../dictionary.pkl", "rb"))

                for word in words:
                    dict_list.append(term_weights[word])
                temp = dict_list.pop()
                for files in dict_list:
                    temp = temp & files.keys()
                result = dict()
                for file in temp:
                    result[file] = 0
                    for word in words:
                        result[file] += term_weights[word][file]
                result_result = []
                for klucz, item in sorted(result.items(), key=operator.itemgetter(1), reverse=True):
                    result_result.append((klucz.replace(".txt", ""), '{:.3f}'.format(round(item, 3))))

    return render(request, 'index.html', {'error': error, 'pages': result_result})

def result(request):
    nazwa = request.GET.get('name')
    nazwa += '.txt'
    tekst = ""
    with open('./../posts/'+nazwa, 'r') as f:
        for line in f:
            tekst += line+"</br>"

    return render(request, 'result.html', {'tekst': tekst})
