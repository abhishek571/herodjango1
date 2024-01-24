from django.db import models

# Create your models here.
class DC(models.Model):
    name=models.CharField(max_length=30)
    heroicname=models.CharField(max_length=30)
    
