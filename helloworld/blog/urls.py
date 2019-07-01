from django.urls import path
from . import views
urlpatterns=[
    path('', views.post, name="firstpost"),
    path('post/<int:pk>/', views.post_detail, name='list'),
    path('post/new/', views.post_new, name='post_new'),
]