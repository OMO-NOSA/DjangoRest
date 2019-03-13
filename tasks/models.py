from django.db import models
from datetime import datetime
from accounts.models import CustomUser
class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=False)
    due_date = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return self.title