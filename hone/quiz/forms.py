from django.forms import ModelForm

from django.forms.models import inlineformset_factory
from quiz.models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        #fields = ['question', 'topic']
    
AnswerFormSet = inlineformset_factory(Question, Answer, extra=2)
