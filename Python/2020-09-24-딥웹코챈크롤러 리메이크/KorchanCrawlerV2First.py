import os

import numpy

import datetime

import requests

import matplotlib

import matplotlib.pyplot as plt

from konlpy.tag import Okt

from bs4 import BeautifulSoup



def createGraph(wordFrequency):

    matplotlib.rcParams['axes.unicode_minus'] = False

    matplotlib.rcParams['font.family'] = "NanumGothicCoding"



    lineX = []

    lineY = []

    for i in wordFrequency:

        lineX.append(i[0])

        lineY.append(i[1])

    x = numpy.arange(20)



    plt.bar(x, lineY)

    plt.xticks(x, lineX)

    plt.show()



def dataMiner(pageArea):

    okt = Okt()

    wordData = []

    while True:

            for pnum in range(pageArea[0], pageArea[1]):

                os.system("python2 {}".format(os.path.join(os.path.dirname(__file__), "onoffcheck_crawler_v2.0.py http://jqu6my2mlqp4zuui.onion/index?page={}".format(pnum))))

                filename = os.path.join(os.path.dirname(__file__), "jqu6my2mlqp4zuui.onion_index?page={}_logs.txt".format(pnum))

                data = open(filename, mode='r', encoding="utf-8")

                html = BeautifulSoup(data, 'html.parser')

                writedpost = html.findAll("div", {"class":"round-border-bottom"})

            writedpost = html.findAll("div", {"class":"round-border-bottom"})

            for post in writedpost:

                for word in okt.morphs(post.text):

                    if len(word.strip()) > 1 and word and "http" not in word and "2020-10" not in word:

                        try: int(word)

                        except: wordData.append(str(word).strip())

            return wordData

def main():

    print("KorchanCrawler Start at {}".format(datetime.datetime.now()))

    pageArea = (0, 5)

    count = {}

    wordData = dataMiner(pageArea)

    for word in wordData:

        try: count[word] += 1

        except: count[word] = 1

    wordFrequency = sorted(count.items(), key=lambda x: x[1], reverse=True)[1:21]

    createGraph(wordFrequency)

main()