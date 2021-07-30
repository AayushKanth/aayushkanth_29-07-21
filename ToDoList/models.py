from django.db import models
from django.utils import timezone

class ToDoList(models.Model):
    #head=models.lable("To-Do Creator")
    title=models.CharField(max_length=120)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
# Create your models here.
