
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from .models import OrderModel
from .serializers import OrderModelSerializer,OrderModelStatusSerializer
from .permissions import IsAuthorOrReadOnly


# POST

class OrderModelCreateAPIView(CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer


class OrderModelListAPIView(ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAdminUser)


class OrderModelDeleteAPIView(DestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (IsAdminUser,)


class OrderModelDetailAPIView(RetrieveAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (IsAdminUser,)


class OrderModelEditAPIView(RetrieveUpdateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (IsAdminUser,)


class OrderModelEditStatusAPIView(RetrieveUpdateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelStatusSerializer
    permission_classes = (IsAdminUser,)
