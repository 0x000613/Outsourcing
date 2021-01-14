print("3 6 9 게임")

excuteCount = 0
for i in range(1, 51):
    if excuteCount % 5 == 0:
        print()
    countNumber = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if countNumber == 1:
        print(i, '=', '*', end='\t\t')
    elif countNumber > 1:
        print(i, '=', '**', end='\t\t')
    else:
        print(i, '=', i, end='\t\t')
    excuteCount += 1