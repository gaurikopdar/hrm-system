from django.db import models
from department.models import Department

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name