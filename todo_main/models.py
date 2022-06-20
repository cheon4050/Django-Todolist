from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    todo = models.CharField(max_length=255, default='')
    finished = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.todo;
