import datetime
from django.conf import settings
from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title