from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=32, 
                            widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Password', max_length=32,
                            widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
