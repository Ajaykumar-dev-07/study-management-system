#forms.py
from . models import Study
from django import forms


class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_name', 'study_description', 'study_phase', 'sponsor_name']