from django.shortcuts import render
from location.models import Country_group
from location.models import Visa_group
from location.models import Age_group
from django.db.models import Sum

# Create your views here.
def country_group(request, location):
    data = Country_group.objects.filter(location=location).values('country').annotate(Sum('country_total')).order_by('-country_total__sum')
    data1 = Country_group.objects.filter(location=location, gender='남')
    data2 = Country_group.objects.filter(location=location, gender='여')

    list = {'list':data1, 'list2':data2,'list3':data}
    return render(request, 'country_group/country_group.html',list)

def visa_group(request, location):
    data = Visa_group.objects.filter(location=location)
    list = {'list':data}
    return render(request, 'visa_group/visa_group.html',list)

def age_group(request, location):
    data = Age_group.objects.filter(location=location)
    list = {'list':data}
    return render(request, 'age_group/age_group.html',list)