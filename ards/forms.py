from django import forms
from .models import Profile,Image,Comment

class NewProfForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    # def __init__(self, *args, **kwargs):
    #     super(NewProfForm, self).__init__(*args, **kwargs)
        # self.fields['prof_pic'].required = False

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['reviews']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['design','usability','content']
