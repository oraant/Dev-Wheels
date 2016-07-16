from django.db import models

# Create your models here.
class StoreTemplate(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    license = models.CharField(max_length=50)
    intro = models.CharField(max_length=3000)

    grade = models.IntegerField(null=True,blank=True)
    desc = models.CharField(max_length=3000,null=True,blank=True)
    imgs = models.CharField(max_length=3000,null=True,blank=True)
    tags = models.CharField(max_length=500,null=True,blank=True)

    up = models.IntegerField(null=True,blank=True)
    down = models.IntegerField(null=True,blank=True)
    watch = models.IntegerField(null=True,blank=True)
    star = models.IntegerField(null=True,blank=True)
    fork = models.IntegerField(null=True,blank=True)

    record = models.DateTimeField()
    version = models.CharField(max_length=20)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    country = models.CharField(max_length=500,null=True,blank=True)
    company = models.CharField(max_length=500,null=True,blank=True)

class TimeSeriesDatabase(StoreTemplate):
    category='database,autoOP'
