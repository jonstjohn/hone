from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz)

class Choice(models.Model):
    choice = models.CharField(max_length=300)
    correct = models.BooleanField()
    question = models.ForeignKey(Question)

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    
