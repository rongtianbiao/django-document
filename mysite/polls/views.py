from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    content = {
        "latest_question_list": latest_question_list,
    }
    # output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, "polls/index.html", content)


def detail(request, question_id):
    # try:
    question = get_object_or_404(Question, pk=question_id)
    # except:
    #     raise Http404("question does not exists")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "you are looking at the results of questions %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question %s." % question_id)