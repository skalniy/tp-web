from django.db import models
from django.contrib.auth.models import User



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
    content = models.TextField()
    is_correct = models.BooleanField()
    rating = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
