from django.db import models

# Create your models here.
class Member(models.Model):
    mid = models.CharField(max_length=100)
    pw = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.mid + ', ' + self.pw + ', ' +  self.nickname + ', ' +  self.gender + ', ' +  self.country + ', ' +  self.email

class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country