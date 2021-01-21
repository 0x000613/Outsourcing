import os
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# 정렬되지 않은 데이트포맷을 깔끔한 데이트포맷으로 변환하여 반환하는 함수
def sortDate(date):
    date = date.text.strip().replace(". ", '-').replace('.', '')
    date = date.split('-')
    return f"{date[0]}-{date[1].rjust(2, '0')}-{date[2].rjust(2, '0')}"

# 20190101 ~ 20210101

baseDIR = os.path.dirname(os.path.realpath(__file__))
driverPath = os.path.join(baseDIR, "chromedriver.exe")
driver = webdriver.Chrome(executable_path=driverPath)
pklPath = os.path.join(baseDIR, "NaverBlog.pkl")

# query = input("어떤 키워드로 검색하시겠습니까? : ")
# startDate= input("시작 날짜를 입력해주세요 : ")
# endDate = input("종료 날짜를 입력해주세요 : ")

# 수집된 2020년의 결과들이 저장되는 리스트형 변수입니다.
year2020List = []
# 수집된 2019년의 결과들이 저장되는 리스트형 변수입니다.
year2019List = []

for pageNo in range(1, 1000):
    url = f"https://section.blog.naver.com/Search/Post.nhn?pageNo={pageNo}&rangeType=PERIOD&orderBy=sim&startDate=2019-01-01&endDate=2019-12-31&keyword=연금"
    driver.get(url)
    driver.implicitly_wait(5)

    titles = driver.find_elements_by_css_selector("span.title") # 블로그 글 제목 리스트
    dates = driver.find_elements_by_class_name("date")  # 블로그 글 작성일 리스트
    
    for i in range(0, len(dates)):
        if titles[i].text != '':
            row = [sortDate(dates[i]), titles[i].text.strip()]
            year2019List.append(row)
            print(row)

    os.system("clear")
    print(pageNo)
    print("Current year2019List's Length = {}".format(len(year2019List)))
    if len(year2019List) >= 1000:
        break

for pageNo in range(1, 1000):
    url = f"https://section.blog.naver.com/Search/Post.nhn?pageNo={pageNo}&rangeType=PERIOD&orderBy=sim&startDate=2020-01-01&endDate=2020-12-31&keyword=연금"
    driver.get(url)
    driver.implicitly_wait(5)

    titles = driver.find_elements_by_css_selector("span.title") # 블로그 글 제목 리스트
    dates = driver.find_elements_by_class_name("date")  # 블로그 글 작성일 리스트
    
    for i in range(0, len(dates)):
        if titles[i].text != '':
            row = [sortDate(dates[i]), titles[i].text.strip()]
            year2020List.append(row)
            print(row)

    os.system("clear")
    print(pageNo)
    print("Current year2020List's Length = {}".format(len(year2020List)))
    if len(year2020List) >= 1000:
        break

df = pd.DataFrame(year2019List + year2020List)
df.to_pickle(pklPath)