from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),  # Add this line
    path('author/', include('author.urls', namespace='author')),
    path('', include('blog.urls', namespace='blog')),
]

