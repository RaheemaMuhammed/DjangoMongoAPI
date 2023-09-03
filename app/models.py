from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=500)
    posted_at=models.DateTimeField(auto_now_add=True)
