from django.shortcuts import render, redirect
from django.views.generic import CreateView

from bbs.models import Bbs
from member.models import Country
from member.models import Member

# Create your views here.
def bbs(request):

    try:
        if request.GET['country'] == '전체':
            data = Bbs.objects.all()
        else:
            data = Bbs.objects.filter(country=request.GET['country'])
    except:
        data = Bbs.objects.all()
    data2 = Country.objects.all().order_by('-country').reverse() # -(dash)랑 reverse 둘다 기억하려고 두번씀
    try:
        list = {'list': data, 'list2':data2,'country':request.GET['country']}
    except:
        list = {'list': data, 'list2': data2, 'country':'전체'}
    return render(request, 'bbs/bbs.html', list)

def content(request,id):
    data = Bbs.objects.filter(id=id)[0]
    content = {'content':data}
    return render(request, 'bbs/content.html', content)

def postPage(request, country):
    data = Country.objects.all().order_by('country')
    list = {'list':data,'country':country}
    return render(request, 'bbs/postPage.html',list)

def post(request):
    data = request.POST
    m = Member.objects.filter(mid=data['mid'])[0]
    b = Bbs(title=data['title'], content=data['content'], country=data['country'], mid=m.mid, user_nick=m.nickname, user_country=m.country)
    b.save()
    return redirect(bbs)

# class Post(CreateView):
#     model = Bbs
#     fields = ['title', 'content']
#     template_name = 'bbs/post.html'
