from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from .serializers import TaskSerializer
from . models import Task
from . forms import TaskForm
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK

class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

@api_view()
def token_owner(request):
    for user in CustomUser.objects.all():
        token,_ = Token.objects.get_or_create(user=user)
	    #return Response({'token': token.key}, status=HTTP_200_OK)

CustomUser = get_user_model()

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            due_date = form.cleaned_data.get('due_date')
            form.save()
            return redirect('detail')
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form':form})

def task_detail(request):
    tasks = Task.objects.order_by('-due_date')

    context = {
        'task': tasks,
    }
    return render (request, 'tasks/task_detail.html', context)