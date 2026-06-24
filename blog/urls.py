from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("post/<str:slug>/", views.details, name='details'),
    
    #This (name) variable used to redirect old urls to new urls  by using reverse(), you can see that in the views.py file (old_urls_redirect view function).
    path("new_something_urls", views.new_urls_view, name='new_page_urls'),
    path("old_urls", views.old_urls_redirect, name='old_urls'),    
]