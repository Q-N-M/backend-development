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
    phone_number = models.CharField(max_length=256, null=True)
    emergency_contact = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.name

class Community(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Transport(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=200)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    description = models.TextField()

class Emoji(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserEmoji(models.Model):
    id = models.BigAutoField(primary_key=True)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, null = True)
    name = models.CharField(max_length=200,null = True)
    comment = models.TextField(null = True)

    def __str__(self):
        return self.name
