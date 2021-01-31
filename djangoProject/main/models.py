from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(models.Model):

    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class BlogPost(models.Model):

    blog_category = models.ForeignKey(BlogCategory, verbose_name="Имя категории", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название поста")
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=500, verbose_name="Описание", default=None)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='media/blog_posts/')
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
