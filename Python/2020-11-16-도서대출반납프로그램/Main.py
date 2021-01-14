import os
import csv
from datetime import datetime

# 시간 메소드 정의
now = datetime.now()

menu = """도서관 대출 시스템입니다.
어떻게 도와드릴까요?
1. 대출
2. 반납
3. 도서기부
4. 종료
"""

# 도서를 도서명으로 찾아서 위치를 반환하는 함수
def findBookByName(bookName, bookList):
    for book in bookList:
        if bookName in book and bookName == book[0]:
            return book

# 도서의 대여, 대여반납일을 수정하는 함수
def changeBookInfo(bookName, bookList, startDate="{}-{}-{}".format(now.year, now.month, now.day), expDate="{}-{}-{}".format(now.year, now.month, int(now.day)+14)):
    for book in bookList:
        if bookName in book and bookName == book[0]:
            replaceBook = book
            replaceBook[3], replaceBook[4] = startDate, expDate
            bookList[bookList.index(book)] = replaceBook
    f = open(CSV_FILE, mode='w', newline='')
    wr = csv.writer(f)
    for line in bookList:
        wr.writerow(line)
    f.close()

# 도서 기부 함수
def giveBook(bookName, bookMaker, bookMakeDate, bookList):
    bookList.append([bookName, bookMaker, bookMakeDate, '', ''])
    f = open(CSV_FILE, mode='w', newline='')
    wr = csv.writer(f)
    for line in bookList:
        wr.writerow(line)
    f.close()

# Main.py 파일이 위치한 디렉토리 경로
BASE_DIR = os.path.realpath(os.path.dirname(__file__))
# CSV 파일이 위치한 경로
CSV_FILE = os.path.join(BASE_DIR, "Data.csv")

# 데이터 읽기
f = open(CSV_FILE, mode='r')
data = csv.reader(f)

# 책 리스트 초기화
bookList = []
for line in data:
    bookList.append(line)
f.close()

while(True):
    # 메뉴 출력
    print(menu)

    # 사용자 메뉴 선택
    select = int(input("> "))

    # 메뉴 1번
    if select == 1:
        print("대출을 도와드리겠습니다. 원하시는 도서의 이름을 입력해주세요")
        bookName = input("> ")
        wishBook = findBookByName(bookName, bookList)
        try:
            if wishBook != None and wishBook[3] == '' and wishBook[4] == '':
                changeBookInfo(bookName, bookList)
                print("대출완료")
            elif wishBook[3] != '' and wishBook[4] != '':
                print("해당 도서는 이미 대출된 상태이므로 대출하실 수 없습니다.")
        except:
            print("검색하신 도서는 저희 도서관에 없습니다.")
    # 메뉴 2번
    elif select == 2:
        print("반납을 도와드리겠습니다. 반납하실 도서의 이름을 입력해주세요")
        bookName = input("> ")
        wishBook = findBookByName(bookName, bookList)
        if wishBook != None and wishBook[3] != '' and wishBook[4] != '':
            changeBookInfo(bookName, bookList, '', '')
            print("반납완료")
        elif wishBook[3] == '' and wishBook[4] == '':
            print("해당 도서는 이미 반납된 상태이므로 반납하실 수 없습니다.")
        else:
            print("검색하신 도서는 저희 도서관에 없습니다.")

    elif select == 3:
        print("기부하실 도서의 이름을 입력해주세요")
        bookName = input("> ")
        print("기부하실 도서의 출판사를 입력해주세요")
        bookMaker = input("> ")
        print("기부하실 도서의 출간일을 입력해주세요")
        bookMakeDate = input("> ")
        giveBook(bookName, bookMaker, bookMakeDate, bookList)
        print("기부가 완료되었습니다. 감사합니다.")

    elif select == 4:
        break