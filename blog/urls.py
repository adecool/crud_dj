from django.urls import path
from blog import views

from . views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name= 'post_edit'),
    path('restricted/', views.restricted, name='restricted'),
    path('post/change_password/', views.change_password, name='change_password'),
    path('post/logout', views.logout, name='logout'),
    path('post/login/', views.user_login, name= 'login'),
    path('post/register/', views.BlogSignUp, name= 'register'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name = 'home'),

    
]