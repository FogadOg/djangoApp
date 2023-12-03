from django.contrib.auth.forms import UserCreationForm  
from django import forms  
import uuid

from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  



class SignupForm(UserCreationForm):
    username = forms.CharField(label='', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'Username'}))  
    # userBlocked=forms.BooleanField(initial=False)
    # email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'Email'}))  
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'Password'}))  
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'Confirm Password'}))  
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    # def email_clean(self):  
    #     email = self.cleaned_data['email'].lower()  
    #     new = User.objects.filter(email=email)  
    #     if new.count():  
    #         raise ValidationError(" Email Already Exist")  
    #     return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['password1']  
        )  
        return user  
    

    





