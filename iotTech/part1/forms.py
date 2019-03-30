from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from part1.models import Document


class user_SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True, help_text='*required')
    last_name = forms.CharField(max_length=30, required=True, help_text='*required')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1', 'password2', )


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('userid','description', 'document', )