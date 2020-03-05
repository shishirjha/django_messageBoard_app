from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    # returns the post as the first 50 characters written in the message.
    def __str__(self):
        return self.text[:50]
