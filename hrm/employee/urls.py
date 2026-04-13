from django.urls import path
from .views import add_employee, list_employees, delete_employee, update_employee

urlpatterns = [
    path('add-employee/', add_employee),
    path('list-employee/', list_employees),
    path('delete-employee/<int:pk>/', delete_employee),
    path('update-employee/<int:pk>/', update_employee),
]