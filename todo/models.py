from django.db import models
from datetime import datetime
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.now)
