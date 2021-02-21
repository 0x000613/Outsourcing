import csv
import os

# csv파일을 읽을 경로를 미리 지정하기 위해 BASE_DIR변수 선언 및 초기화
BASE_DIR = os.path.realpath(os.path.dirname(__file__))

# csv파일을 읽는 일련의 과정
f = open(os.path.join(BASE_DIR, "data3.csv"), 'r', encoding="cp949")
rdr = csv.reader(f)
datas = []
count = 0
for line in rdr:
    if count == 2:
        break
    else:
        datas.append(line)
        count += 1
f.close()

# 데이터 분류별(컬럼명, 데이터, 데이터 타입)로 다른 변수에 할당 선언
dataColumns = datas[0]
datas = datas[1]
dataTypes = []

# 1번째 csv파일의 row를 읽어서 데이터 형을 분류
for text in datas:
    if '.' in text: dataTypes.append("float")
    else:
        try:
            int(text)
            dataTypes.append("integer")
        except:
            dataTypes.append("text")
totalQuery = ""

# 쿼리 형태로 만들어주기 위한 문자열 작업
for n in range(len(dataColumns)):
    totalQuery += dataColumns[n] + ' ' + dataTypes[n] + ','
totalQuery = totalQuery[:-1]

# 자기 자신이 직접 실행시켰을 경우에만 출력 (다른파일에서 호출하면 출력 X)
if __name__ == '__main__':
    print(totalQuery)