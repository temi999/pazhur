from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    context = {
        'all_reelsets': ReelSet.objects.all(),
        'all_default_reelsets': DefaultReelSet.objects.all(),
    }
    return render(request, 'index.html', context)


def reel_sets(request):
    context = {
        'all_reelsets': ReelSet.objects.all(),
        'all_default_reelsets': DefaultReelSet.objects.all(),
    }

    return render(request, 'reel_sets.html', context)
