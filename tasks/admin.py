from django.contrib import admin

# Register your models here.
from . models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', 'due_date')

admin.site.register(Task, TaskAdmin)