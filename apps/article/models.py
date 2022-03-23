from django.db import models

from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    image = models.ImageField(upload_to='article/images')
    creation_date = models.DateField(_('creation_date'), auto_now_add=True)
    tags = TaggableManager(_('tag'))
    content = RichTextField(_('content'))

    class Meta:
        ordering = ["-creation_date"]
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        return self.title
