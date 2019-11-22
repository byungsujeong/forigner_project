from django.db import models

# Create your models here.
class Visit(models.Model):
    country = models.CharField(max_length=100)
    yyyymm = models.CharField(max_length=100)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.country + ', ' + self.yyyymm + ', ' + str(self.total)

class Yyyy(models.Model):
    yyyy = models.CharField(max_length=100)

    def __str__(self):
        return self.yyyy