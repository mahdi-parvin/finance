# ---the form page to writing down the forms to use in templates---
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# ---difing a signin form to get the signin data from the user---
class UserSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype password'}))
    # ---confirm emial checks if the email exists before or not---

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('the email exist')
        return email

    # ---and a clean_username to make sure no such username exists---
    def clean_username(self):
        username=self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('select another username')

    #--- and the same part to the password---
    def clean(self):
        cleaned_data = super(UserSigninForm, self).clean()
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('confirm_password')

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('passwords must be same')

# --- UserLoginForm to use in the login template and getting the user input values---
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'type your password'}))

# ---end of the page---