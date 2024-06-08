from django.db import models

# Create your models here.
class TaskItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    id_user = models.IntegerField()  

class LoginItem(models.Model):
    id_user = models.IntegerField(auto_created= True)
    user= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    