import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 콘솔창 클리어 함수
def clear(name=os.name):
    if name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# 프로세스명 설정 함수
def setTitle(name=os.name):
    if name == "nt":
        title = "Hello"
        os.system("title {}".format(title))
    else:
        pass

setTitle()
while True:
    try:
        windowAmount = int(input("몇 개의 창을 띄울것인지 말씀해주세요 : "))
        break
    except:
        print("숫자만 입력해주세요")
        time.sleep(1.5)
        clear()
clear()

# 경로 설정
baseDIR = os.path.realpath(os.path.dirname(__file__)) # 기초 경로 설정
driver = os.path.join(baseDIR, "chromedriver") # 드라이버 경로 설정
extensionsDIR = os.path.join(baseDIR, "extensions") # 확장 프로그램 경로 설정

# 확장 프로그램 설정
options = Options()
extensions = ["fngmhnnpilhplaeedifhccceomclgfbg.crx", "ogeebjpdeabhncjpfhgdibjajcajepgg.crx", "Lauras_Auto_Click_v_1.3.7.crx"]
for extension in extensions:
    options.add_extension(os.path.join(extensionsDIR, extension))

# 드라이버 설정
#driver = webdriver.Chrome(driver, chrome_options=options)

drivers = []

for i in range(1, windowAmount + 1):
    globals()["driver{}".format(i)] = webdriver.Chrome(driver, chrome_options=options)

input("모든 크롬 창별로 사이트 접속후 로그인을 진행하신 후 완료되었으면 엔터를 눌러주세요")
while True:
    print("1.한 번 리프레시    2.정해진 n초 간격으로 리프레시   3.종료")
    while True:
        try:
            sel = int(input('> '))
            break
        except:
            print("숫자만 입력해주세요")
            time.sleep(1.5)
            clear()
    clear()
    if sel == 1:
        for i in range(1, windowAmount + 1):
            globals()["driver{}".format(i)].refresh()
    elif sel == 2:
        while True:
            try:
                sec = int(input("몇 초 간격으로 리프레시 할까요? : "))
                amount = int(input("총 몇 회 진행할까요? : "))
                break
            except:
                print("숫자만 입력해주세요")
                time.sleep(1.5)
                clear()
        for x in range(amount):
            for i in range(1, windowAmount + 1):
                globals()["driver{}".format(i)].refresh()
            time.sleep(sec)
    elif sel == 3:
        break