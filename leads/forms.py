from django import forms

class Leadform(forms.Form):
    Name = forms.CharField(max_length=20)
    Surname = forms.CharField(max_length=20)
    Age = forms.IntegerField(min_value=0)