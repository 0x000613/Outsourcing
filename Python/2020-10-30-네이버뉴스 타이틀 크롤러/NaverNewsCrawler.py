import os
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

baseDIR = os.path.realpath(os.path.dirname(__file__))
driver = webdriver.Chrome(os.path.join(baseDIR, "chromedriver.exe"))

keyword = "간호"
pagestat = 1

titleList = []

while pagestat <= 91:
    driver.get("https://search.naver.com/search.naver?&where=news&query={}&start={}".format(keyword, pagestat))
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all("a", {"class":"news_tit"})
    for i in titles:
        titleList.append(i.text)
    pagestat = pagestat + 10

f = open("output.csv", 'w', encoding="utf-8")
wr = csv.writer(f)
for i in range(len(titleList)):
    wr.writerow([titleList[i]])
f.close()