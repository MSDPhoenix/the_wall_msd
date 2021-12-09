from django.db import models
from app_folder.models import User

class Message(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    deletable = models.BooleanField(default=False)

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, related_name="user_comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message,related_name="message_comments", on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    deletable = models.BooleanField(default=False)
