from django.contrib import admin

# Register your models here.

from .models import Post, Quote

admin.site.register(Post)
admin.site.register(Quote)