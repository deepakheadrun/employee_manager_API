from django.urls import include, path
from rest_framework import routers
from .views import SkillViewSet
router = routers.DefaultRouter()
router.register('', SkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
