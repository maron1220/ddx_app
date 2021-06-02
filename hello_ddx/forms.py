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

  bt_choice = forms.ChoiceField(label='血液項目',choices = bt_data,widget = forms.Select(attrs={'size':5}),initial=['bun'])


class UpdownForm(forms.Form):
  status_data = [
    ('up','上昇'),
    ('down','低下'),
  ]

  status_choice = forms.ChoiceField(label='状態',choices = status_data,widget = forms.Select(attrs={'size':2}),initial=['up'])