# 모듈 Import
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
import calcFunctions
from keypad import numPadList, operatorList, constantList, functionList
from math_set import constant_set, function_set

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        # 간편하고 가독성있게 버튼들을 사용하기위해 딕셔너리형태로 저장함
        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        # 버튼들을 For문을 이용하여 추가
        for label in buttonGroups.keys():
            r = 0
            c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0
                    r += 1

        # 그리드 레이아웃을 이용해 버튼들을 추가
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)
        
        # 윈도우 타이틀 지정
        self.setWindowTitle("My Calculator")

    # 유저가 버튼을 클릭하는 이벤트가 발생될 때 실행되는 함수
    def buttonClicked(self):
        # 디스플레이에 표시된 문자가 "Error!"일 경우 디스플레이를 초기화함
        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        # 입력된 키가 '=' 일 경우 eval함수를 이용해서 계산결과를 출력, 만약 계산할 수 없는 경우 Error!를 출력
        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)
        
        # 입력된 키가 'C' 일 경우 디스플레이에 표시된 문자열을 전부 초기화
        elif key == 'C':
            self.display.clear()
        
        # 입력된 키가 constantList딕셔너리 안의 키값에 있을 경우
        elif key in constantList:
            # constant_set딕셔너리에 key값을 넣어 value를 반환받고 반환받은 value를 디스플레이에 추가함
            self.display.setText(self.display.text() + constant_set[key])
        
        # 입력된 키가 functionList딕셔너리 안의 키값에 있을 경우
        elif key in functionList:
            # 변수 n에 현재 디스플레이에 표시된 문자열을 저장함
            n = self.display.text()
            # function_set딕셔너리에 key값을 넣어 리턴받은 값은 함수명이고, (n)으로써 해당 함수에 n변수를 넣어 함수를 동작하고
            # 값을 반환받음
            value = function_set[key](n)
            # 반환받은 값이 'dec -> roman'일 경우 
            self.display.setText(str(value))
        else:
            self.display.setText(self.display.text() + key)

# 해당 스크립트 실행자가 자신(__main__)일 경우에만 해당 스크립트를 실행함
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())