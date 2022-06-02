from django.urls import path
from .views import OrderModelCreateAPIView, OrderModelListAPIView, OrderModelDeleteAPIView, \
    OrderModelDetailAPIView, OrderModelEditAPIView,OrderModelEditStatusAPIView

app_name = 'Order'

urlpatterns = [
    path('create/', OrderModelCreateAPIView.as_view(), name='create_api_view'),
    path('', OrderModelListAPIView.as_view(), name='list_api_view'),
    path('delete/<int:pk>/', OrderModelDeleteAPIView.as_view(), name='delete_api_view'),
    path('detail/<int:pk>/', OrderModelDetailAPIView.as_view(), name='detail_api_view'),
    path('edit/<int:pk>/', OrderModelEditAPIView.as_view(), name='edit_api_view'),
    path('order/status/<int:pk>/', OrderModelEditStatusAPIView.as_view(), name='edit_status_api_view'),
]
