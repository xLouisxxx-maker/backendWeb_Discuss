from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader

from django.http import Http404


data = { Question.objects.order_by("-pub_date")[:5]}


#def index(request):
   # latest_question_list = Question.objects.order_by("-pub_date")[:5]
   # template = loader.get_template("polls/index.html")
   # context = {
   #     "latest_question_list": latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("index/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def questions(request):
    #return HttpResponse("this is the first test")
    all_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("questions/questions.html")
    context = {
        "all_question_list": all_question_list,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'questions/questions.html', data) #list of string for test



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id): # damit 404 error
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})