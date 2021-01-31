from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('blog/', views.blog, name='blog'),
  path('blog/category/<category_slug>/', views.category, name='category'),
  path('blog/category/<category_slug>/post/<post_slug>/', views.post, name='post'),
]


urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
