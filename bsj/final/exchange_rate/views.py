from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create your views here.
# 크롤링 정의
def exchange_rate(request):
    # 환율정보 url 경로
    url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
    # 공시 기준 일자 가져오기 위한 url 경로
    url2 = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
    result = requests.get(url)
    result2 = requests.get(url2)
    content = BeautifulSoup(result.content, 'html.parser')
    content2 = BeautifulSoup(result2.content, 'html.parser')
    table = content.select('div.tbl_area table.tbl_exchange tbody tr td')
    standard_date = content2.select('span.date')
    standard_bank = content2.select('span.standard')
    standard_round = content2.select('span.round>em')

    currency=[]
    basic = []
    cash_buy = []
    cash_sell = []
    remittance_send = []
    remittance_get = []
    conversion = []

    # 각 레코드는 7개의 항목으로 되어 있음(통화명, 매매기준율, 현금(살때), 현금(팔때), 송금(보낼때),송금(받을때), 미화환산율)
    for i in range(0,len(table)):
        # 각 레코드 0번째는 통화명
        if(i % 7 == 0):
            currency.append(table[i].string.replace('\n','').replace('\t','').replace(' ',''))
        # 각 레코드 1번째는 매매기준율
        if (i % 7 == 1):
            basic.append(table[i].string.replace(',',''))
        #  각 레코드 2번째는 현금(살때)
        if (i % 7 == 2):
            cash_buy.append(table[i].string.replace(',',''))
        #  각 레코드 3번째는 현금(팔때)
        if (i % 7 == 3):
            cash_sell.append(table[i].string.replace(',',''))
        #  각 레코드 4번째는 송금(보낼때)
        if (i % 7 == 4):
            remittance_send.append(table[i].string.replace(',',''))
        #  각 레코드 5번째는 송금(받을때)
        if (i % 7 == 5):
            remittance_get.append(table[i].string.replace(',', ''))
        #  각 레코드 6번째는 미화환산율
        if (i % 7 == 6):
            conversion.append(table[i].string.replace(',',''))

    df = pd.DataFrame({"currency":currency,"basic rate":basic,"cash(buy)":cash_buy,"cash(sell)":cash_sell,"remittance(send)":remittance_send,"remittance(get)":remittance_get,"conversion with USD":conversion})
    stantard = standard_date[0].string + " " + standard_bank[0].string + " 고시회차" + standard_round[0].string + "회"
    # DataFrame을 html형식으로 변환
    data = {"exchange_rate":df.to_html(),"standard":stantard}

    return render(request, 'exchange_rate/exchange_rate.html', data)