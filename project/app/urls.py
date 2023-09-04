from django.urls import path
from django.views.generic.base import TemplateView
from app import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('add', views.addStaff, name="addStaff"),
    path('delete/<id>', views.deleteStaff, name="deleteStaff"),
    path('edit/<id>', views.editStaff, name="editStaff"),
]
