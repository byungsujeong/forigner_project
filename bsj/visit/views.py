from django.shortcuts import render
import matplotlib
import matplotlib.pyplot as plt
from visit.models import Visit
from visit.models import Yyyy
from member.models import Country

# Create your views here.
def visit(request):
    data = Visit.objects.filter(country=request.GET['country'], yyyymm__startswith=request.GET['yyyy'])
    list1 = []
    list2 = []
    for i in data:
        list1.append(i.total)
        list2.append(i.yyyymm.replace('월','').replace(request.GET['yyyy']+'.',''))
    matplotlib.use('Agg')
    plt.xlabel('month')
    plt.ylabel('total')
    plt.plot(list2, list1)
    plt.savefig('visit/static/graph.png')
    plt.close()
    img_url = '/static/graph.png'
    data2 = Country.objects.all().order_by('country')
    data3 = Yyyy.objects.all().order_by('yyyy')
    list = {'list': data, 'list2':data2, 'list3':data3,'list4':request.GET['yyyy'], 'img_url':img_url}
    return render(request, 'visit/visit.html', list)