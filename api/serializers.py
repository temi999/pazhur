from rest_framework import serializers

# from main_app.models import SlotSet
#
#
# class SlotSetsSerizalizer(serializers.Serializer):
#     owner = serializers.IntegerField()
#     name = serializers.CharField(max_length=30)
#     description = serializers.CharField()
#     slot0 = serializers.CharField(max_length=30)
#     slot1 = serializers.CharField(max_length=30)
#     slot2 = serializers.CharField(max_length=30)
#     slot3 = serializers.CharField(max_length=30)
#     slot4 = serializers.CharField(max_length=30)
#     slot5 = serializers.CharField(max_length=30)
#     slot6 = serializers.CharField(max_length=30)
#     slot7 = serializers.CharField(max_length=30)
#
#     def create(self, validated_data):
#         return SlotSet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.slot0 = validated_data.get('slot0', instance.slot0)
#         instance.slot1 = validated_data.get('slot1', instance.slot1)
#         instance.slot2 = validated_data.get('slot2', instance.slot2)
#         instance.slot3 = validated_data.get('slot3', instance.slot3)
#         instance.slot4 = validated_data.get('slot4', instance.slot4)
#         instance.slot5 = validated_data.get('slot5', instance.slot5)
#         instance.slot6 = validated_data.get('slot6', instance.slot6)
#         instance.slot7 = validated_data.get('slot7', instance.slot7)
#
#         instance.save()
#         return instance
