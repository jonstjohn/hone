from django.forms import ModelForm, HiddenInput
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

from quiz.models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'question']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'correct']

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['correct'].widget = HiddenInput()
        button_text = 'Correct' if self.fields['correct'].initial == 'True' else self.fields['correct'].initial #'Incorrect'
        button_css = 'btn-success' if self.instance.correct else 'btn-danger ng-click="alert()"'
        self.helper.layout = Layout(FieldWithButtons('answer', StrictButton(button_text, css_class=button_css)))
    
AnswerFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, can_delete=False, extra=4, max_num=4)
