from django.db import models


from account.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)
    upvote = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    


    def __str__(self) -> str:
        return f"{self.title}  {self.create_date}"
    


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content[:20]
