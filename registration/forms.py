from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings
from django import forms

User = get_user_model()

widgets_textinput = forms.TextInput(
    attrs={
        "class": "form-control",
    }
)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class TextForm(forms.Form):

    search = forms.CharField(label="ブランド名", widget=widgets_textinput)
    limit = forms.CharField(label="検索件数")