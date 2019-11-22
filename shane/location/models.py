from django.db import models

# Create your models here.
class Country_group(models.Model):
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_total = models.IntegerField(default=0)


    def __str__(self):
        return self.location + ', ' + self.gender + ', ' + self.country + ', ' + str(self.country_total)


class Visa_group(models.Model):
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    visa_type = models.CharField(max_length=100)
    visa_total = models.IntegerField(default=0)

    def __str__(self):
        return self.location + ', ' + self.gender + ', ' + self.visa_type + ', ' + str(self.visa_total)


class Age_group(models.Model):
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age_arange = models.CharField(max_length=100)
    age_total = models.IntegerField(default=0)

    def __str__(self):
        return self.location + ', ' + self.gender + ', ' + self.age_arange + ', ' + str(self.age_total)