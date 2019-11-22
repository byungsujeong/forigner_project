from django.urls import path
from bbs import views

urlpatterns = [
    # 게시판 home(게시물 전체 리스트) 경로
    path('', views.bbs, name='bbs'),
    # 게시물 상세 페이지(flag는 댓글 수정 시 form 변경을 위함) 경로
    path('content/<int:id>/<int:flag>', views.content, name='content'),
    # 게시물 작성 페이지 경로
    path('postPage/<str:country>', views.postPage, name='postPage'),
    # 게시물 insert처리 경로
    path('post', views.post, name='post'),
    # 게시물 댓글 insert처리 경로
    path('content/review', views.review),
    # 게시물 수정페이지 경로
    path('content/bbs_update', views.bbs_update),
    # 게시물 update처리 경로
    path('content/do_update', views.do_update),
    # 게시물 delete처리 경로
    path('content/bbs_delete', views.bbs_delete),
    # 댓글 delete처리 경로
    path('content/review_delete', views.review_delete),
    # 댓글 수정 시 페이지 form 변경하기 위한 경로(flag 값 변경하여 넘기기)
    path('content/review_update', views.review_update),
    # 댓글 update처리 경로
    path('content/do_review_update', views.do_review_update),
]
