import random

# 임의의 숫자 6개를 받을 변수 선언
randomNumberList = []

# 1 ~ 46범위의 숫자중 하나를 반환하는 함수 정의
def returnRandomNumber():
    return random.randrange(1, 46)

# 총 6개의 랜덤한 숫자를 뽑아 randomNumberList에 append
for i in range(6):
    randomNumberList.append(returnRandomNumber())

print(randomNumberList)