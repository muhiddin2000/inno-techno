
from .models import CommentModel
from .serializers import CommentModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import filters


class CommentCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelSerializer


class CommentModelListAPIView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['comment', ]
