# count 초기화
count = 0
# 5부터 0까지 역순 for문
for i in range(6, 0, -1):
    # 왼쪽 삼각형을 그리는 print함수
    if count == 0: print('*'*13, end='')
    else: print('*'*i + '*', end='')
    # 중앙 삼각형의 공백을 채우는 print함수
    if count != 0: print(' '*(count*2 - 1) + '*', end='');print('*'*(i-1) + '*')
    # count가 0이아니면 다음줄로 개행하기 위한 print함수
    else: print()
    # count를 1만큼 증가시킴
    count += 1
    # 중앙 삼각형의 밑변을 그리기 위한 print 함수
    if count == 6: print('*'*13)