from django.db import models

# Create your models here.

class Luggage(models.Model):
    created = models.CharField(max_length=100)
    luggage_types = models.TextField()
    max_items = models.IntegerField()
    status = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.created


class Order(models.Model):
    user = models.CharField(max_length=100)
    luggage_types = models.TextField()
    amount = models.IntegerField()

     
    def __str__(self):
        return self.user
