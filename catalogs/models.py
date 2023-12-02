from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=200)
    published_year = models.IntegerField(default=2023)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title