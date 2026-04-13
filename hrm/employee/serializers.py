from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(
        source="department.dept_name",
        read_only=True
    )

    class Meta:
        model = Employee
        fields = '__all__'