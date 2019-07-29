from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    topic_text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.topic_text}"

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    entry_text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.entry_text[:50]}..."
