from django import forms
from .models import Vault_User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=14, required=True)
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)
    user_first_name = forms.CharField(max_length=30, required=True)
    user_last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Vault_User
        fields = ['username', 'password', 'user_first_name', 'user_last_name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password and password_repeat and password != password_repeat:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = Vault_User(
            username=self.cleaned_data['username'],
            user_first_name=self.cleaned_data['user_first_name'],
            user_last_name=self.cleaned_data['user_last_name'],
            is_superuser=False,
        )
        user.set_password(self.cleaned_data['password'])  # Use set_password()
        if commit:
            user.save()
        return user

    


