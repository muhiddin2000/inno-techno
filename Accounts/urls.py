
from .views import RegisterAPI,LoginAPI,UserUpdate
from knox import views as knox_views
from django.urls import path

app_name = 'Accounts'
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('update/<int:pk>/', UserUpdate.as_view(), name='update'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
