from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from .serializers import TaskSerializer
from . models import Task

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


@api_view()
def token_owner(request, tkn):
	owner_inst = Token.objects.get(key=tkn)
	owner = User.objects.get(pk=owner_inst.user_id)
	return Response({"user":owner.username})