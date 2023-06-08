from django.db import models

# Create your models here.



class User_Profile(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    referral = models.CharField(max_length=255)
    team=models.CharField(max_length=255,default='NONE')


from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='teams')

class Invitations(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)



class Competition(models.Model):
    name = models.CharField(max_length=100)
    rulebook = models.FileField(upload_to='rulebooks/')

    def __str__(self):
        return self.name

class Payment(models.Model):
    email =models.EmailField()
    utr = models.CharField(max_length=255)

    def __str__(self):
        return self.email
