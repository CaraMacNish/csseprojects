from django import forms
from django.forms import ModelForm
from .models import Project, Supervisor

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('primary', 'cosupervisor', 'title', 'description','honours', 'mds', 'se', 'other',
             'numstudents', 'external', 'link', 'references', 'short', 'skills','visible')
        labels = {
#            'primary': 'Primary supervisor',
#            'title': 'Topic title',
#            'description': 'Description',
        }
        help_texts = {
            'primary': 'Please contact the <a href="mailto:cara.macnish@uwa.edu.au">Projects Coordinator</a> to be added as a supervisor.'
        }

        widgets = {
            'primary': forms.Select(attrs={'class': 'form-select'}),
            'cosupervisor': forms.Select(attrs={'class': 'form-select'}),
            'external': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':"6"}),
            'short': forms.Textarea(attrs={'class': 'form-control', 'rows':"3"}),
            'honours': forms.CheckboxInput(attrs={'class': 'check_test'}),
            'mds': forms.CheckboxInput(attrs={'class': 'check_test'}),
            'se': forms.CheckboxInput(attrs={'class': 'check_test'}),
            'other': forms.TextInput(attrs={'class': 'form-control'}),
            'numstudents': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'references': forms.Textarea(attrs={'class': 'form-control', 'rows':"3"}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'visible': forms.CheckboxInput(attrs={'class': 'check_test'}),
        }