from django import forms
from .models import Book

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class DateInput(forms.DateInput):
    input_type = 'date'

class BookCreate(forms.ModelForm):
    # any validation or modification
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    release_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Book
        fields = '__all__'