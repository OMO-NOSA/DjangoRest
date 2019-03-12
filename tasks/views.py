from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import TaskSerializer
from . models import Task

# from rest_framework import generics
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

