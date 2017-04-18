from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms



class QuestionManager(models.Manager):
    def recent(self):
        return self.order_by('-creation_date')
    
    def hot(self):
        return self.order_by('-rating')


class Tag(models.Model):
    content = models.CharField(primary_key=True, max_length=10)
    
    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return '/tag/%s' % self.content

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.FileField()
    rating = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nickname

class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    objects = QuestionManager()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return 'question/%d' % self.id

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField()
    rating = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = { 'content': forms.Textarea(attrs={'class' : 'form-control'})}

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        widgets = { 'content': forms.FileInput(attrs={'class' : 'form-control'})}

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password', 'email' ]
        widgets = {
          'username': forms.TextInput(attrs={'class' : 'form-control'}),
          'password': forms.PasswordInput(attrs={'class' : 'form-control'}),
          'email': forms.EmailInput(attrs={'class' : 'form-control'})
        }
