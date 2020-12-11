from datetime import timezone
from django.db import models


class Complaints(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    priority = models.PositiveIntegerField
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
