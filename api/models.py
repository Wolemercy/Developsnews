from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return f"{self.title}"


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post}"

    # def children(self):
    #     return Comment.objects.filter(parent=self)

    # @property
    # def is_parent(self):
    #     if self.parent is not None:
    #         return False

    #     return True
