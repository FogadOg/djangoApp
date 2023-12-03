# authentication/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'Username'}),label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'Password'}),label='')