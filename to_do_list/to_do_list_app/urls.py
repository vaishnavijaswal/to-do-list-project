from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("add/",views.add_task,name='add_task'),
    path("add_task" , views.add_task_from, name="add_task_form"),
    path("delete_task/<int:id>",views.delete_task,name='delete'),
    path("edit/<int:id>",views.edit_task,name="edit_task"),
    path('edit_task/<int:id>',views.edit_task_form, name='edit_task_form'),
    path("toggle_task/<int:id>/", views.toggle_task, name="toggle_task"),
]