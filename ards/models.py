from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to = 'ards/',default='SOME STRING')
    description=models.CharField(max_length=300)
    link=models.CharField(max_length=100)
