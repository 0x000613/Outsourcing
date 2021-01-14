from msvcrt import getch

def main():
    while True:
        print("Q=종료 C=계속진행")
        key = ord(getch())
        if key == 113 or key == 81:
            print("프로그램 종료")
            return
        elif key == 99 or key == 67:
            print("출력할 예제를 누르세요 (1, 2, 3, 4)")
            key = ord(getch())
            if key == 49:
                for i in range(1, 8):
                    if i > 2 and i < 7:
                        print('*' + ' '*(i-2) + '*')
                    else:
                        print('*'*i)
            elif key == 50:
                # count 초기화
                count = 0
                # 5부터 0까지 역순 for문
                for i in range(6, 0, -1):
                    # 왼쪽 공백 삼각형을 그리는 print함수
                    print(' '*i + '*', end='')
                    # 중앙 삼각형의 공백을 채우는 print함수
                    if count != 0: print(' '*(count*2 - 1) + '*')
                    # count가 0이아니면 다음줄로 개행하기 위한 print함수
                    else: print()
                    # count를 1만큼 증가시킴
                    count += 1
                    # 중앙 삼각형의 밑변을 그리기 위한 print 함수
                    if count == 6: print('*'*13)
            elif key == 51:
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
            elif key == 52:
                j = 7
                k = -1
                for i in range(1, 5):
                    if k == -1: print('*' + ' '*k + ' '*j + '*'*i)
                    elif i == 4: print('*' + ' '*(i-1) + '*' + ' '*(i-1) + '*')
                    else: print('*' + ' '*k + '*' + ' '*j + '*' + ' '*k + '*')
                    j -= 2
                    k+=1

                j = 3
                k = 1
                for i in range(1, 3):
                    print('*' + ' '*k + '*' + ' '*(j) + '*' + ' '*k + '*')
                    k -= 1
                    j += 2
                print('*' + ' '*7 + '*')

main()
            