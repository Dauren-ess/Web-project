from django.contrib import admin

# Register your models here.
from .models import Article, Comment

# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_text', 'pub_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'comment_text', 'article')
