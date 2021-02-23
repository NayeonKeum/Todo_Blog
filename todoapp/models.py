from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    title = models.CharField(help_text="Post title", max_length=100, blank=False, null=False, default="Enter title")
    contents = models.TextField(help_text="post contents", blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True, help_text="post created date")
    updated_at=models.DateTimeField(auto_now=True, help_text="post updated date")

class Comment(models.Model):
    id = models.BigAutoField(help_text="Comment ID", primary_key=True)
    post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")
    contents = models.TextField(help_text="Comment contents", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, help_text="post created date")
    updated_at=models.DateTimeField(auto_now=True, help_text="post updated date")
