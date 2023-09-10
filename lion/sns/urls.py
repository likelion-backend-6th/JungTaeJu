from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'sns'

# urlpatterns = [
#     path('', views.user_list, name='user_list'),
# ]
router = DefaultRouter()
router.register("user", views.UserViewSet, basename="user")
urlpatterns = [
    path('', include(router.urls)),
]