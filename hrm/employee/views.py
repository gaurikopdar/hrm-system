from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['POST'])
def add_employee(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employee Added"})

    return Response(serializer.errors)


@api_view(['GET'])
def list_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response({"message": "Employee Deleted"})
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"})

@api_view(['PUT'])
def update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"})

    serializer = EmployeeSerializer(employee, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employee Updated"})

    return Response(serializer.errors)