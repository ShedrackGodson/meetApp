from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"input"}))
    class Meta:
        model = User
        fields = ["username"]
        exclude = ["email"]

class UserUpdateEmail(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"input"}))
    class Meta:
        model = User
        fields = [
            "email"
        ]

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "location",
            "hometown"
        ]
        widgets = {
            "hometown": forms.TextInput(attrs={"class":"input"}),
            "location": forms.TextInput(attrs={"class": "input"}),
        }

class UserBirthdayForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "birthdate"
        ]

class UserGenderUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "gender"
        ]

class UserBioUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "bio"
        ]
        
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["user","location","hometown","birthdate","interests","gender"]
        widgets = {
            "location": forms.TextInput(attrs={"class": "input"}),
            "hometown": forms.TextInput(attrs={"class":"input"}),
            # "bio": forms.Textarea(attrs={"class":"input"}),
            "birthdate": forms.DateInput(attrs={"class":"input"}),
            "interests": forms.MultipleHiddenInput(attrs={"class":"input"}),
        }