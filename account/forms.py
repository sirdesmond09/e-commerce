from django import forms
from django.contrib.auth.models import User
from account.models import Profile

class LoginForm(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password  = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password2'] != cd['password']:
            message = "Passwords don't match!"
            raise forms.ValidationError(message)
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ('date_of_birth', 'photo')
         
