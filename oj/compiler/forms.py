from django import forms
from compiler.models import CodeSubmission
from home.models import Problems  

LANGUAGE_CHOICES = [
        ("py", "Python"),
        ("c", "C"),
        ("cpp", "C++"),
    ]
class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    

    class Meta:
        model = CodeSubmission
        fields = ["language", "code", "input_data"]

