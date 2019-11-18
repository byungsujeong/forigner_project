from django.db import models

# Create your models here.
# comunity bulletin board 정의
class Bbs(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mid = models.CharField(max_length=100)
    udate = models.DateTimeField(auto_now=True)
    user_nick = models.CharField(max_length=100, null=True)
    user_country = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id) + ', ' + self.title + ', ' + self.content + ', ' + self.country + ', ' + self.mid + ', ' + str(self.udate) + ', ' + str(self.user_nick) + ', ' + str(self.user_country)