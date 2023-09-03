from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.addStaff, name="addStaff"),
    path('delete/<id>', views.deleteStaff, name="deleteStaff"),
    path('edit/<id>', views.editStaff, name="editStaff"),
]
