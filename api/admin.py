from django.contrib import admin
from .models import Post, Vote, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Vote)
admin.site.register(Comment)
