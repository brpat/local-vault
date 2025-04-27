from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=14, label="Username")
    password = forms.CharField(max_length=30, label="Password", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, label="First_Name")
    last_name = forms.CharField(max_length=30, label="Last_Name")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=14, label="Username")
    password = forms.CharField(max_length=30, label="Password", widget=forms.PasswordInput)

