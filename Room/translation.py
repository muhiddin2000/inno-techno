from .models import RoomModel, TypeOfRoomModel
from modeltranslation.translator import register, TranslationOptions


@register(RoomModel)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_number', 'type_of_room', 'is_busy', 'about', 'booking_from_time', 'booking_until_time')


@register(TypeOfRoomModel)
class TypeOfRoomTranslationOptions(TranslationOptions):
    fields = ('name')