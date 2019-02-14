
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext ']
    wordlist = fulltext.split()
    wordcount = {}

    for words in wordlist:
        if words in wordcount:
            wordcount[words] += 1
        else :
            wordcount[words] = 1

    result = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'val': result})

def about(request):
    return render(request, 'about.html')
