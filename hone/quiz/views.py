from django.http import HttpResponse
from django.shortcuts import render

from quiz.models import Question

def index(request):
    questions = Question.objects.all()
    #output = ', '.join([q.question for q in questions])
    context = {'questions': questions}
    return render(request, 'quiz/index.html', context)
    #return HttpResponse(output)

