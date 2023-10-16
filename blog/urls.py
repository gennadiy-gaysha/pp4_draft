from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetails.as_view(), name='post-details'),
    path('create_post/', views.CreatePost.as_view(), name='create-post'),
    path('post/update/<slug:slug>/', views.UpdatePost.as_view(), name='update-post'),
    path('post/delete/<slug:slug>/', views.DeletePost.as_view(), name='delete-post'),
    path('search_country/', views.search_country, name='search-country'),
    path('<slug:slug>/', views.ShowCountry.as_view(), name='show-country'),

]
