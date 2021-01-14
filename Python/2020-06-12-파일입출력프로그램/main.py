import os

# 현재 작업디렉토리를 알아내 BASE_DIR에 선언한다.
BASE_DIR = os.path.realpath(os.path.dirname(__file__))
# 알아낸 작업 디렉토리와 input.txt를 합쳐 input.txt파일의 경로를 완성하여 BASE_FILE에 선언한다.
BASE_FILE = os.path.join(BASE_DIR, "input.txt")

# 메뉴를 표시하는 함수
def menu():
    select = int(input("1)Insert (삽입)\n2)Delete (제거)\n3)find (탐색)\n4)Show (열거)\n5)Change (고침)\n6)Exit (정지)\n> "))
    return select

# 데이터를 파일로부터 가져오는 함수
def getData():
    f = open(BASE_FILE, mode="r", encoding="utf-8")
    datas = f.readlines()
    return datas

# 데이터를 정리하는 함수
def sortData(data):
    # datas 리스트 초기화
    datas = []
    for i in data:
        # 가져온 데이터에서 개행문자 \n을 제거하고 ' '(공백) 기분으로 문자열을 나눠서 datas 리스트에 저장
        datas.append(i.replace("\n", '').split(' '))
    return datas

# 데이터 삽입 함수
def insertData():
    return input("데이터 입력(ex)철수 78) > ")

# 데이터 제거 함수
def deleteData(data):
    targetName = input("제거할 사람의 이름 > ")
    isRemoved = False
    for i in range(len(data)):
        # 제거할 사람의 이름을 리스트에서 찾아 삭제
        if data[i][0] == targetName:
            removeTarget = i
            isRemoved = True
    del(data[removeTarget])
    return data, isRemoved

# 데이터 탐색 함수
def findData(data):
    targetName = input("찾을 사람의 이름 > ")
    for i in range(len(data)):
        # 이름을 리스트에서 찾는데 성공했을 경우
        if data[i][0] == targetName:
            # 위치를 반환하고 함수 종료
            return i
    # 찾지 못했을 경우 -1을 반환
    return -1

# 데이터 열거 함수
def showData(data):
    print(data)

# 데이터 수정 함수
def editData(data):
    newData = input("수정할 사람의 이름과, 수정될 점수를 입력해주세요 (ex)철수 55)> ").split()
    for i in range(len(data)):
        # 이름을 리스트에서 찾는데 성공했을 경우
        if data[i][0] == newData[0]:
            # 점수를 수정하고 data를 반환
            data[i][1] = newData[1]
            return data

# 메인 함수
def main():
    # 초기 파일 데이터 로드
    datas = sortData(getData())
    select = 0
    while True:
        if select != 4:
            showData(datas)
        select = menu()
        # 선택이 1번이면
        if select == 1:
            # insertData함수의 반환값을 datas 리스트에 append
            datas.append(insertData().split())
        # 선택이 2번이면
        elif select == 2:
            # deleteData 함수 실행
            data = deleteData(datas)
            datas = data[0]
            if data[1] == False:
                print("존재하지 않는 사람이므로 제거할 수 없습니다.")
        # 선택이 3번이면
        elif select == 3:
            print(findData(datas))
        # 선택이 4번이면
        elif select == 4:
            showData(datas)
        # 선택이 5번이면
        elif select == 5:
            datas = editData(datas)
        # 선택이 6번이면
        elif select == 6:
            break
        
main()