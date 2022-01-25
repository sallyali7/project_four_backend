from django.db import models

# Create your models here.
class Blogs(models.Model):
    ''' Blogs Model'''
    title = models.CharField(max_length=5000, unique=False)
    content = models.CharField(max_length=10000, unique=False)
    image = models.CharField(max_length=300, unique=False)

    def __str__(self):
        return f'{self.title}'