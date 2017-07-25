from django.forms import ModelForm
from .models import Task
from django import forms
from django.utils.translation import ugettext_lazy as _

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','dateCreated','user_id']
        labels = {
                'name':_('Task Name'),
                'description':_('Task description'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'dateCreated' : forms.HiddenInput(),
            'user_id' : forms.HiddenInput(),
                    }

class UpdateTaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name','description','dateUpdated']
        labels = {
                'name':_('Task Name'),
                'description':_('Task description'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'dateUpdated' : forms.HiddenInput(),
                    }
