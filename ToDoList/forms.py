from django import forms
from .models import ToDoList

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields="__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title',
                                            'placeholder': 'TITLE HERE',
                                            }),
            'details': forms.TextInput(attrs={'class': 'details',
                                              'placeholder': 'DETAILS HERE'}),
            'date': forms.TextInput(attrs={'class': 'date',
                                           'type': 'datetime-local',
                                           }),
        }