from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View, RedirectView
from django.views.generic import CreateView, UpdateView

from quiz.models import Question, Quiz, Attempt, Response, Answer
from quiz.forms import QuestionForm, AnswerFormSet

class HomePageView(TemplateView):

    template_name = 'quiz/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['quizzes'] = Quiz.objects.all()
        return context

class DetailPageView(TemplateView):
    
    template_name = 'quiz/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailPageView, self).get_context_data(**kwargs)
        context['quiz'] = Quiz.objects.get(pk=kwargs['quiz_id'])
        return context

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

class AttemptCreateRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        quiz = Quiz.objects.get(pk=kwargs['quiz_id'])
        attempt = Attempt(user = self.request.user, quiz = quiz)
        attempt.save()

        return attempt.get_absolute_url()

def attempt(request, attempt_id):
    attempt = Attempt.objects.get(pk=attempt_id)
    return render(request, 'quiz/attempt/index.html', {'attempt': attempt})

class AttemptQuestionPageView(View):

    def get(self, request, *args, **kwargs):

        attempt = Attempt.objects.get(pk=kwargs['attempt_id'])
        quiz = attempt.quiz
        questions = quiz.questions.all()

        pos = int(kwargs['num'])

        # TODO incorrect position
        if pos >= len(questions):
            error = True

        question = questions[pos]

        responses = Response.objects.filter(attempt=attempt, answer__question=question)
        response = responses[0] if responses else None
        context = {'question': question, 'answers': question.answer_set.all(), 'number': pos + 1, 'response': response, 'attempt': attempt}
        return render(request, 'quiz/attempt/question.html', context)

    def post(self, request, *args, **kwargs):

        attempt = Attempt.objects.get(pk=kwargs['attempt_id'])
        answer = Answer.objects.get(pk=request.POST['answer']) 
        pos = int(kwargs['num'])
        questions = attempt.quiz.questions.all()
        question = questions[pos]

        responses = Response.objects.filter(attempt=attempt, answer__question=question)

        if responses:
            response = responses[0]
            response.answer = answer
        else:
            response = Response(attempt = attempt, answer = answer)
        response.save()

        pos = int(kwargs['num'])

        if pos == len(questions) - 1:
            return redirect('/quiz/attempt/{0}/result'.format(attempt.id, pos + 1))
        else:
            return redirect('/quiz/attempt/{0}/{1}'.format(attempt.id, pos + 1))

class AttemptResultPageView(TemplateView):

    template_name = 'quiz/attempt/result.html'

    def get_context_data(self, **kwargs):
        context = super(AttemptResultPageView, self).get_context_data(**kwargs)
        attempt = Attempt.objects.get(pk=kwargs['attempt_id'])
        responses = Response.objects.filter(attempt=attempt)
        context['responses'] = responses
        context['attempt'] = attempt
        context['questionCount'] = attempt.quiz.questions.count()

        return context

class DashboardPageView(TemplateView):

    template_name = 'quiz/dashboard.html'

class ContributeHomePageView(TemplateView):

    template_name = 'quiz/contribute/index.html'

class QuestionCreatePageView(CreateView):

    model = Question 
    template_name = 'quiz/question/create.html'
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super(QuestionCreatePageView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['answer_formset'] = AnswerFormSet(self.request.POST)
        else:
            context['answer_formset'] = AnswerFormSet()
            context['test'] = 'test'
        return context
