import os
import re
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup

# 워드 클라우드 함수
def wordcloud():
    fontpath = os.path.join(os.path.dirname(__file__), "SRC", "NanumGothic.ttf")
    wordcloud = WordCloud(
        font_path = fontpath,
        width = 800,
        height = 800
    )
    text = open(os.path.join(os.path.dirname(__file__), "SRC", "data.txt")).read()
    wordcloud = wordcloud.generate(text)
    fig = plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    fig.savefig('wordcloud_without_axisoff.png')

# 파싱 데이터 재정렬 함수
def remove_tag(content):
    content = str(content)
    cleanr =re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    cleantext = cleantext.strip()
    return cleantext

# 프로그램 메인 함수
def main():
    while True:
        for pnum in range(1, 11):
            os.system("python2 {}".format(os.path.join(os.path.dirname(__file__), "onoffcheck_crawler_v2.0.py http://jqu6my2mlqp4zuui.onion/index?page={}".format(pnum))))
            filename = os.path.join(os.path.dirname(__file__), "jqu6my2mlqp4zuui.onion_index?page={}_logs.txt".format(pnum))
            data = open(filename, mode='r', encoding="utf-8")
            soup = BeautifulSoup(data, 'html.parser')
            # 게시글 리스트 파싱
            soup = soup.select("#boardarea tr .content")
            write_list = []
            for i in soup:
                write_list.append(remove_tag(i.text).replace("\n        ", '').replace("\n", ''))
            for i in write_list:
                open(os.path.join(os.path.dirname(__file__), "SRC", "data.txt"), mode="at", encoding="utf-8").write(i + '\n')
                
        wordcloud()
        print("crawl restart in 1 hour")
        time.sleep(3600)

main()
