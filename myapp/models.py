from django.db import models
from django.utils import timezone
# Create your models here.
class Dreamreal(models.Model):
    website=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    class Meta:
        db_table = 'dreamreal'


class Adoptreal(models.Model):
    yellowcard = models.CharField(max_length=50)
    yellowcardnumber = models.CharField(max_length=50)
    why = models.CharField(max_length=200)
    place = models.CharField(max_length=50)
    varity = models.CharField(max_length=50)
    userwho=models.CharField(max_length=50)
    petname=models.CharField(max_length=50)
    petsex=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='static/picture', blank=False, null=False)
    phonenumber=models.IntegerField()
    class data:
        db_table = 'adoptreal'

class Helpreal(models.Model):
    when = models.DateTimeField(default=timezone.now)
    where = models.CharField(max_length=50)
    petname = models.CharField(max_length=50)
    varity=models.CharField(max_length=50)
    yellowcard=models.CharField(max_length=50)
    yellowcardnumber=models.CharField(max_length=50)
    special = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/picture', blank=False, null=False)
    phonenumber=models.IntegerField()
    class feta:
        db_table = 'helpreal'
