from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StudentForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
		exclude = ['user']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
