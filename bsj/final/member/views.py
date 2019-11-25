from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import Member
from member.models import Country

# 회원가입 화면 정의
def join(request):
    # 나라선택 위한 리스트
    data = Country.objects.all().order_by('country')
    list = {'list':data}
    return render(request, 'member/join.html', list)

# 회원가입 처리 정의
def insert(request):
    data = request.POST
    m = Member(mid=data['mid'], pw=data['pw'], nickname=data['nickname'], gender=data['gender'], country=data['country'], email=data['email'])
    m.save()
    return render(request,'home.html')

# 로그인 화면 정의
def login(request):
    return render(request, 'member/login.html')

# 로그와웃 처리 정의
def logout(request):
    # 세션에 등록된 mid값을 삭제
    del request.session['mid']
    return render(request, 'member/login.html')

# 로그인 처리 정의
def check(request):
    data = request.POST
    # 로그인 요청 시 넘어오는 id를 조건으로 데이터 가져오기
    session = Member.objects.filter(mid=data['mid'])
    # flag default 0으로 지정
    flag = 0

    # 가져온 데이터 인덱스 0값을 가져왔을 때 오류가 발생하면 아이디가 없는 것(try-except)
    try:
        # 가져온 데이터의 pw와 입력한 pw가 일치한경우 아이디를 세션에 등록하여 로그인 처리
        if session[0].pw == data['pw']:
            request.session['mid'] = data['mid']
            return render(request, 'home.html')
        # pw가 다른경우 flag2를 넘겨 pw가 틀리다는 alert 발생
        else:
            flag = 2
            dic_flag = {'flag': flag}
            return render(request, 'member/login.html', dic_flag)
    # id데이터가 없는 경우
    except:
        # flag1을 넘겨 없는 id라는 alert 발생
        flag = 1
        dic_flag = {'flag': flag}
        return render(request, 'member/login.html', dic_flag)

# 회원정보 화면 정의
def member_info(request, mid):
    data = Member.objects.filter(mid=mid)[0]
    data2 = Country.objects.all().order_by('country')
    info = {'info':data, 'list':data2}
    return render(request, 'member/member_info.html', info)

# 회원정보 수정(update) 정의
def update(request):
    data = request.POST
    Member.objects.filter(mid=data['mid']).update(pw=data['pw'],nickname=data['nickname'],gender=data['gender'],country=data['country'],email=data['email'])
    return render(request, 'home.html')

# id 중복확인 정의
def overlapcheck(request):
    # ajax로 넘김 데이터 get
    data = request.GET
    m = Member.objects.filter(mid=data['mid'])
    # 아이디가 있어서 오류가 나지 않으면 data1
    try:
        if m[0].mid == data['mid']:
            data=1
    # 아이디가 없어서 오류가 발생하면 data0
    except:
        data=0
    # data를 ajax success result값으로 받기 위해 HttpResponse로 data 반환
    return HttpResponse(data)

def delete(request):
    del request.session['mid']
    data = request.GET
    Member.objects.filter(mid=data['mid']).delete()
    return render(request,'home.html')