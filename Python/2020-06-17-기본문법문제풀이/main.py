std = int(input("입력하는 학생수가 총 몇명인가요? : "))
print("학생의 이름과 취미를 차례대로 입력하세요!")
stdAllData = []
stdNameData = []
stdHobbyData = []
count = 1
while count <= std:
    print(count, "번째 학생 =====")
    stdName = input("* 이름 : ")
    stdHobby = input("* 취미 : ")
    stdAllData.append((stdName, stdHobby))
    stdNameData.append(stdName)
    stdHobbyData.append(stdHobby)
    count += 1

print("== 전체 학생 리스트 정보 :", stdNameData)
print("== 전체 취미 세트 정보 :", list(set(stdHobbyData)))