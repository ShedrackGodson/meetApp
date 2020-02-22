from django import forms
from .models import GroupDetails

class GroupForm(forms.ModelForm):
    class Meta:
        model = GroupDetails
        fields = [
            'group_name','group_location','group_about','organizers'
        ]

    # name = forms.CharField(
    #     max_length = 50,
    #     help_text = "Every group has a name.."
    # )
    # topic = forms.CharField(
    #     max_length = 255,
    #     help_text = "Topics of a group.."
    # )
    # location = forms.CharField(
    #     help_text = "Locate your group.."
    # )

    # def clean(self):
    #     cleaned_data = super(GroupForm, self).clean()
    #     name = cleaned_data.get('name')
    #     topic = cleaned_data.get('topic')
    #     location = cleaned_data.get('location')
    #     if not name and not topic and not location:
    #         raise forms.ValidationError("You can't create an empty group..")