from django import forms
from django.core import validators
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.forms import widgets
from firstApplication import models

def name(value):
    if len(value) <= 6:
        raise forms.ValidationError("Please Enter At leaset Six Character")
    
    elif len(value) >= 20:
        raise forms.ValidationError("Sorry! You Cross the Max Limit.Maximum Word Limit is 20")
    
def even(value):
    if len(value) < 8:
        raise forms.ValidationError("Password Would Be Minimum 8 Character")
    
    elif len(value) >= 12:
        raise forms.ValidationError("Your Password is longer than 12 Character")
         
                  

class StudentList(forms.ModelForm): 
    class Meta:
        model = models.StudentList
        fields='__all__'
        
class user_login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}))