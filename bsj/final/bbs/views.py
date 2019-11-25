from django.shortcuts import render, redirect
from bbs.models import Bbs
from bbs.models import Review
from member.models import Country
from member.models import Member

# Create your views here.
# 게시판페이지 정의
def bbs(request):
    # insert 또는 delete처리 시 redirect 처리하는 경우 request 값이 없으므로 오류 처리하기 위한 try-except
    try:
        # 게시물 전체보기와 특정나라 글만 보기 구분하기 위한 if-else
        if request.GET['country'] == '전체':
            data = Bbs.objects.all().order_by('-id')
        else:
            data = Bbs.objects.filter(country=request.GET['country'])
    except:
        data = Bbs.objects.all().order_by('-id')
    # 선택한 나라 게시판으로 이동하기 위한 combobox 생성할 나라 리스트
    data2 = Country.objects.all().order_by('-country').reverse() # -(dash)랑 reverse 둘다 기억하려고 두번씀
    # request가 없는 경우 전체 게시판으로 가기 위한 try-except
    try:
        list = {'list': data, 'list2':data2,'country':request.GET['country']}
    except:
        list = {'list': data, 'list2': data2, 'country':'전체'}
    return render(request, 'bbs/bbs.html', list)

# 게시물 상세 페이지 정의(flag는 댓글 수정 시 form 변경을 위함)
def content(request,id, flag):
    # 게시물 상세내용
    data = Bbs.objects.filter(id=id)[0]
    # 해당 게시물의 댓글 리스트
    data2 = Review.objects.filter(oid=id).order_by('-id')
    list = {'content':data, 'review':data2, 'flag':flag}
    return render(request, 'bbs/content.html', list)

# 게시글 작성 페이지 정의(country는 선택한 나라 게시판에서 게시글 작성 시 해당 나라로 insert되게 하기 위함)
def postPage(request, country):
    # 전체 게시판에서 작성하는 경우 나라 선택하도록 combobox 생성할 나라 리스트
    data = Country.objects.all().order_by('country')
    list = {'list':data,'country':country}
    return render(request, 'bbs/postPage.html',list)

# 게시글 insert처리 정의
def post(request):
    data = request.POST
    m = Member.objects.filter(mid=data['mid'])[0]
    b = Bbs(title=data['title'], content=data['content'], country=data['country'], mid=m.mid, user_nick=m.nickname, user_country=m.country)
    b.save()
    return redirect(bbs)

# 댓글 insert처리 정의
def review(request):
    # flag가 0일 때 댓글 form이 모두 수정 불가능한 읽기전용 데이터로 template에 반영하기 위함
    flag=0
    data = request.POST
    m = Member.objects.filter(mid=request.session['mid'])[0]
    Review(oid=data['oid'], mid=m.mid, user_nick=m.nickname, review_content=data['review_content']).save()
    return redirect(content, data['oid'],flag)

# 게시물 수정 페이지 정의
def bbs_update(request):
    data = request.GET
    b = Bbs.objects.filter(id=data['id'])[0]
    list = {'list':b}
    return render(request, 'bbs/update_page.html', list)

# 게시물 update처리 정의
def do_update(request):
    # flag가 0일 때 댓글 form이 모두 수정 불가능한 읽기전용 데이터로 template에 반영하기 위함
    flag=0
    data = request.POST
    Bbs.objects.filter(id=data['id']).update(title=data['title'], content=data['content'])
    return redirect(content, data['id'], flag)

# 게시물 delete처리 정의
def bbs_delete(request):
    data = request.GET
    Bbs.objects.filter(id=data['id']).delete()
    return redirect(bbs)

# 댓글 delete처리 정의
def review_delete(request):
    # flag가 0일 때 댓글 form이 모두 수정 불가능한 읽기전용 데이터로 template에 반영하기 위함
    flag=0
    data = request.GET
    Review.objects.filter(id=data['id']).delete()
    return redirect(content, data['oid'], flag)

# 댓글 수정 시 선택한 댓글 form변경 정의
def review_update(request):
    data = request.GET
    # 해당 댓글만 form 변경하도록 flag에 댓글 id 넣어 return
    flag = data['id']
    return redirect(content, data['oid'], flag)

# 댓글 update처리 정의
def do_review_update(request):
    # update가 완료 되면 flag를 다시 0으로 바꿔 form을 원래 형식(읽기전용)으로 바꿔주기 위함.
    flag = 0
    data = request.POST
    Review.objects.filter(id=data['id']).update(review_content=data['review_content'])
    return redirect(content, data['oid'], flag)