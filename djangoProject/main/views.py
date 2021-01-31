from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from .models import BlogCategory, BlogPost

from bs4 import BeautifulSoup


def index(request):
    category_list = BlogCategory.objects.all()
    return render(request, 'index.html', {'category': category_list})


def blog(request):
    category_list = BlogCategory.objects.all()
    posts_list = BlogPost.objects.all()
    posts = posts_list.order_by('-id')
    paginator = Paginator(posts, 9)

    page_number = request.GET.get('page')
    page_numbers = [page_number, f'{int(page_number) + 1}', f'{int(page_number) + 2}'] if paginator.num_pages != 1 and \
        paginator.num_pages != 2 else ['1', '2'] if paginator.num_pages == 2 else ['1']
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'category': category_list, 'posts': page_obj, 'page': page_numbers})


def category(request, category_slug):
    category_list = BlogCategory.objects.all()
    b = BlogCategory.objects.get(slug=category_slug)
    try:
        posts = b.blogpost_set.order_by('id')
    except Exception as e:
        print(e)
        raise Http404("Пост не найден!")
    posts = posts.order_by('-id')
    paginator = Paginator(posts, 9)

    page_number = request.GET.get('page')
    page_numbers = [page_number, f'{int(page_number) + 1}', f'{int(page_number) + 2}'] if paginator.num_pages != 1 and \
        paginator.num_pages != 2 else ['1', '2'] if paginator.num_pages == 2 else ['1']
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'category': category_list, 'posts': page_obj, 'page': page_numbers})


def post(request, category_slug, post_slug):
    category_list = BlogCategory.objects.all()
    post_obj = BlogPost.objects.get(slug=post_slug)
    soup = BeautifulSoup(post_obj.content)
    post_dropdown_item = ' '.join(["" if i.get("id") is None else i.get('id') for i in soup.find_all()]).split()
    return render(request, 'post.html', {'category': category_list, 'post': post_obj,
                                         'dropdown_item': post_dropdown_item})
