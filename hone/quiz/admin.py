from django.contrib import admin

from quiz.models import Question, Answer, Topic

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 4
    max_num = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['topic', 'question']}),
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic)
#admin.site.register(Answer)
