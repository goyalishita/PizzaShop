from django.db import models

# Create your models here.

class Pizza(models.Model):
    name=models.CharField(max_length=200,null=True)
    type=models.CharField(max_length=200,null=True)
    size=models.IntegerField(default=10,null=True,blank=True)
    topping=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.name)