from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# models.py

from django.db import models
from django.contrib.auth.models import User, Permission

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True) 

    class Meta:
        permissions = [
            ("can_create_blog", "Can create blog"),
            ("can_view_blog", "Can view blog"),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




    
class BlogPostCount(models.Model):
    count = models.PositiveIntegerField(default=0)