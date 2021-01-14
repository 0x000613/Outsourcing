columnName =    ["요금제명", "기본료", "데이터한도", "음성한도", "데이터초과요율", "음성초과요율"]
skt =           ["T플랜 세이브              ", 33000, 1500, 10000, 22, 1.98]
freet =         ["심플 100분2G             ", 4400, 2000, 100, 22, 1.98]
hellovision =   ["The 착한 데이터 유심 1.3GB", 8500, 1300, 6000, 22.53, 1.98]
eyesmobile =    ["아이즈100                ", 8500, 1500, 300, 22.53, 1.98]
plans = [skt, freet, hellovision, eyesmobile]

for i in range(len(plans)):
    print("{}. {}        {}      {}      {}      {}      {}".format(i+1, plans[i][0], plans[i][1], plans[i][2], plans[i][3], plans[i][4], plans[i][5]))

num = int(input("궁금하신 요금제 번호를 알려주세요 : "))
info = input("어떤 정보가 궁금하신가요? 요금제명, 기본료, 데이터한도, 음성한도, 데이터초과요율, 음성초과요율 중에서 답해주세요 : ")

print("{}번 요금제의 {}은 {}입니다.".format(num, info, plans[num-1][columnName.index(info)]))

useData = int(input("한 달에 데이터를 몇 MB 사용하시나요? "))
useVoice = int(input("한 달에 음성을 몇 분 사용하시나요? "))

for i in range(len(plans)):
    if useData > plans[i][2]:
        dataPrice = ((useData - plans[i][2]) * plans[i][4])
    else:
        dataPrice = 0

    if useVoice > plans[i][3]:
        voicePrice = ((useVoice - plans[i][3]) * (plans[i][5]*60))
    else:
        voicePrice = 0
    
    print("{}번 요금제를 사용하셨을 때의 요금은 {}원입니다.".format(i+1, plans[i][1] + dataPrice + voicePrice))