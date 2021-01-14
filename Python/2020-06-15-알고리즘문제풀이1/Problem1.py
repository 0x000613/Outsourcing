num1, num2, num3 = input().split()
num1 = int(num1); num2 = int(num2); num3 = int(num3)

if num1 >= num2 == False:
    Min = num1
    if num1 >= num3 == False:
        Min = num1
    else:
        Min = num3
else:
    Min = num2
    if num2 >= num3 == False:
        Min = num3
    else:
        Min = num1

