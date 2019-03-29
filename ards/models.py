from django.db import models

import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    user = models.OneToOneField(User,null=True)
    prof_pic = models.ImageField(upload_to = 'ards/',default='SOME STRING')
    bio = models.CharField(max_length=300)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

class Project(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'ards/',default='SOME STRING')
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

class Review(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    design = models.RatingField(range=10)
    usability = models.RatingField(range=10)
    content = models.RatingField(range=10)

    def save_review(self):
        self.save()
