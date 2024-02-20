from django import forms
from til.models import Learned


class LearningForm(forms.ModelForm):
    class Meta:
        model = Learned
        fields = ["title", "tldr", "content"]
