from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.CommentList.as_view()),
    path('<int:id>/', views.CommentDetail.as_view()),
]