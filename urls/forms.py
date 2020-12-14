from django import forms


class CreateUrlForm(forms.Form):
    url = forms.CharField()
