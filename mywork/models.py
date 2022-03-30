from django.db import models

# Create your models here.
class accoubtasid(models.Model):
    useraccount=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    class Meta:
        db_table = 'accoubtasid'