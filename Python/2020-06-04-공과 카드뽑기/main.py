res = 0

while True:
    ball = input()
    numcard = int(input())
    if ball == 'b':
        res += numcard
        print("Now :",res)
    elif ball == 'y':
        print("Now :",res)
        continue
    elif ball == 'r':
        print("Total :",res)
        break
if res >= 45:
    print("Juchan is WIN")
else:
    print("Minje is WIN")