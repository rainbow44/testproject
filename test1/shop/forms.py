from django import forms


class TestForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200, widget = forms.TextInput(attrs={'id':'forminput1'}))


class MainForm(forms.Form):
    username = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=30)
    comment = forms.CharField(max_length=500)
