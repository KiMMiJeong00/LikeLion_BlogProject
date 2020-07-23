from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blog , name="blog"),
    path('<int:blog_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name='create'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
    path('update/<int:blog_id>', views.update, name='update'),
    path('comment/<int:blog_id>',views.comment,name='comment'),
    path('commnet/delete/<int:comment_id>',views.comment_delete,name='comment_delete'),
    path('like/<int:blog_id>',views.post_like,name='post_like'),#like라는 url이 들어왔을 때 post_like라는걸 만들겠다.
]
