from django.contrib import admin
from .models import Post, Comment


class CommentAdminInline(admin.TabularInline):
    model = Comment
    list_display = ('post', 'author', 'created_at')
    search_fields = ('author', 'content')
    extra = 0

class adminPost(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    inlines = [CommentAdminInline]

admin.site.register(Post, adminPost) 