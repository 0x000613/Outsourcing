# 세균
hour = int(input())
temps = []

germs = 1

for temp in range(hour):
    temps.append(int(input()))

for temp in temps:
    if temp < 0:
        germs *= 0.5
    elif temp >= 40:
        pass
    else:
        germs *= 5
print("Number of germs : {}".format(int(germs)))