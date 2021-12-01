from django import forms 

class UserCreation(forms.Form):
    username = forms.CharField(label='Name',max_length=100)
   # email = forms.EmailField()
    password = forms.CharField(label='Pass', min_length=8, max_length=20)
    