from rest_framework.routers import SimpleRouter
from .views import TypeOfRoomViewSet, RoomModelViewSet, RoomModelImageViewSet


app_name = 'room'

router = SimpleRouter()

router.register('type', TypeOfRoomViewSet, basename='type_of_room')
router.register('images', RoomModelImageViewSet, basename='room_images')
router.register('', RoomModelViewSet, basename='rooms')

urlpatterns = router.urls