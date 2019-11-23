from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from main_app.models import SlotSet
from.serializers import SlotSetsSerizalizer


class SlotSetsView(APIView):
    def get(self, request):
        slot_sets = SlotSet.objects.all()
        serializer = SlotSetsSerizalizer(slot_sets, many=True)
        return Response({"SlotSets": serializer.data})


class CreateSlotSetView(APIView):
    def post(self, request):
        slot_sets = request.data.get('slot_set')

        serializer = SlotSetsSerizalizer(data=slot_sets)
        if serializer.is_valid(raise_exception=True):
            slot_set_saved = serializer.save()
        return Response({'success': 'Slot set "{}" created successfully'.format(slot_set_saved.name)})


class UpdateSlotSetView(APIView):
    def put(self, request, pk):
        saved_slot_set = get_object_or_404(SlotSet.objects.all(), pk=pk)
        data = request.data.get('slot_set')
        serializer = SlotSetsSerizalizer(instance=saved_slot_set, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            slot_set_saved = serializer.save()

        return Response({
            'success': 'Slot set "{}" updated succesfully'.format(slot_set_saved.name)
        })
