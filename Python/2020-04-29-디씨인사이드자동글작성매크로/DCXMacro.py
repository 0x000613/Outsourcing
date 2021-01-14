import sys
import random
import time
import pyautogui
from selenium import webdriver
import os
import ImgClicker
import threading
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton)

def writer(username, password, title, contents, delay, headless):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        BASE_DIR = os.path.dirname(__file__)
        GALL = "leagueoflegends3"
        URL = 'https://gall.dcinside.com/board/write/?id={}'.format(GALL)
        options = webdriver.ChromeOptions()

        #headless 모드(크롬 창 히든) off
        if headless:
            options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        #user-agent 변경
        options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")

        #크롬 드라이버 로드
        driver = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver.exe'), chrome_options=options)

        driver.implicitly_wait(3)
        #글작성 페이지 로드
        driver.get(URL)
        time.sleep(1)

        #글작성 구간
        driver.find_element_by_id('name').send_keys(username) # 작성자 닉네임
        driver.find_element_by_id('password').send_keys(password) # 작성자 패스워드
        driver.find_element_by_id('subject').send_keys(random.choice(title) + str(random.randrange(10000, 99999))) # 글 제목
        time.sleep(1)
        driver.find_element_by_xpath("/html/body").click()
        time.sleep(1)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@name='tx_canvas_wysiwyg']"))
        time.sleep(1)
        # 글 내용
        driver.find_element_by_tag_name("body").send_keys(contents + str(random.randrange(10000, 99999)))
        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/main/section/article[2]/form/div[4]/button[2]').click() # 작성 버튼 클릭
        print("매크로 1회 작업완료")
        ImgClicker.click() # IP 변경 button 클릭
        time.sleep(delay)
        driver.quit()
    print("매크로 작업 완료")
 
class MyApp(QWidget):
 
    def __init__(self):
 
        super().__init__()
        self.initUI()
 
    def initUI(self):
 
        # 그리드 레이아웃을 생성
        grid = QGridLayout()
        # 창의 레이아웃을 그리드로 설정
        self.setLayout(grid)

        # 유동 아이디 닉네임, 비밀번호 설정
        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        grid.addWidget(QLabel('아이디'), 0, 0)
        grid.addWidget(self.username, 1, 0)
        grid.addWidget(QLabel('비밀번호'), 2, 0)
        grid.addWidget(self.password, 3, 0)
 
        # 글 제목
        self.title_1 = QLineEdit(self)
        self.title_2 = QLineEdit(self)
        self.title_3 = QLineEdit(self)
        grid.addWidget(QLabel('제목 1'), 4, 0)
        grid.addWidget(self.title_1, 5, 0)
        grid.addWidget(QLabel('제목 2'), 6, 0)
        grid.addWidget(self.title_2, 7, 0)
        grid.addWidget(QLabel('제목 3'), 8, 0)
        grid.addWidget(self.title_3, 9, 0)

        # 딜레이
        self.delay = QLineEdit(self)
        grid.addWidget(QLabel('딜레이(초)'), 10, 0)
        grid.addWidget(self.delay, 11, 0)

        # 내용
        self.contents = QTextEdit(self)
        grid.addWidget(QLabel('내용'), 12, 0)
        grid.addWidget(self.contents, 13, 0)

        # 시작 버튼
        self.on_btn = QPushButton('시작', self)
        grid.addWidget(self.on_btn, 14, 0)
        self.on_btn.clicked.connect(self.on_btn_clicked)
        # 정지 버튼
        self.off_btn = QPushButton('정지', self)
        grid.addWidget(self.off_btn, 15, 0)
        self.off_btn.clicked.connect(self.off_btn_clicked)

        self.setWindowTitle('DCXMacro')
        self.setGeometry(300, 300, 450, 700)
        self.show()
    
    def on_btn_clicked(self):
        global t
        username = self.username.text()
        password = self.password.text()
        title = [self.title_1.text(), self.title_2.text(), self.title_3.text()]
        contents = self.contents.toPlainText()
        delay = int(self.delay.text())
        headless=False
        t = threading.Thread(target=writer, args=(username, password, title, contents, delay, headless))
        t.start()

    def off_btn_clicked(self):
        global t
        t.do_run = False
        t.join()
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())