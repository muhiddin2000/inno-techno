from django.db import models
from .choices import RoomType, Book
from Accounts.models import CustomUser


class OrderModel(models.Model):
    room_type = models.CharField(max_length=100, choices=RoomType.choices)
    room_number = models.IntegerField()
    status = models.CharField(max_length=100)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type_of_booking = models.CharField(max_length=100, choices=Book.choices)
    room_date = models.DateField()
    sum_of_people = models.IntegerField()

    def __str__(self):
        return self.room_type
