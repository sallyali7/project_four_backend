from django.db import models

# Create your models here.

class Jobs(models.Model):
    ''' Jobs Model '''
    title = models.CharField(max_length=500, unique=False)
    company_name = models.CharField(max_length= 500, unique=False)
    job_description = models.CharField(max_length=5000, unique=False)
    salary = models.PositiveIntegerField(unique=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

# class Blogs(models.Model):
#     ''' Blogs Model'''
#     title = models.CharField(max_length=500, unique=False)
#     content = models.CharField(max_length=10000, unique=False)
#     created_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.title}'