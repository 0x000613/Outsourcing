import os
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def crawler(username):
    path = os.path.realpath(os.path.dirname(__file__))
    dataFile = open(os.path.join(path, "export", "{}".format(username)), mode="at", encoding="utf-8")

    # Your Twitter account here
    twitterAccount = {"id":"", "pw":""}

    SCROLL_PAUSE_TIME = 2

    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument("headless")

    path = os.path.realpath(os.path.dirname(__file__))
    driver = webdriver.Chrome(os.path.join(path, "chromedriver.exe"), chrome_options=options)

    followersURL = "https://twitter.com/{}/followers".format(username)

    # 트위터 로그인
    driver.get("https://mobile.twitter.com/login?lang=ko")
    username_field = driver.find_element_by_name("session[username_or_email]")
    password_field = driver.find_element_by_name("session[password]")
    username_field.send_keys(twitterAccount["id"])
    driver.implicitly_wait(1)
    password_field.send_keys(twitterAccount["pw"])
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div').click()

    driver.get(followersURL)

    last_height = 0

    userList = []

    while True:
        # 화면 최하단으로 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # 페이지 로드를 기다림
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
        time.sleep(SCROLL_PAUSE_TIME)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
    
        # 새로운 높이가 이전 높이와 변하지 않았을 경우 스크롤 종료
        if new_height == last_height:
            break
        
        # 스크롤 다운이 된다면 스크롤 다운이 된 후의 창 높이를 새로운 높이로 갱신
        last_height = new_height

        crawlData = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div')
        for i in crawlData:
            for x in i.text.split():
                if x[0] == '@':
                    print(x)
                    dataFile.write("{}\n".format(x))
                    userList.append(x)
    return userList

userList = crawler(input("검색하실 유저명을 입력해주세요 : "))