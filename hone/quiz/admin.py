from django.contrib import admin
from quiz.models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Question)
admin.site.register(Answer)
