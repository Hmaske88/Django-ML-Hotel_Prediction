from django.db import models

# Create your models here.
class DataBase(models.Model):
    location = models.IntegerField()
    rent = models.IntegerField()
    stars = models.IntegerField()
    food = models.IntegerField()
    foodType = models.IntegerField()
    discount = models.IntegerField()