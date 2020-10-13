from django.contrib import admin

from post.models import Post, Category, Comment, Reply

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'slug']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'status', 'created_at']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['reply', 'status', 'created_at']

admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Reply, ReplyAdmin)