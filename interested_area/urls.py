from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.InterestedAreaList.as_view()),
    path('<int:id>/', views.InterestedAreaDetail.as_view()),
]