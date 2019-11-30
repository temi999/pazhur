from rest_framework import serializers
from main_app.models import Reel, ReelSet, DefaultReel, DefaultReelSet
from django.contrib.auth.models import User


class ReelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reel
        fields = ['id', 'owner', 'reelset', 'name', 'description',
                  'field0', 'field1', 'field2', 'field3',
                  'field4', 'field5', 'field6', 'field7', ]


class ReelSetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ReelSet
        fields = ['id', 'owner', 'name', 'description', 'reels']


class DefaultReelSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultReelSet
        fields = ['id', 'name', 'description', 'reels']


class DefaultReelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultReel
        fields = ['id', 'name', 'reelset', 'description',
                  'field0', 'field1', 'field2', 'field3',
                  'field4', 'field5', 'field6', 'field7', ]

class UserSerializer(serializers.ModelSerializer):
    reelsets = serializers.PrimaryKeyRelatedField(many=True, queryset=ReelSet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'reelsets', 'reelset']
