import random

for i in range(5):
    date = input("날짜를 입력해주세요 : ")
    brightness = random.randint(0, 100)
    print(brightness)

    month = int(date[:2])
    time = int(date[4:6])

    # 동절기 조건
    if (month > 10 or month < 4) and (brightness <= 45 or time >= 17):
        print("가로등 ON")

    # 하절기 조건
    elif (month > 3 or month < 11) and (brightness <= 45 or time >= 18):
        print("가로등 ON")

    else:
        print("가로등 OFF")