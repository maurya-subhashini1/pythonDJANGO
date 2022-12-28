# from django.db import models
from djongo import models



class Article(models.Model):
    objectId=models.ObjectIdField()
    title=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    comment=models.CharField(max_length=500)


    # def __str__(self):
    #     return self.title



 