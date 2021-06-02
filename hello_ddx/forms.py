from django import forms

class DdxForm(forms.Form):
  bt_data = [
    ('bun','BUN'),
    ('cre','CRE'),
    ('gpt','GPT'),
    ('alb','ALB'),
    ('t-bil','T-Bil'),
    ('ca','Ca')
  ]

  bt_choice = forms.ChoiceField(label='radio',choices = bt_data,widget = forms.Select(attrs={'size':5}))
