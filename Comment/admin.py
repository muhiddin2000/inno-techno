from django.contrib import admin

from .models import CommentModel


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'rating']