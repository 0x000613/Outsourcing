import os
import csv

BaseDIR = os.path.realpath(os.path.dirname(__file__))

def readData():
    while True:
        filename = input("파일 이름을 입력하세요 : ")
        filename = os.path.join(BaseDIR, filename)
        try:
            f = open(filename, 'r', encoding='utf-8')
            break
        except FileNotFoundError:
            print("존재하지 않는 파일입니다. 파일명을 다시 입력해주세요")
            pass
    return csv.reader(f)
