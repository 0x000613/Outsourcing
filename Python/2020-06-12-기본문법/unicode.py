# 대문자를 쉽게 가져올수 있는 string 모듈을 import한다.
from string import ascii_uppercase
# 대문자 리스트를 가져온다.
alphaList = list(ascii_uppercase)

# 개행을 관리하는 변수 nextLineCounter 초기화
nextLineCounter = 0
for alpha in alphaList:
    # nextLineCounter를 4로 나눈 나머지 값이 0이면
    if nextLineCounter % 4 == 0:
        # 개행
        print()
    # 알파벳 : 알파벳 아스키코드값 탭 + 탭, 개행은 없음 출력한다.
    print(alpha + " : " + str(ord(alpha)) + "\t\t", end='')
    # nextLineCounter을 1만큼 증가시킨다.
    nextLineCounter += 1