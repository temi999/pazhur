from django.shortcuts import render
from .models import SlotSet


# Create your views here.
def index(request):
    context = {
        'num_slotsets': SlotSet.objects.all().count(),
    }
    return render(request, 'index.html', context)


def slot_sets(request):
    context = {
        'count': SlotSet.objects.all().count(),
        'objects': SlotSet.objects.all(),
    }

    return render(request, 'slot_sets.html', context)
