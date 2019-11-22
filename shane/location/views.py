
from django.shortcuts import render
from location.models import Country_group
from location.models import Visa_group
from location.models import Age_group
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import HTML
from django.db.models import Sum
from member.models import Country



def country_group(request, location):
    total_data = Country_group.objects.filter(location=location).values('country').annotate(Sum('country_total')).order_by('-country_total__sum')
    gender_m = Country_group.objects.filter(location=location, gender='남').order_by('-country_total')
    gender_f = Country_group.objects.filter(location=location, gender='여').order_by('-country_total')


    total_countries = 0

    for j in range(9,len(total_data)):
        total_countries = total_countries + total_data[j]['country_total__sum']


    gender_m_sum=0
    gender_f_sum=0

    for i in range(9,len(gender_m)):
        gender_m_sum = gender_m_sum + gender_m[i].country_total
        gender_f_sum = gender_f_sum + gender_f[i].country_total

    country_list = Country.objects.all().order_by('country')

    list_gender = {'gender_m':gender_m, 'gender_f':gender_f, 'gender_f_sum':gender_f_sum, 'gender_m_sum':gender_m_sum,'total_data':total_data, 'total_countries':total_countries,'country_list':country_list}

    return render(request, 'country_group/country_group.html', list_gender)


def visa_group(request, location):
    total_visa = Visa_group.objects.filter(location=location).values('visa_type').annotate(Sum('visa_total')).order_by('-visa_total__sum')
    visa_m = Visa_group.objects.filter(location=location, gender='남').order_by('-visa_total')
    visa_f = Visa_group.objects.filter(location=location, gender='여').order_by('-visa_total')


    total_visa_countries = 0

    for j in range(9, len(total_visa)):
        total_visa_countries =  total_visa_countries + total_visa[j]['visa_total__sum']


    visa_m_sum = 0
    visa_f_sum = 0

    for i in range(9, len(visa_m)):
        visa_m_sum = visa_m_sum + visa_m[i].visa_total
        visa_f_sum = visa_f_sum + visa_f[i].visa_total

    list_visa = {'visa_m': visa_m, 'visa_f': visa_f, 'visa_m_sum': visa_f_sum, 'visa_f_sum': visa_m_sum, 'total_visa': total_visa, 'total_visa_countries': total_visa_countries}

    return render(request, 'visa_group/visa_group.html', list_visa)


def age_group(request, location):
    total_age = Age_group.objects.filter(location=location).values('age_arange').annotate(Sum('age_total')).order_by('-age_total__sum')
    age_m = Age_group.objects.filter(location=location, gender='남').order_by('-age_total')
    age_f = Age_group.objects.filter(location=location, gender='여').order_by('-age_total')


    total_age_arange = 0

    for j in range(9, len(total_age)):
        total_age_arange = total_age_arange + total_age [j]['age_total__sum']


    age_m_sum = 0
    age_f_sum = 0

    for i in range(9, len(age_m)):
        age_m_sum = age_m_sum + age_m[i].age_total
        age_f_sum = age_f_sum + age_f[i].age_total

    age_visa = {'age_m': age_m, 'age_f': age_f, 'age_m_sum': age_m_sum, 'age_f_sum': age_f_sum,'total_age': total_age, 'total_age_arange': total_age_arange}

    return render(request, 'age_group/age_group.html',age_visa)