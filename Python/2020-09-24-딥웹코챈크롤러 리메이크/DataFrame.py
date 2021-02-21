import os
import matplotlib
import matplotlib.pyplot as plt

a = [('로리', 42), ('N번방', 25), ('박사방', 22), ('대마', 19), ('강간', 19), ('마약', 18), ('텔그', 16), ('보안', 15), ('VPN', 14), ('사람', 14), ('검색', 14), ('사진', 13), ('텔레', 13), ('자료', 13), ('사이트', 13), ('형님', 13), ('그냥', 12), ('씨발', 12), ('존나', 12), ('약쟁이', 12)]

def createGraph(wordFrequency):
    # matplot 폰트 설정
    matplotlib.rcParams['axes.unicode_minus'] = False
    matplotlib.rcParams['font.family'] = "AppleGothic"

    word = []
    count = []
    for i in range(len(wordFrequency)):
        word.append(wordFrequency[i][0])
        count.append(int(wordFrequency[i][1]))

    plt.figure()
    plt.bar(word, count)
    plt.show()

createGraph(a)