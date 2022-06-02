from django.shortcuts import render
from .models import TypeOfRoomModel, RoomModel, RoomImageModel 
from rest_framework.viewsets import ModelViewSet
from .serializers import TypeOfRoomModelSerializer, RoomModelSerializer, RoomImageModelSerializer


class TypeOfRoomViewSet(ModelViewSet):
    queryset = TypeOfRoomModel.objects.all()
    serializer_class = TypeOfRoomModelSerializer


class RoomModelViewSet(ModelViewSet):
    queryset = RoomModel.objects.all()
    serializer_class = RoomModelSerializer
    filterset_fields = ['room_number', 'type_of_room', 'is_busy']


class RoomModelImageViewSet(ModelViewSet):
    queryset = RoomImageModel.objects.all()
    serializer_class = RoomImageModelSerializer