from rest_framework import serializers
from main_app.models import Node, Reel, ReelSet, DefaultNode, DefaultReel, DefaultReelSet
from django.contrib.auth.models import User


class NodeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Node
        fields = ['id', 'owner', 'reel', 'description', 'content']


class ReelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reel
        fields = ['id', 'owner', 'reelset', 'name', 'description', 'nodes']


class ReelSetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ReelSet
        fields = ['id', 'owner', 'name', 'description', 'reels']


class DefaultNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultNode
        fields = ['id', 'reel', 'description', 'content']


class DefaultReelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultReel
        fields = ['id', 'name', 'reelset', 'description', 'nodes']


class DefaultReelSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultReelSet
        fields = ['id', 'name', 'description', 'reels']


class UserSerializer(serializers.ModelSerializer):
    reelsets = serializers.PrimaryKeyRelatedField(many=True, queryset=ReelSet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'reelsets', 'reelset']
