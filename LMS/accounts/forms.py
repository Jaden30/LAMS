from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text= "A valid email is required", required = True)


    class Meta:
        model = Account
        fields = ("email", "username", "first_name", "last_name", "password1", "password2")