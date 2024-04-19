from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False)
    category=models.CharField(max_length=100, null=False, blank=False)
    price=models.IntegerField()
    Description=models.TextField()
    Rating=models.IntegerField()
    #to show the actual product name in admin portal
    def __str__(self):
        return self.name
