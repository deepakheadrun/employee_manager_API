from django.urls import include, path
from rest_framework import routers
from .views import CommentViewSet
router = routers.DefaultRouter()
router.register('', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
