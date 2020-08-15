from django.contrib import admin
from django.urls import include, path  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),  # new
    path('api/post/', include('post.urls')),  # new
    path('api/v1/', include('post.urls')),  # new
    path('api-auth/', include('rest_framework.urls')),  # new
]
