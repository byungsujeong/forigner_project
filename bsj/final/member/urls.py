from django.urls import path
from member import views

urlpatterns = [
    # 회원가입 화면 경로
    path('', views.join),
    # 회원가입처리(insert) 경로
    path('insert', views.insert),
    # 로그인 화면 경로
    path('login', views.login),
    # 로그아웃 처리(del session) 경로
    path('logout', views.logout),
    # 로그인처리 화면(session) 경로
    path('check', views.check),
    # 회원정보 화면 경로
    path('member_info/<str:mid>', views.member_info),
    # 회원정보 update처리 경로
    path('update', views.update),
    # id중복확인, pw일치 확인, email형식확인 ajax처리 경로
    path('overlapcheck', views.overlapcheck),
    path('delete', views.delete),
]