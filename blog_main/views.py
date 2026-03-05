from django.shortcuts import render
from blogs.models import Category, Blog, SocialLinks

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published')
    simple_posts = Blog.objects.filter(is_featured=False, status='Published')

    if request.method == 'POST':
        pass
    
    context = {
        'featured_posts': featured_posts,
        'simple_posts': simple_posts,
    }
    return render(request, 'home.html', context)