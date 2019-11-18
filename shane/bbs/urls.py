from django.urls import path
from bbs import views

urlpatterns = [
    path('', views.bbs, name='bbs'),
    path('content/<int:id>', views.content, name='content'),
    path('postPage/<str:country>', views.postPage, name='postPage'),
    path('post', views.post, name='post')
]
