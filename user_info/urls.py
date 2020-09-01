from django.urls import include, path
from rest_framework import routers
from . import views
from .views import InfoViewSet
router = routers.DefaultRouter()
router.register('', InfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]