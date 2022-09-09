from django.db import models
import datetime

class Task(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=250)
    created_at = models.DateField(default=datetime.date.today)
     