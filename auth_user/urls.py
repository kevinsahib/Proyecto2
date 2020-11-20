from django.urls import  path, re_path

from auth_user import views

urlpatterns = [
    re_path(r'^auth_userModel_url', views.auth_userModelView.as_view())
]