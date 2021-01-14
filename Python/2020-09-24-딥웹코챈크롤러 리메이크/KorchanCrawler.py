import os
import time
import numpy
import requests
import matplotlib
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from bs4 import BeautifulSoup

excludedWord = open(os.path.join(os.path.dirname(__file__), "excludedWord.txt"), mode='r', encoding="utf-8").read().split()

def createGraph(wordFrequency):
    try:
        plt.close("all")
    except:
        pass
    matplotlib.rcParams['axes.unicode_minus'] = False
    matplotlib.rcParams['font.family'] = "NanumGothicCoding"
    lineX = []
    lineY = []
    for i in wordFrequency:
        lineX.append(i[0])
        lineY.append(i[1])
    x = numpy.arange(20)
    plt.rcParams["figure.figsize"] = (17,6)
    plt.bar(x, lineY)
    plt.xticks(x, lineX)
    plt.show(block=False)

def dataMiner(pageArea):
    okt = Okt()
    wordData = []
    while True:
            for pnum in range(pageArea[0], pageArea[1]):
                os.system("python2 {}".format(os.path.join(os.path.dirname(__file__), "onoffcheck_crawler_v2.0.py http://jqu6my2mlqp4zuui.onion/index?page={}".format(pnum))))
                print("Page Crawling End")
                filename = os.path.join(os.path.dirname(__file__), "jqu6my2mlqp4zuui.onion_index?page={}_logs.txt".format(pnum))
                print("Read File End")
                data = open(filename, mode='r', encoding="utf-8").read()
                print("Load Data End")
                html = BeautifulSoup(data, 'html.parser')
                print("HTML Soup End")
                writedpost = html.findAll("div", {"class":"round-border-bottom"}) # 이부분에서 오래걸림
                print("Data parsing End")
                for post in writedpost:
                    for word in okt.morphs(post.text):
                        print(word)
                        if len(word.strip()) > 1 and word and "http" not in word and word not in excludedWord:
                            try: int(word)
                            except: wordData.append(str(word).strip())
            return wordData
def main():
    pageArea = (0, 2)
    count = {}
    wordData = dataMiner(pageArea)
    for word in wordData:
        try: count[word] += 1
        except: count[word] = 1
    wordFrequency = sorted(count.items(), key=lambda x: x[1], reverse=True)[1:21]
    createGraph(wordFrequency)

while True:
    main()