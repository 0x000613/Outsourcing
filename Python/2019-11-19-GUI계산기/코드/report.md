PyQt5 GUI 기반 계산기 프로그램 관리 보고서

# 프로그래밍 과제 - GUI 기반 계산기 프로그램 관리

> Programming Language: Python3
>
> GUI Library: PyQt5

## 코드 설명

### 1. mycalc10.py

```python
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
        }
```
전반적인 UI 구성 작업 숫자가 표시되는 QLineEdit 영역과 숫자버튼 등 여러가지 버튼 추가

### 2. buttonClicked 함수

```python
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
            self.display.setText(str(value))
        else:
            self.display.setText(self.display.text() + key)
```

해당 함수는 유저가 생성된 버튼중 어떤 버튼을 눌렀을때나 해당 함수가 실행된다.
첫번째로 해당 함수가 실행되면 display에 표시된 값을 가져온다. 그리고 만약 display에 표시된 값이 "Error!"일 경우 디스플레이를 초기화하고 다음 작동을 실행한다.
왜냐하면 display에 표시된 값이 "Error!"인데 해당 값을 초기화시키지 않고 다음 작동을 실행할 경우 "Error!"구문 뒤에 유저가 새로이 클릭한 값이 이어서 붙거나 eval()함수를 사용할 때 에러가 발생할 수 있기 때문이다.  
  
입력된 키가 '='일 경우 eval()함수를 이용해서 display에 표시된 값을 모두 계산한다. 만약 이 과정에서 Error가 발생할 경우 try ~ except절의 except구문이 실행되며 해당 except구문에서는
result 변수에 "Error!" 문자열을 저장하고 display에서는 해당 result변수의 값을 출력한다.

입력된 키가 'C'일 경우 display에 표시된 값을 초기화한다.

입력된 키가 constantList 딕셔너리 안의 키값에 있을 경우 constant_set 딕셔너리에 key값을 넣어 value를 반환하고 반환받은 value를 디스플레이에 출력한다.

입력된 키가 functionList 딕셔너리 안의 키값에 있을 경우 변수 n에 현재 디스플레이에 표시된 문자열을 저장하고 function_set딕셔너리에 입력된 키값을 넣어 리턴받은 값은 함수명이고, (n)으로써 해당 함수에 n변수를 넣어 함수를 동작하고 값을 반환받는다. 이러한 과정으로 반환받은 값을 디스플레이에 출력한다.

만약 위 if ~ else절에서 if조건에 해당하는키가 아닐 경우 else절이 실행되며 해당 else절에서는 단순히 입력받은 키를 display에 출력되어있는 기존 값에 이어붙여넣어 재출력한다.



### 3. 프로그램 실행

```python
# 해당 스크립트 실행자가 자신(__main__)일 경우에만 해당 스크립트를 실행함
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
```
만약 해당 스크립트를 실행시킨 실행자가 mycalc10.py(본인파일)일 경우에만 위의 내용을 실행한다.

### 4. calcFunctions.py

```python
import keypad
from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

# 10진수를 2진수로 변환한 값을 리턴하는 함수
def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

# 2진수를 10진수로 변환한 값을 리턴하는 함수
def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

# 10진수를 로마숫자로 변환한 값을 리턴하는 함수
def decToRoman(numStr):
    romans = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
              ]
    try:
        n=int(numStr)
        result=''
        for value,letters in romans:
            while n>=value:
                result+=letters
                n-=value
        return result
    except:
        return 'dec -> roman'

# 로마숫자를 10진수로 변환한 값을 리턴하는 함수
def romanToDec(numStr):
    romans = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
              ]
    try:

        ret=0
        while len(numStr)!=0:
            for x in romans:
                while numStr[0:len(x[1])]==x[1]:
                    numStr=numStr[len(x[1]):]
                    ret+=x[0]
        return ret
    except:
        return 'Error!'
```
mycalc10의 계산기 프로그램에서 특수버튼이 클릭되었을때 해당 calcFunctions.py의 함수들을 이용해서 계산하고 출력한다.
calcFunctions.py에는 다양한 함수가 존재한다.

decToBin 함수의 경우 10진수를 2진수로 변환하는 함수이다. 반대로 binToDec 함수의 경우에는 2진수를 10진수로 변환한다.
decToRoman 함수는 10진수를 로마숫자로 변환하는 함수이다. 반대로 romanToDec 함수의 경우에는 로마숫자를 10진수로 변환하는 함수이다.

### 5. keypad.py

```python
numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '3', '2', '1',
    '0', ',', '='
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = [
    'pi',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)',
]

functionList = [
    'factorail (!)',
    '-> binary',
    'binary -> dec',
    '-> roman'
]
```

keypad.py의 경우 단순한 구조를 가지고있는데 이는 mycalc10 계산기 프로그램에서 ui를 구성할때 각 버튼의 이름들을 저장해둔 파이썬 파일이다.
각 버튼의 이름은 list자료형을 통해 정의되어있는데 mycalc10에서 ui를 생성할때 해당 리스트안의 원자값들을 하나 하나 빼어 ui를 구성한다.

### 6. math_set.py

```python
import calcFunctions


constant_set = {
    'pi':'3.141592',
    '빛의 이동 속도 (m/s)':'3E+8',
    '소리의 이동 속도 (m/s)':'340',
    '태양과의 평균 거리 (km)':'1.5E+8',
    }

function_set = {
    'factorial (!)':calcFunctions.factorial,
    '-> binary':calcFunctions.decToBin,
    'binary -> dec':calcFunctions.binToDec,
    '-> roman':calcFunctions.decToRoman,
}
```

math_set에서는 mycalc에서 버튼을 클릭하였을때 어떤 함수를 실행해야하는지, 혹은 어떤 값을 반환하기 위하여 존재한다.

딕셔너리 자료형으로 구성되어있으며, constant_set의 경우 값이 절대 변하지않는 상수들을 정의해두었다. 예를들어 pi의 경우 3.14라는 변하지 않는 값을 가지고있는데 사용자가 pi버튼을 클릭하면 해당 버튼이 키가 되어 저장되어있는 value인 3.141592가 반환되도록 하는 구조이다.

function_set에서는 버튼을 클릭할경우 해당 버튼에 따라 실행시킬 함수명을 반환해주기위해 존재한다.
