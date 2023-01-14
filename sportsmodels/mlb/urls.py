from django.urls import path

from . import views

## fixes namespace collision
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]