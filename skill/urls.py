from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.SkillList.as_view()),
    path('<int:id>/', views.SkillDetail.as_view()),
]