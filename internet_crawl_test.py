# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:47:34 2020

@author: steve
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import os

select_area=['466920']

#select_area=['466920','466900','466880','C0AD50','C0AD30','466940','C0C480','467490','467480','467410','467440','467590']
            #依序為台北 淡水 板橋 鶯歌 蘆洲 基隆 桃園 台中 嘉義 台南 高雄 恆春
"""
select_area=['467530','C0M410','C0M520','C0M530','C0M640','C0M650','C0M660','C0M670','C0M680','C0M690','C0M700','C0M710','C0M720','C0M740','C0M750','C0M760','C0M770','C0M780','C0M790','C0M800',
             'C0M810','C0M820','C0M830','C0M850'] #chiayi country
            #,'C1M390','C1M400','C1M480','C1M600','C1M610','C1M620','C1M640'] #chiayi country
"""
select_day=['2018-01','2018-02','2018-03','2018-04','2018-05','2018-06','2018-07','2018-08','2018-09','2018-10','2018-11','2018-12',
            '2019-01','2019-02','2019-03','2019-04','2019-05','2019-06','2019-07','2019-08','2019-09','2019-10','2019-11','2019-12',
            '2020-01','2020-02']

for i in select_area:
    for j in select_day:
        time.sleep(1)
        html = urlopen("http://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station="+i+"&stname=%25E6%25B0%2591%25E9%259B%2584&datepicker="+j).read().decode('utf-8')
        print('html:',html)
    
        soup = BeautifulSoup(html, features='lxml')
        print('\nh1:',soup.h1)
        print('\ntd:', soup.td)
        
        all_td = soup.find_all('td')
        path='test_weather/'+i
        if not os.path.isdir(path):
            os.mkdir(path)
        f=open('test_weather/'+i+'/test_weather_'+i+'_'+j+'.txt','w')
        for l in all_td:
            f.write(str(l).encode("utf8").decode("cp950","ignore"))
            f.write("\n")
        f.close()