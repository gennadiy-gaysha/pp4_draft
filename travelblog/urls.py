from django.contrib import admin
from django.urls import path, include

from blog.views import page_not_found, permission_denied

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('about.urls')),
    path('', include('blog.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('accounts.urls')),
]

handler404 = page_not_found
handler403 = permission_denied

