from django.urls import  path, re_path

from Alumnos import views

urlpatterns = [
    re_path(r'^alumnosModel_url', views.AlumnosModelView.as_view()),
    path('alumnos_get', views.AlumnosModelView.as_view()),
    path('alumnos_delete/<slug:id>', views.AlumnosModelView.as_view()),
    path('alumnos_edit/<slug:id>', views.AlumnosModelView.as_view())
]

