import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
 
BASE_DIR = os.path.realpath(os.path.dirname(__file__))
form_class = uic.loadUiType(os.path.join(BASE_DIR, "main.ui"))[0]

# 입금 총액
totalMoney = 0
refundMoney = 0
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 잔돈 반환 버튼 클릭
        self.refundButton.clicked.connect(self.refundBtnClicked)

        # 동전 버튼 클릭
        self.coin50.clicked.connect(self.insertCoin50)
        self.coin100.clicked.connect(self.insertCoin100)
        self.coin500.clicked.connect(self.insertCoin500)

        # 커피 버튼 클릭
        self.milkCoffeButton.clicked.connect(self.milkCoffeBtnClicked)
        self.sugarCoffeButton.clicked.connect(self.sugarCoffeBtnClicked)
        self.blackCoffeButton.clicked.connect(self.blackCoffeBtnClicked)

        # 커피 꺼내기 버튼 클릭
        self.takeoutButton.clicked.connect(self.takeoutCoffeBtnClicked)

        # 지폐 투입 드롭 다운 콤보박스
        self.paperMoneySelect.activated[str].connect(self.paperMoneySelected)
    
    # 지폐 투입 드롭 다운 콤보박스 기능 함수
    def paperMoneySelected(self, text):
        global refundMoney
        global totalMoney
        try:
            text = text.replace(',', ''); text = text.replace("원", '')
            refundMoney += int(text)
            totalMoney += int(text)
        except:
            print("error")
        self.totalMoney.setText(str(totalMoney))

    # 잔돈반환 버튼 기능 함수
    def refundBtnClicked(self):
        global refundMoney
        self.refundLineEdit.setText(str(refundMoney))

    # 커피 구매 버튼 기능 함수
    def milkCoffeBtnClicked(self):
        global refundMoney
        refundMoney -= 300
    def sugarCoffeBtnClicked(self):
        global refundMoney
        refundMoney -= 300
    def blackCoffeBtnClicked(self):
        global refundMoney
        refundMoney -= 200

    # 동전 버튼 기능 함수
    def insertCoin50(self):
        global totalMoney
        global refundMoney
        refundMoney += 50
        totalMoney += 50
        self.totalMoney.setText(str(totalMoney))
    def insertCoin100(self):
        global totalMoney
        global refundMoney
        refundMoney += 100
        totalMoney += 100
        self.totalMoney.setText(str(totalMoney))
    def insertCoin500(self):
        global totalMoney
        global refundMoney
        refundMoney += 500
        totalMoney += 500
        self.totalMoney.setText(str(totalMoney))

    # 커피 꺼내기 버튼 기능 함수
    def takeoutCoffeBtnClicked(self):
        global totalMoney
        global refundMoney
        totalMoney = 0
        refundMoney = 0
        self.totalMoney.setText(str(totalMoney))
        self.refundLineEdit.setText(str(refundMoney))
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()