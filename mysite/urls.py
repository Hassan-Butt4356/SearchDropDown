from dropdownSearch.views import (
    AllPosts,
    CreatePost
)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',AllPosts.as_view(),name='home'),
    path('create/',CreatePost.as_view(),name='create'),
]
