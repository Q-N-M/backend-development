from django.db import models

class User(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=256)