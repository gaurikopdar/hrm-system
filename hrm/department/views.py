from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer 

@api_view(['POST'])
def add_department(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Department Added Successfully"})
    return Response(serializer.errors)

@api_view(['GET'])
def list_departments(request):
    departments = Department.objects.filter(status=True)
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({"error":"Department not found"})
    
    serializer = DepartmentSerializer(department, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Department Updated"})
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_department(request,pk):
    try:
        department = Department.objects.get(pk=pk)
        department.status = False
        department.save()
        return Response({"message": "Department Deleted"})
    except Department.DoesNotExist:
        return Response({"error": "Department not found"})