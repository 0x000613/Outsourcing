import random

# 리스트 정렬을 위한 선택정렬 알고리즘 함수 생성
def select(tlist):
    for i in range(len(tlist)-1): # 리스트의 크기-1만큼 반복
        for j in range(i+1, len(tlist)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
            if tlist[i] > tlist[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
                tlist[i] , tlist[j]  = tlist[j], tlist[i] # swap 해주기
        print(tlist)
    return tlist

# rand1 변수에 5~9사이의 정수형 난수 1개를 발생시켜 대입
rand1 = random.randint(5, 9)
# rand2 초기화
rand2 = []
# rand1의 값만큼 1~99사이의 정수형 난수를 발생시켜 rand2 리스트에 추가
for i in range(rand1):
    rand2.append(random.randint(1, 99))

# 정렬함수를 이용해 rand2 정렬
rand2 = select(rand2)