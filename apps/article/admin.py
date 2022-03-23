from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    search_fields = (
        "tags__name",
    )

admin.site.register(Article, ArticleAdmin)