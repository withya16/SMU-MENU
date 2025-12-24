import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import csv

# 네이버 지도 URL 리스트
url_list = [
    "https://map.naver.com/p/search/%EC%88%99%EB%AA%85%EC%97%AC%EC%9E%90%EB%8C%80%ED%95%99%EA%B5%90/place/31357362?c=17.93,0,0,0,dh",#육쌈냉면
    "https://map.naver.com/p/search/%EC%88%99%EB%AA%85%EC%97%AC%EC%9E%90%EB%8C%80%ED%95%99%EA%B5%90/place/1225528407?c=17.93,0,0,0,dh",#장재근초밥
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1710721871?c=17.39,0,0,0,dh&placePath=%3Fentry%3Dbmp", # 면식당
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/33141786?c=17.84,0,0,0,dh&placePath=%3Fentry%3Dbmp",#포라임
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/20393083?c=17.84,0,0,0,dh&placePath=%3Fentry%3Dbmp" ,# 베스트프렌드
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/11822204?c=17.84,0,0,0,dh", #달볶이
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/39402518?c=18.13,0,0,0,dh&placePath=%3Fentry%3Dbmp",#포36거리
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/38520832?c=19.00,0,0,0,dh&placePath=%3Fentry%3Dbmp",#사이공마켓,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/35357170?c=19.30,0,0,0,dh&placePath=%3Fentry%3Dbmp",#빨봉분식,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/37604156?c=19.30,0,0,0,dh&placePath=%3Fentry%3Dbmp",#아리랑,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1822077577?c=19.30,0,0,0,dh",#버스컵떡볶이,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1867723156?c=19.30,0,0,0,dh",#앙꼬,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1634250257?c=19.30,0,0,0,dh",#루다브레드,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1499881357?c=19.30,0,0,0,dh",#컴포즈커피,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1938714550?c=20.00,0,0,0,dh",#벤티프레소,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1964695450?c=20.00,0,0,0,dh",#샐러디,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1053376088?c=19.11,0,0,0,dh&placePath=%3Fentry%3Dbmp",#네코노스시,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1121296624?c=19.11,0,0,0,dh&placePath=%3Fentry%3Dbmp",#마포구이마당,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/11600155?c=19.11,0,0,0,dh&placePath=%3Fentry%3Dbmp",#정,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/38226766?c=19.11,0,0,0,dh&placePath=%3Fentry%3Dbmp",#지지고,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/38227453?c=19.11,0,0,0,dh&placePath=%3Fentry%3Dbmp",#이ㅏㄱ토스트,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/229295571?c=19.11,0,0,0,dh&placePath=%3Fentry%3Dbmp",#리또리또,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1643832594?c=19.26,0,0,0,dh&placePath=%3Fentry%3Dbmp",#위드달걀빵
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1947229051?c=19.26,0,0,0,dh&placePath=%3Fentry%3Dbmp",#미스터카츠,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/13377125?c=19.41,0,0,0,dh",#하마,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1580738812?c=19.41,0,0,0,dh&placePath=%3Fentry%3Dbmp",#쥬케로카페,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1732861163?c=19.26,0,0,0,dh&placePath=%3Fentry%3Dbmp",#몬스터플레이스,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1139206641?c=19.26,0,0,0,dh&placePath=%2F%3Faction%3Dbookmark",#킷테,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/37392079?c=19.26,0,0,0,dh&placePath=%3Fentry%3Dbmp",#숙대소반,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1863671075?c=19.26,0,0,0,dh&placePath=%3Fentry%3Dbmp",#카페퓨엔테,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/38548042?c=19.26,0,0,0,dh&placePath=%3Fentry%3Dbmp",#카페나리나무,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/31413184?c=19.26,0,0,0,dh&placePath=%3Fentry%3Dbmp",#부당ㅁ동치킨,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/12950424?c=19.26,0,0,0,dh",#스타벅스숙대점,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1886718487?c=19.55,0,0,0,dh",#뜸들이다,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1130263015?c=19.55,0,0,0,dh",#스택빈,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/13586350?c=19.70,0,0,0,dh&placePath=%3Fentry%3Dbmp",#더함,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1519808598?c=19.70,0,0,0,dh",#홍짜장,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1260486430?c=19.70,0,0,0,dh",#무모한초밥,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/385441394?c=19.70,0,0,0,dh&placePath=%3Fentry%3Dbmp",#마시앤바시,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1462827389?c=19.70,0,0,0,dh&placePath=%3Fentry%3Dbmp",#긴자료코,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/457840624?c=19.70,0,0,0,dh&placePath=%3Fentry%3Dbmp",#홍곱창,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/38628031?c=19.70,0,0,0,dh&placePath=%3Fentry%3Dbmp",#이자와,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/729583733?c=19.70,0,0,0,dh&placePath=%3Fentry%3Dbmp",#타코비,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/11620882?c=19.70,0,0,0,dh&placePath=%3Fentry%3Dbmp",#와플하우스,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1824409156?c=19.39,0,0,0,dh&placePath=%3Fentry%3Dbmp",#비일,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/20510788?c=18.96,0,0,0,dh&placePath=%3Fentry%3Dbmp",#베나레스,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1864792294?c=18.96,0,0,0,dh&placePath=%3Fentry%3Dbmp",#사브로21,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/20521260?c=18.96,0,0,0,dh&placePath=%3Fentry%3Dbmp",#나폴리키친,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/32873972?c=18.96,0,0,0,dh&placePath=%3Fentry%3Dbmp",#어바웃샤브,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/608474270?c=18.96,0,0,0,dh&placePath=%3Fentry%3Dbmp",#백채김치찌개,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1090690229?c=18.96,0,0,0,dh&placePath=%3Fentry%3Dbmp",#본죽,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1593059414?c=17.61,0,0,0,dh&placePath=%3Fentry%3Dbmp",#만나칼국수,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1805379721?c=17.61,0,0,0,dh&placePath=%3Fentry%3Dbmp",#교촌치킨,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1156600106?c=17.61,0,0,0,dh&placePath=%3Fentry%3Dbmp",#먼데이피크닉,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1027383007?c=17.61,0,0,0,dh&placePath=%3Fentry%3Dbmp",#까치네분식,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1403783898?c=17.92,0,0,0,dh&placePath=%3Fentry%3Dbmp",#메이드바이그레이스,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/36314854?c=17.92,0,0,0,dh&placePath=%3Fentry%3Dbmp",#버거인,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1116654116?c=18.22,0,0,0,dh",#츄르츄르라멘,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1420182118?c=18.22,0,0,0,dh",#레이브피자,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1408688235?c=18.50,0,0,0,dh",#김밥2000,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1874545324?c=18.50,0,0,0,dh",#꽃보다크레페,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/18718329?c=18.65,0,0,0,dh",#굴다리소곱창,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/18718055?c=19.39,0,0,0,dh",#두리식당,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/34556586?c=19.39,0,0,0,dh&placePath=%3Fentry%3Dbmp",#한입소반,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1107759562?c=19.39,0,0,0,dh",#산촌쭈꾸미,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/11711391?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp",#쌍대포소금구이,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/1090397990?c=18.28,0,0,0,dh",#상록수,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/37704343?c=18.28,0,0,0,dh",#스시사이꼬,
    "https://map.naver.com/p/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/place/32614080?c=18.51,0,0,0,dh"#써브웨이,
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1264343790?c=15.81,0,0,0,dh&placePath=%3Fentry%253Dbmp", #키보 에다마메
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/18138022?c=15.81,0,0,0,dh&placePath=%3Fentry%253Dbmp", #별진화로구이
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1134380329?c=15.81,0,0,0,dh&placePath=%3Fentry%253Dbmp", #남영동양문
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1993434921?c=16.56,0,0,0,dh&placePath=%3Fentry%3Dbmp", #원동미나리삼겹살
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1202589603?c=16.56,0,0,0,dh&placePath=%3Fentry%3Dbmp", #다이빙룸
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1960419585?c=16.56,0,0,0,dh", #KFC 숙대입구점
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1437567446?c=17.05,0,0,0,dh", #이웃집영준이
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/21692522?c=17.05,0,0,0,dh", #하노이별 숙대입구점
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1584543298?c=17.05,0,0,0,dh", #철길우동까스
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/18128511?c=17.05,0,0,0,dh", #대관령목장
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1452312747?c=17.05,0,0,0,dh", #모토카레시
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/37371125?c=17.05,0,0,0,dh", #라이언스커피로스터스
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/36432841?c=17.05,0,0,0,dh&placePath=%3Fentry%3Dbmp", #구복만두
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1361722409?c=17.51,0,0,0,dh&placePath=%3Fentry%3Dbmp", #한강로칼국수
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1903881715?c=17.51,0,0,0,dh", #더블랙웨일바
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1259626694?c=17.51,0,0,0,dh", #미드스트오브플로우
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1726513067?c=17.51,0,0,0,dh", #가든한밤
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1685877606?c=17.51,0,0,0,dh", #솔티드 스모크
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/20912548?c=17.51,0,0,0,dh", #Jesus Coffee
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1123580172?c=17.51,0,0,0,dh&placePath=%3Fentry%3Dbmp", #남산드럼통 본점
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/667716278?c=17.51,0,0,0,dh&placePath=%3Fentry%3Dbmp", #때가이르매
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1706611874?c=17.51,0,0,0,dh&placePath=%3Fentry%3Dbmp", #경성빵공장 카스테라점
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/20897435?c=17.83,0,0,0,dh", #둘이파전
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1006912352?c=17.83,0,0,0,dh", #짚신매운갈비찜
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1809018107?c=17.83,0,0,0,dh&placePath=%3Fentry%3Dbmp", #멘타미
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1389258535?c=17.94,0,0,0,dh&placePath=%3Fentry%3Dbmp", #탄막
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1879213294?c=17.94,0,0,0,dh&placePath=%3Fentry%3Dbmp", #청기와타운 남영점
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/21427490?c=17.94,0,0,0,dh&placePath=%3Fentry%3Dbmp", #오복함흥냉면
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1477472215?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp", #카페시바
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1980101692?c=18.28,0,0,0,dh", #하이퐁가든
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1414413246?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp", #평화남영
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1318653699?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp", #품계
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1485127270?c=18.28,0,0,0,dh", #온센 용산구점
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1937470835?c=18.28,0,0,0,dh", #틸데
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/33127324?c=18.28,0,0,0,dh", #구구
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1465236583?c=18.28,0,0,0,dh", #MUJABEE
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/20149514?c=18.28,0,0,0,dh", #옛날감자전
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/18715234?c=18.28,0,0,0,dh", #윤지식당
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1740824640?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp", #살팀보카
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1006208343?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp", #남영탉
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/20867185?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp", #소소라면 닭꼬치
    "https://map.naver.com/p/search/%EC%88%99%EB%8C%80%EC%9E%85%EA%B5%AC%EC%97%AD%20%EB%A7%9B%EC%A7%91/place/1183463721?c=18.28,0,0,0,dh&placePath=%3Fentry%3Dbmp", #없음 베이커리
    
]

# 크롬 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 크롤링 데이터 저장 리스트
csv_data = []
rev = []  # 키워드 리뷰 데이터를 저장할 리스트

# Create timestamp for filename
now = datetime.datetime.now()
file_name = 'naver_review_' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.csv'

# URL 리스트 순회
for idx, url in enumerate(url_list, start=0):  # index 0부터 시작
    driver.get(url)
    time.sleep(3)  # 페이지 로딩 대기

    try:
        detail_frame = driver.find_element(By.CSS_SELECTOR, '#entryIframe')  
        driver.switch_to.frame(detail_frame)
        time.sleep(3)

        # 가게 이름 가져오기
        name = driver.find_element(By.CSS_SELECTOR, "#_title > div > span.GHAhO").text
        type = driver.find_element(By.CSS_SELECTOR, "#_title > div > span.lnJFt").text
        print(f"Processing {name}")
        
        try:
            # class명이 'veBoZ'인 모든 요소 가져오기
            tabs = driver.find_elements(By.CLASS_NAME, "veBoZ")
            
            # 각 탭의 텍스트가 '리뷰'를 포함하는지 확인하고, 해당 탭 클릭
            for tab in tabs:
                if '리뷰' in tab.text:
                    tab.click()  # 탭 클릭
                    print("리뷰 탭 클릭 완료!")
                    break
            else:
                print("'리뷰' 탭을 찾을 수 없습니다.")

        except Exception as e:
            print(f"리뷰 탭 클릭 중 오류 발생: {e}")

        # 태그 리뷰와 그에 맞는 수 찾기
        tags_reviews = []

        # '더보기' 버튼을 반복적으로 클릭하여 모든 태그 리뷰를 로드
        while True:
            try:
                ul_element = driver.find_element(By.CSS_SELECTOR, ".mrSZf > ul")
                li_elements = ul_element.find_elements(By.TAG_NAME, "li")

                # 각 리뷰 항목 순회
                for li in li_elements:
                    try:
                        tag_text = li.find_element(By.CLASS_NAME, "t3JSf").text
                    except:
                        tag_text = "No tag text"

                    try:
                        tag_count = li.find_element(By.CLASS_NAME, "CUoLy").text
                        tag_count = tag_count.replace('이 키워드를 선택한 인원\n', '').strip()
                        tags_reviews.append({tag_text: int(tag_count)})
                    except:
                        tags_reviews.append({tag_text: 0})

                # '더보기' 버튼 클릭
                more_button = driver.find_element(By.CLASS_NAME, "dP0sq")
                more_button.click()
                time.sleep(2)

            except:
                print("No more '더보기' button found.")
                break  # 더 이상 '더보기' 버튼이 없을 경우 루프 종료
        
        # Scroll down the page to load reviews using JavaScript
        for _ in range(15):
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(1)

        # Click '더보기' button to load more reviews
        try:
            for _ in range(2):
                load_more_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id=\"app-root\"]/div/div/div/div[6]/div[3]/div[3]/div[2]/div/a')))
                if load_more_button:
                    driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
                    driver.execute_script("arguments[0].click();", load_more_button)
                    time.sleep(3.5)
                else:
                    print("No more reviews to load.")
                    break
        except Exception as e:
            print(f"Error in loading more reviews: {e}")
            if 'target frame detached' in str(e):
                print("Frame detached, attempting to switch to iframe again.")
                driver.switch_to.default_content()
                driver.switch_to.frame('entryIframe')

        # Scroll to the first review item after loading more reviews
        first_review_element = driver.find_element(By.XPATH, '//*[@id=\"app-root\"]/div/div/div/div[6]/div[3]/div[3]/div[1]/ul/li[1]')
        driver.execute_script("arguments[0].scrollIntoView(true);", first_review_element)
        time.sleep(1)

        # Expand all review keywords by clicking the '+' button if it exists
        try:
            while True:
                expand_button = driver.find_element(By.CSS_SELECTOR, 'a.pui__jhpEyP.pui__ggzZJ8')
                if expand_button:
                    driver.execute_script("arguments[0].click();", expand_button)
                    time.sleep(2)
                else:
                    break
        except Exception as e:
            print(f"No more expand buttons found or error clicking it: {e}")

        # Get the page source and start scraping reviews
        html = driver.page_source
        bs = BeautifulSoup(html, 'lxml')

        # 리뷰 클래스 select
        reviews = bs.select('li.pui__X35jYm.place_apply_pui.EjjAW')

        # 각 리뷰 기준 처리
        for r in reviews[:20]:  # 최대 리뷰 수 20
            try:
                nickname = r.select_one('span.pui__uslU0d span.pui__NMi-Dp').get_text() if r.select_one('span.pui__uslU0d span.pui__NMi-Dp') else 'N/A'
                visit_keywords = [kw.get_text() for kw in r.select('span.pui__V8F9nN')] + ['N/A'] * 4
                review_keywords = [tag.get_text(strip=True) for tag in r.select('div.pui__HLNvmI span.pui__jhpEyP')] + ['N/A'] * 5

                # 방문키워드 최대 4개, 리뷰키워드 최대 5개. 그 이상은 오류라 간주하고 리스트 자름
                visit_keywords = visit_keywords[:4]
                review_keywords = review_keywords[:5]

                rev.append([
                    name,
                    visit_keywords[0], visit_keywords[1], visit_keywords[2], visit_keywords[3],
                    review_keywords[0], review_keywords[1], review_keywords[2], review_keywords[3], review_keywords[4]
                ])

            except Exception as e:
                print(f"Error extracting review: {e}")
        print(len(rev))

        # 태그 리뷰 정보 출력 및 저장
        print(f"Tags and Counts for {name}: {tags_reviews}")
        csv_data.append([idx, name, type, tags_reviews])  # 태그리뷰를 list로 추가

        # 세부 페이지 크롤링 끝나면 다시 기본 페이지로 돌아감
        driver.switch_to.default_content()

    except Exception as e:
        print(f"Error processing URL: {e}")
        driver.switch_to.default_content()
        continue

# 크롬 드라이버 종료
driver.quit()

# 키워드 리뷰 CSV 파일 저장
with open(file_name, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['store_name', 'visit_keyword_1', 'visit_keyword_2', 'visit_keyword_3', 'visit_keyword_4',
                     'review_keyword_1', 'review_keyword_2', 'review_keyword_3', 'review_keyword_4', 'review_keyword_5'])
    writer.writerows(rev)

print(f"Keyword reviews data saved to {file_name}")


# DataFrame 생성 및 CSV 파일로 저장
rating_df = pd.DataFrame(csv_data, columns=['index', '가게명', '음식종류', '태그리뷰'])
rating_df.to_csv('숙명여대_맛집_크롤링1.csv', encoding='utf-8-sig', index=False)

print("CSV 파일 저장 완료!")
