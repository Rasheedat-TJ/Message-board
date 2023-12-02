from django.db import models

# Create your models here.

class Post(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Quote(models.Model):
    quote = models.CharField(max_length=255)

    def __str__(self):
        return self.quote