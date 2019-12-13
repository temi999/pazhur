from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from api.serializers import *


class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ReelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reel.objects.all()
    serializer_class = ReelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class ReelSetList(generics.ListCreateAPIView):
    queryset = ReelSet.objects.all()
    serializer_class = ReelSetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReelSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReelSet.objects.all()
    serializer_class = ReelSetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


# ---------------------------------- DEFAULT SETS -------------------------------------------


class DefaultNodeDetail(generics.RetrieveAPIView):
    queryset = DefaultNode.objects.all()
    serializer_class = DefaultNodeSerializer


class DefaultReelSetList(generics.ListAPIView):
    queryset = DefaultReelSet.objects.all()
    serializer_class = DefaultReelSetSerializer


class DefaultReelSetDetail(generics.RetrieveAPIView):
    queryset = DefaultReelSet.objects.all()
    serializer_class = DefaultReelSetSerializer


class DefaultReelDetail(generics.RetrieveAPIView):
    queryset = DefaultReel.objects.all()
    serializer_class = DefaultReelSerializer


# -------------------------------------- USERS ----------------------------------------------


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
