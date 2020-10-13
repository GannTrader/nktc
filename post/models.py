from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


STATUS = (
    ('active', 'active'),
    ('inactive', 'inactive')
)


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    image = models.FileField()
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default="inactive")


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace("đ", "d"))
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_query_name="tagPost")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default="inactive")

    def __str__(self):
        return self.comment


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default="inactive")



    def __str__(self):
        return self.reply