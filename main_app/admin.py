from django.contrib import admin
from .models import (
    Node,
    Reel,
    ReelSet,
    DefaultNode,
    DefaultReel,
    DefaultReelSet
)

# Register your models here.
admin.site.register(Node)
admin.site.register(Reel)
admin.site.register(ReelSet)
admin.site.register(DefaultNode)
admin.site.register(DefaultReel)
admin.site.register(DefaultReelSet)
