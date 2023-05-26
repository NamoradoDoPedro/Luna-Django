from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.DateField(max_length=30)
    sex = models.CharField(max_length=10)
