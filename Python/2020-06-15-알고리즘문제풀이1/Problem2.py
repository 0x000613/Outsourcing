num1, num2, num3 = input().split()
num1 = int(num1); num2 = int(num2); num3 = int(num3)
if (num1 + num2 + num3) % 2 == 0: print(max(num1, num2, num3))
else: print(num1 + num2 + num3)