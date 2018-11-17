from django.shortcuts import render
from .functions import stop_words_generator
import pickle
import operator


def index(request):
    error = []
    result_result = []
    if request.GET.get('submit'):
        if request.GET.get('search') == "":
            error.append("Empty sring")
        else:
            term_weights = pickle.load(open("./../dictionary.pkl", "rb"))
            words = request.GET.get('search').split()

            if request.GET.get('stop') == 'on':
                print("stop")
                #number = request.GET.get('number')
                number = 20
                stop_list = stop_words_generator.most_common(number)
                for word in words:
                    for stop in stop_list:
                        if word == stop:
                            words.remove(word)
                            error.append("W frazie wystąpiło stop słowo: "+word)

            dict_list = []
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
                result_result.append((klucz, '{:.3f}'.format(round(item, 3))))

    return render(request, 'index.html', {'error': error, 'pages': result_result})
