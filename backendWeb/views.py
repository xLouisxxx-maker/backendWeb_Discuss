from django.http import HttpResponse
from django.shortcuts import render
data = {
    'articles': [
        {   
            'title': "niga",
            'volume': 10,
            'issue': 4
        },
        {   
            'title': "niga2",
            'volume': 6,
            'issue': 4
        },
        {   
            'title': "test",
            'volume': 8,
            'issue': 1
        }
    ]
    }

def articles(request):
    #return HttpResponse("this is the first test")
    return render(request, 'articles/articles.html', data) #list of string for test

def home(request):
    return HttpResponse("home page")
