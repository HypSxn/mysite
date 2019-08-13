from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>',views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_id>', views.blogs_with_type, name='blogs_with_type'),
    ]