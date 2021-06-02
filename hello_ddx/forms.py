from django import forms

class DdxForm(forms.Form):
  name = forms.CharField(label = 'name')
  mail = forms.CharField(label = 'mail')
  age = forms.IntegerField(label = 'age')
  