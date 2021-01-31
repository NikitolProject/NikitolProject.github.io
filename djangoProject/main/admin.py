from django import forms
from django.contrib import admin
from .models import BlogCategory, BlogPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget


admin.site.register(BlogCategory)


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm


admin.site.register(BlogPost)
