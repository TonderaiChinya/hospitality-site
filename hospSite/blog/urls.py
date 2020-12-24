from django.urls import path
from . import views
# from .views import HomeView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

# urlspatterns = [
#     path('', HomeView.as_view(), name="home"),
#
# ]