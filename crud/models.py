from django.db import models

class crudstudent(models.Model):
    name=models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    mobile=models.IntegerField()
    gender=models.CharField(max_length=1)
