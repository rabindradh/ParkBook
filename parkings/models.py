from django.db import models
from datetime import datetime
from owners.models import Owner
# Create your models here.

class Parking(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.IntegerField(max_length=100)
    park_date = models.DateTimeField(default=datetime.now,blank=True)
    no_of_vehicle = models.IntegerField(default=0)
    photo_garage = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_occupied = models.BooleanField(default=True)
    def __str__(self):
        return self.title