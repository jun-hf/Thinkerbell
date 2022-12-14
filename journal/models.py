from tabnanny import verbose
from django.db import models

# Create your models here.

class Log(models.Model):
    content = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Entry(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.content 


