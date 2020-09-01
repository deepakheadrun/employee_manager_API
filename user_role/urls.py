from django.urls import path,include
from user_role import views
urlpatterns = [
    path('', views.UserRoleView.as_view()),
   
]