from django.http import HttpResponse
from django.shortcuts import render

from quiz.models import Question, Quiz

def index(request):
    questions = Question.objects.all()
    #output = ', '.join([q.question for q in questions])
    context = {'questions': questions}
    return render(request, 'quiz/index.html', context)
    #return HttpResponse(output)

def question(request, quiz_id, num):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = quiz.questions.all()
    
    pos = int(num)

    # TODO incorrect position
    if pos >= len(questions):
        error = True

    question = questions[pos]
    context = {'question': question, 'answers': question.answer_set.all()}
    return render(request, 'quiz/question.html', context)
