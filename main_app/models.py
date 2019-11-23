from django.db import models
from django.contrib.auth.models import User


class Reel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    field0 = models.CharField(max_length=30, default='1')
    field1 = models.CharField(max_length=30, default='2')
    field2 = models.CharField(max_length=30, default='3')
    field3 = models.CharField(max_length=30, default='4')
    field4 = models.CharField(max_length=30, default='5')
    field5 = models.CharField(max_length=30, default='6')
    field6 = models.CharField(max_length=30, default='7')
    field7 = models.CharField(max_length=30, default='8')

    def __str__(self):
        return self.name


class ReelSet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    reels = models.ManyToManyField(Reel, verbose_name='list of reels')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['owner']


class DefaultReel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    field0 = models.CharField(max_length=30, default='1')
    field1 = models.CharField(max_length=30, default='2')
    field2 = models.CharField(max_length=30, default='3')
    field3 = models.CharField(max_length=30, default='4')
    field4 = models.CharField(max_length=30, default='5')
    field5 = models.CharField(max_length=30, default='6')
    field6 = models.CharField(max_length=30, default='7')
    field7 = models.CharField(max_length=30, default='8')

    def __str__(self):
        return self.name


class DefaultReelSet(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    reels = models.ManyToManyField(DefaultReel, verbose_name='list of default reels')

    def __str__(self):
        return self.name


