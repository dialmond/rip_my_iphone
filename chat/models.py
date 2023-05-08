from django.db import models
from django.utils import timezone

from accounts.models import User

# a message has some text, and someone who sends it
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name="messages")
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return self.content
