fruit = {"배":[2000, 3], "사과":[1500, 5], "딸기":[1800, 2], "참외":[2300, 5]}
totalNeedMoney = 0
for i in fruit:
    if fruit[i][1] < 5:
        print("{}는(은) {}개 모자라며 더 구매하는데 {}원이 필요합니다.".format(i, 5 - fruit[i][1], fruit[i][1] * fruit[i][0]))
        totalNeedMoney += fruit[i][0]
print("총 {}원이 필요합니다.".format(totalNeedMoney))