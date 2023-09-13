# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Blog, BlogPostCount

@receiver(post_save, sender=Blog)
@receiver(post_delete, sender=Blog)
def update_blog_post_count(sender, instance, **kwargs):
    # Count the total number of blog posts and update the BlogPostCount model
    blog_post_count, _ = BlogPostCount.objects.get_or_create(pk=1)
    blog_post_count.count = Blog.objects.count()
    blog_post_count.save()
