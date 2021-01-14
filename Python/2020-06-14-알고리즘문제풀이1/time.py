n1 = int(input())
n2 = int(input())
m = 60
for t in range(n1):
    if t + 1 == n1: m += n2
    for m in range(1, m):
        if m % 10 == 0 and m != 60:
            print("{} : {}".format(t, m))
        elif m == 60:
            print("{} : {}".format(t+1, "00"))