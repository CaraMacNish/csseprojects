from django import forms
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'short', 'honours', 'mds', 'se', 'engineering', 'other', 'numstudents', 'primary', 'cosupervisors', 'external', 'link', 'references')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '*Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }