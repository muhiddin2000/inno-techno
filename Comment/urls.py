from django.urls import path
from Comment.views import CommentCreateAPIView, CommentModelListAPIView

app_name = 'comment'

urlpatterns = [
    path('', CommentCreateAPIView.as_view(), name = 'create_comment'),
    path('all/', CommentModelListAPIView.as_view(), name='list_comment'),
]


