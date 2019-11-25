from django.urls import path
from exchange_rate import views

urlpatterns = [
    # 환율정보 화면 경로
    path('', views.exchange_rate, name='exchange_rate'),
]
