from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=150, 
                            widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Password', max_length=150,
                            widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class PasswordUpdateForm(forms.Form):
    origin = forms.CharField(label='New Password', max_length=150, required=False,
                        widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    repeated = forms.CharField(label='Repeat Password', max_length=150, required=False,
                        widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    
    def clean(self):
        cleaned_data = super(PasswordUpdateForm, self).clean()
        
        if cleaned_data.get('origin') != cleaned_data.get('repeated'):
            raise forms.ValidationError("Password ain't equal")

class SignupForm(forms.Form):
    username = forms.CharField(label='Login', max_length=150, 
                            widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(label='Email', max_length=150,
                            widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Password', max_length=150,
                            widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    repeated = forms.CharField(label='Repeat Password', max_length=150,
                            widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    avatar = forms.ImageField(label='Avatar', required=False,
                             widget=forms.FileInput(attrs={'class' : 'form-control'}))
    
    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        
        if cleaned_data.get('password') != cleaned_data.get('repeated'):
            raise forms.ValidationError("Password ain't equal")
        
    def clean_username(self):
        if User.objects.get(username=self.cleaned_data['username']):
            raise forms.ValidationError("Username already registered")

