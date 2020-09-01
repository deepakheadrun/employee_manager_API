from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.ExperienceList.as_view()),
    path('<int:id>/', views.ExperienceDetail.as_view()),
]