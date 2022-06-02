from rest_framework.serializers import ModelSerializer
from .models import OrderModel


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['id', 'room_type', 'room_number', 'status', 'user_id', 'type_of_booking', 'room_date',
              'sum_of_people']


class OrderModelStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['id', 'status']
