from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'ards/',default='SOME STRING')
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=100)

class Profile(models.Model):
    prof_pic = models.ImageField(upload_to = 'ards/',default='SOME STRING')
    bio = models.CharField(max_length=300)
    posts = models.ForeignKey(Project)
    contact = models.CharField(max_length=30)

class Review(models.Model):
    design = models.RatingField(range=10)
    usability = models.RatingField(range=10)
    content = models.RatingField(range=10)
