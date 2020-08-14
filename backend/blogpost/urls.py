from django.urls import path

from .views import DetailBlogpost, ListBlogpost

urlpatterns = [
    path('', ListBlogpost.as_view()),
    path('<int:pk>', DetailBlogpost.as_view()),

]
