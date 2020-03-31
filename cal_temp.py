# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:04:39 2020

@author: steve
"""
import os
import csv

select_area=['466920','466900','466880','C0AD50','C0AD30','466940','C0C480','467490','467480','467410','467440','467590']
            #依序為台北 淡水 板橋 鶯歌 蘆洲 基隆 桃園 台中 嘉義 台南 高雄 恆春
select_day=['2018-01','2018-02','2018-03','2018-04','2018-05','2018-06','2018-07','2018-08','2018-09','2018-10','2018-11','2018-12',
            '2019-01','2019-02','2019-03','2019-04','2019-05','2019-06','2019-07','2019-08','2019-09','2019-10','2019-11','2019-12',
            '2020-01','2020-02']
with open('output.csv', 'w+', newline='') as csvFile:
    fieldNames = ['城市','日期', '24度', '26度','28度']
    writer = csv.DictWriter(csvFile, fieldNames)
    writer.writeheader()
    for i in select_area:
        writer.writerow({'城市':i,'日期': '','24度':'', '26度': '', '28度':''})
        for j in select_day:
            path='test_weather/'+i
            if not os.path.isdir(path):
                print('false')
            else:
                f=open('test_weather/'+i+'/test_weather_'+i+'_'+j+'.txt','r')
                all_td=f.readlines()
                false_num=0
                k='</select></td>\n'
                first_day=all_td.index(k)+15 #the first temp in the data
                total_day_in_month=0
                pass_temp_1=24.0 #the lowest temp
                pass_temp_2=26.0
                pass_temp_3=28.0
                ans_1=0
                ans_2=0
                ans_3=0
                while(first_day<len(all_td)):
                    num =''.join([x for x in all_td[first_day] if x.isdigit()])
                    if not num:
                        false_num+=1
                    else:
                        tmp=list(num)
                        tmp.insert(len(tmp)-1,'.')
                        num=''.join(tmp)
                        num=float(num)
                        if num > pass_temp_1:
                            ans_1=ans_1+1
                        if num > pass_temp_2:
                            ans_2=ans_2+1
                        if num > pass_temp_3:
                            ans_3=ans_3+1
                        total_day_in_month+=1
                    first_day+=35
                    
                writer.writerow({'日期': j,'24度':ans_1, '26度': ans_2, '28度':ans_3})
                print('false:',false_num)
                print('total_day:',total_day_in_month)
                print('There is ',ans_1,' days over ',pass_temp_1,' degrees Celsius.')