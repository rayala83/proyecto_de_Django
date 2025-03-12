#from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer
from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "bienvenido a la API de taareas. Visite /api/para usar la API."})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer