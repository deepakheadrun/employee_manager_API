from django.urls import include, path
from rest_framework import routers
from .views import PerformanceViewSet
router = routers.DefaultRouter()
router.register('', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
