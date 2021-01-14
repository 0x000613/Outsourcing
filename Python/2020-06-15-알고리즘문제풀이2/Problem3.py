# 음료수
people = int(input())
bottle = int(input())
bottlePerMaxPay = 8000/people
totalPay = 0
for count in range(bottle):
    currentBottleCount = int(input())
    if currentBottleCount * 1600 > bottlePerMaxPay: totalPay += bottlePerMaxPay
    else: totalPay += currentBottleCount * 1600
print("Total = {} won".format(int(totalPay)))