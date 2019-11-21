from django.urls import path
from member import views

urlpatterns = [
    # path('', views.Join.as_view(), name='join'),
    path('', views.join),
    path('insert', views.insert),
    path('login', views.login),
    path('logout', views.logout),
    path('check', views.check),
    path('member_info/<str:mid>', views.member_info),
    path('update', views.update),
    path('overlapcheck', views.overlapcheck)
]