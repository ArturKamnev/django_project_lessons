from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


class CustomRegisterForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=100, initial='+996')
    gender = forms.CharField(required=True, max_length=100, initial='m')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'photo',
            'first_name',
            'email',
            'phone_number',
            'gender',
        )
    
    def save(self, commit = True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user