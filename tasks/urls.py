from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view()),
	path('login',views.login, name='login'),
    path('create/', views.create_task, name='create'),
    path('details/', views.task_detail, name='detail'),
]
