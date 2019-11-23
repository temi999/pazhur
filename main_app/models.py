from django.db import models


# хранить значение каждого слота на барабане
class SlotSet(models.Model):
    owner = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    slot0 = models.CharField(max_length=30)
    slot1 = models.CharField(max_length=30)
    slot2 = models.CharField(max_length=30)
    slot3 = models.CharField(max_length=30)
    slot4 = models.CharField(max_length=30)
    slot5 = models.CharField(max_length=30)
    slot6 = models.CharField(max_length=30)
    slot7 = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['owner']
