from django.shortcuts import render, redirect
from member.models import Member
from member.models import Country


def join(request):
    data = Country.objects.all().order_by('country')
    list = {'list':data}
    return render(request, 'member/join.html', list)

def insert(request):
    data = request.POST
    m = Member(mid=data['mid'], pw=data['pw'], nickname=data['nickname'], gender=data['gender'], country=data['country'], email=data['email'])
    m.save()
    return redirect(join)

def login(request):
    return render(request, 'member/login.html')

def logout(request):
    del request.session['mid']
    return render(request, 'member/login.html')

def check(request):
    data = request.POST
    session = Member.objects.filter(mid=data['mid'])

    try:
        if session[0].pw == data['pw']:
            request.session['mid'] = data['mid']
            return render(request, 'home.html')
        else:
            return redirect(login)
    except:
        return redirect(login)

def member_info(request, mid):
    data = Member.objects.filter(mid=mid)[0]
    info = {'info':data}
    return render(request, 'member/member_info.html', info)

def update(request):
    data = request.POST
    Member.objects.filter(mid=data['mid']).update(pw=data['pw'],nickname=data['nickname'],gender=data['gender'],country=data['country'],email=data['email'])
    return render(request, 'home.html')

def map(request):
    return render(request,'member/mapping.html')