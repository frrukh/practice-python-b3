from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.id}--{self.first_name}-{self.email}'

class Student(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.id}--{self.f_name}--{self.email}'