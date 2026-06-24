from pdb import post_mortem
import logging
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import pkg_resources
from .models import Post
from django.http import Http404

# Create your views here.
# posts = [
#      {"id": 1, "title": "Post 1", "content": "This is the content of post 1."},
#      {"id": 2, "title": "Post 2", "content": "This is the content of post 2."},
#      {"id": 3, "title": "Post 3", "content": "This is the content of post 3."},
#      {"id": 4, "title": "Post 4", "content": "This is the content of post 4."},   
#     ]
# The index view function returns a simple HttpResponse with a greeting message.
def index(request):
    blog_tittle = "Latest Posts"
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'blog_title': blog_tittle, 'posts': posts})

# The details view function takes a slug as a parameter and returns an HttpResponse that includes the post information in the message.
def details(request, slug):
    #post = next((item for item in Post if item == int(post_id)), None)

#getting data from database
    try:
        post = Post.objects.get(slug = slug)
        
    except Post.DoesNotExist:
        
        raise Http404("Post not found.")
        
    #logger = logging.getLogger("Testing")
    #logger.debug(f"Post variable is : {post}")
    return render(request, 'blog/details.html', {'post': post})

# The old_urls_redirect view function redirects to the new URLs view.
def old_urls_redirect(request):
    return redirect(reverse('blog:new_page_urls'))

# The new_urls_view function returns an HttpResponse indicating that this is the new URL for the blog.
def new_urls_view(request):
    return HttpResponse("This is the new URL for the blog.")
