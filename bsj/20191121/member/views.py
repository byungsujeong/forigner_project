from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import Member
from member.models import Country

# Create your views here.
# class Join(CreateView):
#     model = Member
#     fields = ['mid', 'pw', 'nickname', 'gender', 'country', 'email']
#     template_name = 'member/join.html'
#
#     def form_valid(self, form):
#         if form.is_valid():
#             form.instance.save()
#             return redirect('/')
#         else:
#             return self.render_to_response({'form': form})

def join(request):
    data = Country.objects.all().order_by('country')
    list = {'list':data}
    return render(request, 'member/join.html', list)

def insert(request):
    data = request.POST
    m = Member(mid=data['mid'], pw=data['pw'], nickname=data['nickname'], gender=data['gender'], country=data['country'], email=data['email'])
    m.save()
    return render(request,'home.html')

def login(request):
    return render(request, 'member/login.html')

def logout(request):
    del request.session['mid']
    return render(request, 'member/login.html')

def check(request):
    data = request.POST
    session = Member.objects.filter(mid=data['mid'])
    flag = 0

    try:
        if session[0].pw == data['pw']:
            request.session['mid'] = data['mid']
            return render(request, 'home.html')
        else:
            flag = 2
            dic_flag={'flag':flag}
            return render(request, 'member/login.html', dic_flag)
    except:
        flag = 1
        dic_flag = {'flag': flag}
        return render(request, 'member/login.html', dic_flag)

def member_info(request, mid):
    data = Member.objects.filter(mid=mid)[0]
    data2 = Country.objects.all().order_by('country')
    info = {'info':data, 'list':data2}
    return render(request, 'member/member_info.html', info)

def update(request):
    data = request.POST
    Member.objects.filter(mid=data['mid']).update(pw=data['pw'],nickname=data['nickname'],gender=data['gender'],country=data['country'],email=data['email'])
    return render(request, 'home.html')

def overlapcheck(request):
    data = request.GET
    m = Member.objects.filter(mid=data['mid'])
    try:
        if m[0].mid == data['mid']:
            data=1
    except:
        data=0
    return HttpResponse(data)
