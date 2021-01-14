import os

# 숫자 확인 함수
def is_digit(string):
    try:
        tmp = float(str)
        return True
    except:
        return False

while True:
    # 사용자에게 파일명을 입력받음
    filename = str(input("파일이름: "))
    # 파일 로드 시도
    try:
        f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), mode="r", encoding="utf-8")
        break
    # 파일이 존재하지 않아, FileNotFoundError 에러가 발생한 경우
    except FileNotFoundError:
        print(filename + "file을 사용할 수 없습니다.")
        continue

# data를 count 하기 위한 변수
groupdatacount = 0
groupsum = 0
groupmax = 0
groupmin = 100

totaldatacount = 0
totalsum = 0
totalmax = 0
totalmin = 100
totalrange = 0
totalaverage = 0
# 매 그룹 시작마다 그룹시작을 출력하기위한 체크 변수
groupfirst = True
groupcount = 1

for line in f.readlines():
    try:
        float(line.strip())
        # group
        groupdatacount += 1
        groupsum += float(line.strip())
        if float(line.strip()) > groupmax: groupmax = float(line.strip())
        if float(line.strip()) < float(groupmin): groupmin = float(line.strip())

        # total
        totaldatacount += 1
        totalsum += float(line.strip())
        if float(line.strip()) > totalmax: totalmax = float(line.strip())
        if float(line.strip()) < float(totalmin): totalmin = float(line.strip())

        totalsum += float(line.strip())
    except:
        try:
            # *을 처음 읽은게 아니면
            if '*' in line.strip() and groupfirst == False:
                print("Group", str(groupcount))
                print("\tdata count =", str(groupdatacount))
                print("\tmax =", str(round(groupmax, 2)))
                print("\tmin =", str(round(groupmin, 2)))
                print("\trange=", str(round(groupmax-groupmin, 2)))
                print("\taverage=", str(round(groupsum/groupdatacount, 2)))
                print("*****")

                groupcount += 1
                groupdatacount = 0
                groupsum = 0
                groupmax = 0
                groupmin = 100

            elif '*' in line.strip() and groupfirst:
                print("*****")
                groupfirst = False
        except:
            pass
print("===========================================")
print("Total {} Groups".format(groupcount))
print("Total data count = {}".format(totaldatacount))
print("Maxval = {}".format(round(totalmax, 2)))
print("Minval = {}".format(round(totalmin, 2)))
print("Range = {}".format(round(totalmax - totalmin, 2)))
print("Average = {}".format(round(totalsum / totaldatacount / 2)))
print("===========================================")