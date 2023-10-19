from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegisterNewAccount.as_view(), name='register'),
    path('edit_profile/', views.EditDetails.as_view(), name='edit-profile'),
    path('password/', views.ChangePassword.as_view(), name='change-password'),
    path('author_bio/<str:author_name>/', views.author_bio, name='author-bio'),
    path('create_profile/<str:username>/', views.CreateProfile.as_view(), name='create-profile'),
    path('update_profile/<str:username>/', views.UpdateProfile.as_view(), name='update-profile'),
]
