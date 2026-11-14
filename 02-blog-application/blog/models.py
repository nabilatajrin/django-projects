from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    slugs = models.SlugField(null=True)
    content = models.TextField(null=True, blank=True)
