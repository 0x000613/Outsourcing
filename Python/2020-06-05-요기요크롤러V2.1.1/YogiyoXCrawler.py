import os
import bs4
import time
import openpyxl
from selenium import webdriver

# 기본 설정
os.system("title YogiyoXCrawler - Xeorsoftware v2.1.0")

BASE_DIR = os.path.realpath(os.path.dirname("__file__"))

# 엑셀 제어문 초기화
wb = openpyxl.load_workbook(os.path.join(BASE_DIR, 'result.xlsx'))
sheet1 = wb.active

# 크롬 드라이버 로드
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
# 크롬 창 사이즈 설정
driver.set_window_size(1024, 800)
# 크롬 드라이버 최종 로드 대기
driver.implicitly_wait(1)

# 무한스크롤링 함수
def scroller():
    # 무한스크롤 페이지를 모두 파싱하기 위해 스크롤링
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

# 음식점 리스트 파서
def restListCrawler(pageSource):
    restNameList = pageSource.find_all("div", class_="restaurant-name")
    return restNameList

# 음식점 검색 함수
def restFinder(restName):
    global restFind
    # 검색 버튼 클릭
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/a').click()
            break
        except:
            #print("검색 버튼 클릭 에러 발생")
            continue
    # 음식점명 입력
    driver.find_element_by_xpath('//*[@id="category"]/ul/li[15]/form/div/input').send_keys(restName)
    # 검색 버튼 클릭
    driver.find_element_by_xpath('//*[@id="category_search_button"]').click()
    # 검색된 음식점 클릭
    try:
        driver.find_element_by_xpath('//*[@id="content"]/div/div[5]/div/div/div/div').click()
        restFind = True
    except:
        restFind = False
        pass

# 음식점 상세 정보 파서
def restInfoParser():
    try:
        # 전화번호 파싱
        callNumber = str(driver.find_element_by_xpath('//*[@id="info"]/div[2]/p[2]/span').get_attribute('innerHTML')).replace(" (요기요 제공 번호)", '')
    except:
        callNumber = "NULL"
    try:
        # 주소지 파싱
        address = driver.find_element_by_xpath('//*[@id="info"]/div[2]/p[3]/span').get_attribute('innerHTML')
    except:
        address = "NULL"
    # 요기요 홈페이지 버그로 인해, 음식점 리스트 페이지에서만 음식점 검색이 가능하여 뒤로가기 스크립트 삽입으로 해결함
    driver.execute_script("window.history.go(-1)")
    return callNumber, address

# 프로그램 메인 함수
def main():
    # 음식점 검색 에러 발생 Boolean 변수
    restFind = True
    # 모든 음식점 리스트
    # 유저에게 검색할 주소를 입력받음
    address = input("구역검색을 위한 주소를 입력해주세요 : ")

    # 크롤러 요기요 페이지 접속
    driver.get("https://www.yogiyo.co.kr/mobile/#/")

    # 주소입력창 초기화
    driver.find_element_by_class_name("form-control").clear()
    # 주소입력창에 사용자가 설정한 주소 입력
    driver.find_element_by_class_name("form-control").send_keys(address)
    # 주소 검색 버튼 클릭
    driver.find_element_by_xpath('//*[@id="button_search_address"]/button[2]').click()

    # 음식점 리스트가 로드될때까지 프로그램 정지
    time.sleep(2)

    # 무한 스크롤링
    scroller()

    # 음식점 리스트 파싱
    pageSource = bs4.BeautifulSoup(driver.page_source, "html.parser")
    # 파싱된 음식점 리스트를 restNameList 변수에 저장
    restNameList = []
    for rest in restListCrawler(pageSource):
        restNameList.append(rest.text)
    
    # 검색된 음식점의 총 합을 유저 인터페이스에 출력
    if len(restNameList) == 0:
        print("해당 지역에 검색된 음식점이 없거나, 주소를 잘못 입력하셨습니다.")
        print("다시 입력해주세요")
    else:
        print("검색된 음식점 수 : " + str(len(restNameList)) + "곳")

    count = 0
    # 음식점 상세 페이지 접근 및 크롤링
    for restName in restNameList:
        if restFind == False:
            pass
        else:
            # 엑셀데이터 재로드
            wb = openpyxl.load_workbook(os.path.join(BASE_DIR, 'result.xlsx'))
            sheet1 = wb.active
            restFinder(restName)
            # 음식점 정보가 로드될때까지 프로그램 정지
            time.sleep(1)
            restInfo = restInfoParser()
            # [음식점명, 음식점 전화번호, 음식점 주소] 리스트 형태의 데이터를 엑셀 파일 데이터에 추가
            sheet1.append([restName, restInfo[0], restInfo[1]])
            # 엑셀 데이터 저장
            wb.save(os.path.join(BASE_DIR, 'result.xlsx'))
            count += 1
            print("현재 진행상태 : {}/{}   {}%".format(count, len(restNameList), round(count * 100 / len(restNameList), 2)), end='\r')
    print("작업이 완료되었습니다.\n프로그램을 종료하셔도 됩니다.")
    os.system("pause")
main()