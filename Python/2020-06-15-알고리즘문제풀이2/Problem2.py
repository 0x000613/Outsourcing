# 수열
n1 = int(input())
n2 = int(input())

a1 = n1
if a1 > 0:
    a2 = a1 * 2 + 1
    print(a2)
elif a1 < 0:
    a2 = a1 ** 2
    print(a2)
else:
    a2 = 10
    print(a2)

for i in range(n1+1, n2):
    if a2 > 0 and a2 * 2 + 1 < n2:
        a2 = a2 * 2 + 1
        print(a2)
    elif a2 < 0 and a2 ** 2 < n2:
        a2 = a2 ** 2
        print(a2)
    elif a2 == 0 and a2 + 10 < n2:
        a2 += 10
        print(a2)