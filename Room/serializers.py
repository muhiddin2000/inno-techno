from rest_framework import serializers
from .models import TypeOfRoomModel, RoomModel, RoomImageModel

class TypeOfRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfRoomModel
        fields = '__all__'

class RoomModelSerializer(serializers.ModelSerializer):
    # images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = RoomModel
        fields = '__all__'

class RoomImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImageModel
        fields = '__all__'