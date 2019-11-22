from django.db import models

# Create your models here.
# 회원 정의
class Member(models.Model):
    mid = models.CharField(max_length=100)
    pw = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.mid + ', ' + self.pw + ', ' +  self.nickname + ', ' +  self.gender + ', ' +  self.country + ', ' +  self.email

# 나라 리스트
class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country