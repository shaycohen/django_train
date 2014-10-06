#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Question
from django.template import RequestContext, loader


def index(request):
    latest_poll_list = Question.objects.order_by('-pub_date')[:5]
    #Shortcut# template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    #Shortcut# return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)
 
def detail(request, question_id):
    #Shortcut# try:
    #Shortcut#     poll = Question.objects.get(pk=question_id)
    #Shortcut# except Question.DoesNotExist:
    #Shortcut#     raise Http404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def text(request, question_id):
    q = Question.objects.get(id=question_id)
    return HttpResponse("Text for question '%s'" % q.question_text)

