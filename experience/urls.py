from django.urls import include, path
from rest_framework import routers
from .views import ExperienceViewSet
router = routers.DefaultRouter()
router.register('', ExperienceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
