from django.urls import path
from .views import (
    add_department,
    delete_department,
    list_departments,
    update_department,
    admin_login
)

urlpatterns = [
    path('login/', admin_login),

    path('add-department/', add_department),

    path('departments/', list_departments),
    path('list-department/', list_departments),

    path('update-department/<int:pk>/', update_department),

    path('delete-department/<int:pk>/', delete_department),
]