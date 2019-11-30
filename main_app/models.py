from django.db import models
from django.contrib.auth.models import User

MAX_FIELD_LENGTH = 60


class Reel(models.Model):
    owner = models.ForeignKey(User, related_name='reels', on_delete=models.CASCADE)
    reelset = models.ForeignKey('ReelSet', related_name='reels', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    field0 = models.CharField(max_length=MAX_FIELD_LENGTH, default='1')
    field1 = models.CharField(max_length=MAX_FIELD_LENGTH, default='2')
    field2 = models.CharField(max_length=MAX_FIELD_LENGTH, default='3')
    field3 = models.CharField(max_length=MAX_FIELD_LENGTH, default='4')
    field4 = models.CharField(max_length=MAX_FIELD_LENGTH, default='5')
    field5 = models.CharField(max_length=MAX_FIELD_LENGTH, default='6')
    field6 = models.CharField(max_length=MAX_FIELD_LENGTH, default='7')
    field7 = models.CharField(max_length=MAX_FIELD_LENGTH, default='8')

    def __str__(self):
        return self.name


class ReelSet(models.Model):
    owner = models.ForeignKey(User, related_name='reelsets', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['owner']


class DefaultReel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    field0 = models.CharField(max_length=MAX_FIELD_LENGTH, default='1')
    field1 = models.CharField(max_length=MAX_FIELD_LENGTH, default='2')
    field2 = models.CharField(max_length=MAX_FIELD_LENGTH, default='3')
    field3 = models.CharField(max_length=MAX_FIELD_LENGTH, default='4')
    field4 = models.CharField(max_length=MAX_FIELD_LENGTH, default='5')
    field5 = models.CharField(max_length=MAX_FIELD_LENGTH, default='6')
    field6 = models.CharField(max_length=MAX_FIELD_LENGTH, default='7')
    field7 = models.CharField(max_length=MAX_FIELD_LENGTH, default='8')

    def __str__(self):
        return self.name


class DefaultReelSet(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    reels = models.ManyToManyField(DefaultReel, verbose_name='list of default reels')

    def __str__(self):
        return self.name


