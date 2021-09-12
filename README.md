# crawl_for_weather_TW_demo
用於抓取http://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp 觀測資料查詢系統的簡易程式碼<br>
Use to crawl Taiwan's area weather from http://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp 

## 需求(Dependencies)
* BeatifulSoup 4.0up

## 環境(Environment)
* Windows 10<br>
* Anaconda 3<br>
* Python 3.6

## 前言(Foreword)
此專案應友人需求而生，初窺爬蟲，還請不吝指教<br>
I am the beginner in Git and crawl.This repository was created by request from my firend.
If there are any problems, feel free to give your comments.Thanks for your suggestions.

## 使用(Guide):
直接執行internet_crawl_test.py，其預設值為抓取466920代碼(台北)在2018-01到2020-02期間內的所有td欄位資料，你可以在程式碼中的select_area更改想要抓取的地區代碼以及select_day更改想要抓取的時間區段，相關代碼可以上http://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp 查詢，所有結果將預設輸出在test_weather下，並依照城市代碼輸出成資料夾。<br><br>
Run the file internet_crawl_test.py. default set is crawl 466920(Taipei)'s all data from 2018-01 to 2020-02 which labeled by <td> field. You can reset this sets on select_area and select_day in the code and find the city number from http://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp . All results might be outputed on folder "test_weather" with their city number.
