from datetime import timezone
from django.db import models


class Todos(models.Model):
    todo_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_name
    
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    reminder_time = models.DateTimeField()
    def save(self, *args, **kwargs):
        if not self.reminder_time.tzinfo:
            self.reminder_time = timezone.make_aware(self.reminder_time, timezone.get_current_timezone())
        super(Task, self).save(*args, **kwargs)

