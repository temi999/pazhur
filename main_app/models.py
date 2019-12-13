from django.db import models
from django.contrib.auth.models import User

MAX_FIELD_LENGTH = 60


class Node(models.Model):
    owner = models.ForeignKey(User, related_name='nodes', on_delete=models.CASCADE)
    reel = models.ForeignKey('Reel', related_name='nodes', on_delete=models.CASCADE)
    description = models.TextField(null=True)
    content = models.CharField(max_length=MAX_FIELD_LENGTH)

    def __str__(self):
        return self.content


class Reel(models.Model):
    owner = models.ForeignKey(User, related_name='reels', on_delete=models.CASCADE)
    reelset = models.ForeignKey('ReelSet', related_name='reels', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

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


class DefaultNode(models.Model):
    reel = models.ForeignKey('DefaultReel', related_name='nodes', on_delete=models.CASCADE)
    description = models.TextField(null=True)
    content = models.CharField(max_length=MAX_FIELD_LENGTH)

    def __str__(self):
        return self.content


class DefaultReel(models.Model):
    name = models.CharField(max_length=30)
    reelset = models.ForeignKey('DefaultReelSet', related_name='reels', on_delete=models.CASCADE)
    description = models.TextField(null=True)
    leave_empty = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DefaultReelSet(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


