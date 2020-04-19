from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User 

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        #fields = ('username', 'email')
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
        