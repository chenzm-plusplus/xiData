from django.db import models

# Create your models here.

class Filelist(models.Model):
    fileID = models.IntegerField(default=0)
    fileName = models.CharField(max_length=30)