from django.urls import path, include

from todo_main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('create/',views.create_todo),
    path('delete/<int:pk>/',views.delete_todo),
    path('finish/<int:pk>/',views.finish_todo),
    path('finished/',views.finished_list)
]