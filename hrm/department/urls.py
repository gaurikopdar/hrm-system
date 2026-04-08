from django.urls import path
from .views import add_department, delete_department, list_departments, update_department

urlpatterns = [
    path('add-department/', add_department),
    path('departments/', list_departments),
    path('update-department/<int:pk>/', update_department),
    path('delete-department/<int:pk>/', delete_department),
]