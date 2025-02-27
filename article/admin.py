from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ArticleTagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'body', 'created')
    raw_id_fields = ('author', 'article',)


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.ArticleTags, ArticleTagsAdmin)
