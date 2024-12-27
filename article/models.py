from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:article category', args=[self.slug, ])

    def __str__(self):
        return f'{self.title}'


class ArticleTags(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:article tag', args=[self.slug,])

    def __str__(self):
        return f'{self.title}'


class Article(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    tag = models.ManyToManyField(ArticleTags, related_name='tags')
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField('article/images/%m/%d/')
    description = RichTextField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:article detail', args=[self.slug, ])

    def __str__(self):
        return f'{self.author} - {self.title} - {self.category}'
