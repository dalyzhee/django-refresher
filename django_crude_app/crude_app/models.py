from turtle import title
from unicodedata import name
from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=200, default="levis")
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.text
