from . import views
from django.urls import path
app_name = 'blog-app'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog-post.html', views.about, name='about'),
]