from django.db import models

# Create your models here.
class Player(models.Model):
    pos = models.CharField(max_length=2)
    no = models.IntegerField("number")
    player = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gs = models.IntegerField(default=0)
    sb = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    sh = models.IntegerField(default=0)
    sg = models.IntegerField(default=0)
    a = models.IntegerField(default=0)
    fc = models.IntegerField(default=0)
    fs = models.IntegerField(default=0)
    yc = models.IntegerField(default=0)
    rc = models.IntegerField(default=0)
