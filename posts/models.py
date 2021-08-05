from django.db import models
from django.db.models.base import Model

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:20]
