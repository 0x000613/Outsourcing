import os
import sqlite3
import pandas as pd

# 데이터 저장 경로 초기화
BASE_DIR = os.path.realpath(os.path.dirname(__file__))

# 데이터베이스 커서(접속 관련) 설정 초기화
conn = sqlite3.connect(os.path.join(BASE_DIR, "data.db"),
                       isolation_level=None)  # iso~~~ = 자동 커밋
c = conn.cursor()

# 데이터 삽입 함수
def addDataBase():
    # 엑셀 데이터 삽입
    data = pd.read_csv(os.path.join(BASE_DIR, "data.csv"), encoding="cp949")

    # "dataTable"이라는 테이블에 데이터를 삽입하는 코드
    c.execute("CREATE TABLE IF NOT EXISTS dataTable \
        (idx integer PRIMARY KEY, channel text, ordermount integer, canclemount integer, totalmount integer, pgm_start text) ")
    # ([컬럼이름, 데이터타입, 옵션] 순으로 데이터를 삽입함)

    datas = []
    for queryNum in range(len(data["채널"])):
        datas.append((data["채널"][queryNum], int(data["주문수량"][queryNum]), int(data["취소수량"][queryNum]), int(data["주문수량"][queryNum]) - int(data["취소수량"][queryNum]), data["방송시작시간"][queryNum]))

    c.executemany(
        "INSERT INTO dataTable(channel, ordermount, canclemount, totalmount, pgm_start) VALUES(?,?,?,?,?)", datas)

# 데이터 출력 함수
def viewDataBase():
    c.execute("SELECT * FROM dataTable")
    print(c.fetchall())

addDataBase()