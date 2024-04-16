from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.Fields + ()
