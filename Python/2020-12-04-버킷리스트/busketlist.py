import os

def dataController(mode, contents=None):
    if mode == 'r': return open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "busketlist.txt"), mode=mode, encoding="utf-8").readlines()
    elif mode == 'w':
        f = open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "busketlist.txt"), mode='w', encoding="utf-8")
        f.write('')
        for i in busketList:
            open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "busketlist.txt"), mode="at", encoding="utf-8").write(str(i) + "\n")

tempBusketList = dataController('r')
busketList = []

for i in tempBusketList:
    busketList.append(i.strip())

del tempBusketList

while True:
    print ('*'*50)
    menu=int(input('메뉴선택(1:전체보기, 2:추가, 3:삭제, 4:종료): '))
    print ('*'*50)
    if menu==1:
        for i in range(len(busketList)):
            print("{}) {}".format(i+1, busketList[i]))
    elif menu==2:
        busketList.append(input("버킷리스트에 추가할 항목은?: "))
    elif menu==3:
        for i in range(len(busketList)):
            print('{}) {}'.format(i+1, busketList[i]))
        deleteNum=int(input("버킷리스트에서 삭제할 항목은?: "))
        if deleteNum>len(busketList) or deleteNum <1:
            print("선택오류")
        else:
            busketList.pop(deleteNum-1)
    elif menu==4:
        print("프로그램 종료")
        dataController('w', busketList)
        break
    else:
        print("해당 메뉴가 없습니다.")