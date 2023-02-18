from django.db import models

class addrate(models.Model):
    Category=models.CharField(max_length=40)
    Rating=models.CharField(max_length=10,null=True,blank=True)

class addmoviedb(models.Model):
    Language=models.CharField(max_length=20)
    Category = models.CharField(max_length=40)
    Name=models.CharField(max_length=30)
    Image=models.ImageField(upload_to="Profile",blank=True,null=True)


