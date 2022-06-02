from django.contrib import admin
from .models import TypeOfRoomModel, RoomModel, RoomImageModel
from modeltranslation.admin import TranslationAdmin


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(RoomModel)
class RoomModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'type_of_room']


@admin.register(TypeOfRoomModel)
class TypeOfRoomModelAdmin(MyTranslationAdmin):
    list_display = ['name']


@admin.register(RoomImageModel)
class RoomImageModelAdmin(admin.ModelAdmin):
    list_display = ['id']
