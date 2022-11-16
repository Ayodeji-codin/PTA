from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 90, label = 'Username')
    password = forms.CharField(max_length = 70, widget = forms.PasswordInput, label = 'Password')

#class GeneralForm(forms.Form):
#    id = forms.CharField(max)