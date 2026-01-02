from django.shortcuts import render
from blog.models import BlogPost

def home_view(request):
    recent_posts = BlogPost.objects.order_by('-created_at')[:5]  # Show last 5 posts
    return render(request, 'home/home.html', {
        'message': 'Hello, World! Welcome to my Django home page.',
        'recent_posts': recent_posts,
    })