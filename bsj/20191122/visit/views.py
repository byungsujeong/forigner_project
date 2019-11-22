from django.shortcuts import render
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
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
    df = pd.DataFrame({'month':list2,'total':list1})
    df_table = df.to_html()
    matplotlib.use('Agg')
    matplotlib.style.use('ggplot')
    plt.xlabel('month')
    plt.ylabel('total')
    plt.bar(list2, list1, color='skyblue')
    plt.plot(list2, list1, color='mediumblue')
    plt.savefig('visit/static/graph.png')
    plt.close()
    img_url = '/static/graph.png'
    data2 = Country.objects.all().order_by('country')
    data3 = Yyyy.objects.all().order_by('-yyyy')
    list = {'list': data, 'list2':data2, 'list3':data3,'list4':request.GET['yyyy'], 'img_url':img_url, 'df_table':df_table}
    return render(request, 'visit/visit.html', list)

def predict(request):
    data = request.GET
    pic_type1 = '/static/' + data['country'] + '_line+seasonal.png'
    pic_type2 = '/static/' + data['country']+'_whole.png'
    data2 = Country.objects.all().order_by('country')
    data3 = Yyyy.objects.all().order_by('-yyyy')
    pic_url = {'pic1':pic_type1,'pic2':pic_type2,'list':data,'list2':data2,'list3':data3}
    return render(request, 'visit/predict.html',pic_url)