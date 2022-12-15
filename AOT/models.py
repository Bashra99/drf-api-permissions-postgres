from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class AOT(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    description=models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.name

class Titan(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    description=models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.name

        
        
        
