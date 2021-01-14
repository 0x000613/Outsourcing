import os
from wordcloud import WordCloud
from selenium import webdriver
import matplotlib.pyplot as plt

# 디렉토리 BASE DIR 설정
BASE_DIR = os.path.realpath(os.path.dirname(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
font = os.path.join(BASE_DIR, "AppleSDGothicNeoB.ttf")

# 크롬 창 크기 설정
driver.set_window_size(1024, 800)
# 데이터가 저장될 리스트
datas = []
page = 1
while True:
    # 페이지 이동 대기
    driver.implicitly_wait(1)
    # 페이지 접속
    driver.get("https://www.donga.com/news/search?p={}&query=%EC%A7%91%EA%B0%92&check_news=1&more=1&sorting=1&search_date=2&v1=&v2=&range=1".format(page))
    # 접속한 사이트에서 tit의 클래스를 가지고 있는 요소의 데이터를 titles 리스트에 저장
    titles = driver.find_elements_by_class_name("tit")
    # 크롤링 시작
    for i in titles:
        if i.text != '':
            datas.append(i.text)
    print(len(datas))
    if len(datas) == 900:
        break
    page += 15
print(datas)

unique_string=(" ").join(datas)
wordcloud = WordCloud(font_path = font, width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("crawlData"+".png", bbox_inches='tight')
plt.show()
plt.close()