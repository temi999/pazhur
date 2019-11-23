from django.contrib import admin
from .models import (
    Reel,
    ReelSet,
    DefaultReel,
    DefaultReelSet
)

# Register your models here.
admin.site.register(Reel)
admin.site.register(ReelSet)
admin.site.register(DefaultReel)
admin.site.register(DefaultReelSet)
