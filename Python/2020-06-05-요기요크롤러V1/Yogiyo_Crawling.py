import os
import bs4
import time
import pandas as pd
import atexit
from selenium import webdriver

os.system("title YogiyoXCrawler - Xeorsoftware v1.0.0")

try:
    # 출력 HTML 파일을 위한 데이터셋 초기화
    restNameList = []
    restAddressList = []
    restCallnumberList = []

    address = input("구역검색을 위한 주소를 입력해주세요 : ")

    BASE_DIR = os.path.realpath(os.path.dirname("__file__"))

    driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
    driver.set_window_size(1024, 800)
    driver.implicitly_wait(1)

    driver.get("https://www.yogiyo.co.kr/mobile/#/")

    driver.find_element_by_class_name("form-control").clear()
    driver.find_element_by_class_name("form-control").send_keys(address)

    try:
        driver.find_element_by_xpath('//*[@id="button_search_address"]/button[2]').click()
    except:
        pass
    time.sleep(2)

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    # 무한 스크롤링을 통해 모든 음식점 리스트를 로드
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
        
    # 모든 음식점의 리스트를 저장
    restaurantList = []
    newRestaurantList = []
    restaurantSource = driver.page_source
    soup = bs4.BeautifulSoup(restaurantSource, "html.parser")


    for restName in soup.findAll("div", class_="col-sm-6 contract"):
        restaurantList.append(restName)

    for restName in restaurantList:
        newRestaurantList.append(restName.find("div", class_="restaurant-name").text)

    restaurantList = newRestaurantList
    del(newRestaurantList)

    count = len(restaurantList)
    currentCount = 0
    print("{}개의 음식점을 찾았습니다.".format(count))

    # 개별 음식점 정보 파싱
    for restName in restaurantList:
        # 좌측상단 검색 아이콘 클릭
        try:
            driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/a').click()
            # 검색란에 restName 입력
            driver.find_element_by_xpath('//*[@id="category"]/ul/li[15]/form/div/input').send_keys(restName)
            # 검색 버튼 클릭
            driver.find_element_by_xpath('//*[@id="category_search_button"]').click()
            # 검색결과 1번째 항목 클릭
            driver.find_element_by_xpath('//*[@id="content"]/div/div[5]/div/div/div/div').click()
        except:
            pass

        time.sleep(1)
        try:
        # 정보 파싱
            restAddress = driver.find_element_by_xpath('//*[@id="info"]/div[2]/p[3]/span')
            restCallNumber = driver.find_element_by_xpath('//*[@id="info"]/div[2]/p[2]/span')
            restAddress = restAddress.get_attribute('innerHTML')
            restCallNumber = str(restCallNumber.get_attribute('innerHTML')).replace(" (요기요 제공 번호)", '')
        except:
            pass

        if restAddress == None or restAddress == '':
            restAddress = "NULL"
        if restCallNumber == None or restCallNumber == '':
            restCallNumber = "NULL"
        
        try:
            print("**********************************")
            print(restName)
            print(restAddress)
            print(restCallNumber)
            print("현재 진행상태 : {}/{}   {}%".format(currentCount, count, round(currentCount * 100 / count, 2)))

            restNameList.append(restName)
            restAddressList.append(restAddress)
            restCallnumberList.append(restCallNumber)
            currentCount += 1
        except:
            pass
        driver.execute_script("window.history.go(-1)")
        
    print("프로그램 종료 루틴 수행중")
    print("데이터 저장중..")
    # 출력 HTML을 위한 pandas 데이터 프레임 생성
    dataFrame = pd.DataFrame(
        {
            'name':restNameList,
            'address':restAddressList,
            'callnumber':restCallnumberList
        }
    )
    dataFrame.to_excel("{}.xlsx".format(address))
    print("데이터 저장이 완료되었습니다.")

except KeyboardInterrupt:
    print("프로그램 종료 루틴 수행중")
    print("데이터 저장중..")
    # 출력 HTML을 위한 pandas 데이터 프레임 생성
    dataFrame = pd.DataFrame(
        {
            'name':restNameList,
            'address':restAddressList,
            'callnumber':restCallnumberList
        }
    )
    dataFrame.to_excel("{}.xlsx".format(address))
    print("데이터 저장이 완료되었습니다.")