from rest_framework import serializers
from .models import CommentModel


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'
