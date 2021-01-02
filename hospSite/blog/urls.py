from django.urls import path
from . import views
from .views import like_post

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('like/', like_post, name='like-post'),
]

# urlspatterns = [
#     path('', HomeView.as_view(), name="home"),
#
# ]