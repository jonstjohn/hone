from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=300)
    topic = models.ForeignKey('Topic')

    def __unicode__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=300)
    correct = models.BooleanField()
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.answer

class Topic(models.Model):
    topic = models.CharField(max_length=50)

    def __unicode__(self):
        return self.topic

class Quiz(models.Model):
    quiz = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.quiz

class Attempt(models.Model):
    quiz = models.ForeignKey(Quiz)
    user = models.ForeignKey(User)

    def get_absolute_url(self):
        return '/quiz/attempt/{0}'.format(self.id)

class Response(models.Model):
    attempt = models.ForeignKey(Attempt)
    answer = models.ForeignKey(Answer)
