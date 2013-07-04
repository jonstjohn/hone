from django.forms import ModelForm, HiddenInput, Textarea
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

from quiz.models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'question']
        widgets = {'question': Textarea}

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        
        self.helper.layout = Layout(Field('topic'), Field('question', rows='4', css_class='input-xxlarge'))

        #self.fields['question'].widget = Textarea(attrs={'rows': 4, 'cols': 80})

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

        button_text = 'Correct' if self.fields['correct'].initial == 'Correct' else 'Incorrect'
        button_css = 'correct-button btn-success' if self.instance.correct else 'correct-button btn-danger' #  ng-click="toggleCorrect()"'
        self.helper.layout = Layout(FieldWithButtons('answer', StrictButton(button_text, css_class=button_css, ng_click="toggleCorrect()")))
    
AnswerFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, can_delete=False, extra=4, max_num=4)
