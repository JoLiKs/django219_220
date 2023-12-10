from django import forms


class UserForm(forms.Form):
    img = forms.ImageField()