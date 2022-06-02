from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


# Create your models here.

class TypeOfRoomModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return self.name


class RoomModel(models.Model):
    room_number = models.PositiveIntegerField(unique=True, verbose_name=_('room_number'), null=True)
    type_of_room = models.ForeignKey(TypeOfRoomModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('type'))
    is_busy = models.BooleanField(default=False, null=True, blank=True, verbose_name=_('is_busy'))
    about = RichTextField(verbose_name=_('about'))
    booking_from_time = models.DateTimeField(null=True, blank=True, verbose_name=_('booking_from_time'))
    booking_until_time = models.DateTimeField(null=True, blank=True, verbose_name=_('booking_until_time'))

    def __str__(self):
        return str(self.room_number)


class RoomImageModel(models.Model):
    images = models.ImageField(upload_to='images/', verbose_name=_('images'), null=True)
    room_id = models.ForeignKey(RoomModel, on_delete=models.CASCADE, verbose_name=_('room_id'))

    def __str__(self):
        return str(self.room_id)