from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view()),
	path('rest-auth/', include('rest_auth.urls')),
	path('authed-user/<str:tkn>/', views.token_owner),
    path('create/', views.create_task, name='create'),
    path('details/', views.task_detail, name='detail'),
]
