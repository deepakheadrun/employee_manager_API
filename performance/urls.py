from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.PerformanceList.as_view()),
    path('<int:id>/', views.PerformanceDetail.as_view()),
]