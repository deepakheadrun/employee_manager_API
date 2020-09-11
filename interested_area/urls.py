from django.urls import include, path
from rest_framework import routers
from .views import InterestedAreaViewSet
router = routers.DefaultRouter()
router.register('', InterestedAreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
