from django import forms
from .models import Topics, MeetAppGroup


class GroupCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Write your group name...'
        }
    ))
    location = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Type your city...',
            'class': 'controls'
        }
    ))
    topics = forms.CheckboxSelectMultiple(
        attrs={
            'class':'form-control'
        }
    )
    desc = forms.Textarea(
        attrs={
            'cols':10,
            'rows':10,
            'placeholder':'Please write at least 50 characters',
            'required': 'true'
        }
    )
    class Meta:
        model = MeetAppGroup
        fields = ("name","location","topics","desc")