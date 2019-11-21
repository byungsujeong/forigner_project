from django.urls import path
from exchange_rate import views

urlpatterns = [
    path('', views.exchange_rate, name='exchange_rate'),
]
