from django.urls import  path, re_path

from auth_user import views

urlpatterns = [
    re_path(r'^authuser', views.auth_userView.as_view()),
    path('authuserget', views.auth_userView.as_view())
]