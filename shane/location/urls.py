from django.urls import path
from location import views

urlpatterns = [
    path('<str:location>', views.country_group),
    path('visa_group/<str:location>', views.visa_group),
    path('age_group/<str:location>', views.age_group),
]
