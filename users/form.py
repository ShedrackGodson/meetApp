from django import forms
from .models import Profile
from django.contrib.auth.models import User



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"input"}))
    class Meta:
        model = User
        fields = ["username","email"]


class ProfileUpdateForm(forms.ModelForm):
    # location = forms.TextInput(widget=forms.TextInput(attrs={"class":"input"}))
    # hometown = forms.CharField(widget=forms.CharField(attrs={"class":"input"}))
    # bio = forms.TextInput(widget=forms.TextInput(attrs={"class":"input"}))
    # birthdate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"input"}))
    # avatar = forms.ImageField(widget=forms.ImageField(attrs={"class":"input"}))
    # interests = forms.CharField(widget=forms.CharField(attrs={"class":"input"}))

    class Meta:
        model = Profile
        fields = ["location","hometown","birthdate","bio","interests"]
        widgets = {
            "location": forms.TextInput(attrs={"class": "inpu"}),
            "hometown": forms.TextInput(attrs={"class":"input"}),
            "bio": forms.Textarea(attrs={"class":"input"}),
            "birthdate": forms.DateInput(attrs={"class":"input"}),
            "interests": forms.MultipleHiddenInput(attrs={"class":"input"}),
            # "avatar": forms.(attrs={"class":"input"}),
        }