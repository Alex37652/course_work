from django.forms import ModelForm, DateInput
from calender.models import Event
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

from .models import *



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input','placeholder': 'Your email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Repeat password'}))
    group = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'group')


class LoginUserForm(AuthenticationForm):
  username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
  password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))


class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)