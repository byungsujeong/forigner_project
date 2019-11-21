from django.urls import path
from visit import views

urlpatterns = [
    path('', views.visit),
]
