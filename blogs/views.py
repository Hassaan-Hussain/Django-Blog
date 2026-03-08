from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blog, Category, Comment
from django.db.models import Q

# Create your views here.

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)

def blog(request, slug):
    blog_post = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=blog_post)
    total_comments = Comment.objects.filter(blog=blog_post).count()
    if request.method == 'POST':
        new_comment = Comment.objects.create(comment=comment, blog=blog_post, user=request.user)
        comment = request.POST.get('comment')
        new_comment.save()
        return HttpResponseRedirect(request.path_info)
    context = {
        'blog_post': blog_post,
        'comments': comments,
        'total_comments': total_comments,
    }
    return render(request, 'single_blog_page.html', context)

def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        posts = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
        
        context = {
            'posts': posts,
            'keyword': keyword,
        }
        return render(request, 'search.html', context)