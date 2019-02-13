from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    def __str__(self):
        return self.name
