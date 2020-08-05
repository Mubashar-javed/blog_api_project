from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('', views.PostViewSet)

urlpatterns = router.urls
