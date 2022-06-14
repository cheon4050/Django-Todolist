from django.urls import path

from todo_main import views

urlpatterns = [
    path('', views.index, name='index')
]