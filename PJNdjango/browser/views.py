from django.shortcuts import render
import pickle
import operator


def index(request):
    error = None
    result_result = []
    if request.GET.get('submit'):
        if request.GET.get('search') == "":
            error = "Empty sring"
        else:
            term_weights = pickle.load(open("./../dictionary.pkl", "rb"))
            words = request.GET.get('search').split()
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
