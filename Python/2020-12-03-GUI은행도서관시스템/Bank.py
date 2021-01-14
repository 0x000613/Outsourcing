import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

path = os.path.realpath(os.path.dirname(__file__))

now = datetime.now()

Window_login = tk.Tk()
inputID = tk.StringVar()
inputPassword = tk.StringVar()

class user():
    userid = ''
    userpw = ''
    name = ''
    balance = 0

testUser = user()
testUser.name = "test"
testUser.userid = "test"
testUser.userpw = "test123"
try:
    data = open(os.path.join(path, "입출금내역.txt"), mode='r', encoding="utf-8").readlines()
    moneyIndex = data[-1].index('액')+4
    testUser.balance = int(data[-1][moneyIndex:-2])
except:
    testUser.balance = 0

def dataWriter(data, amount):
    date = "{}-{}-{} {}:{}".format(now.year, now.month, now.month, now.hour, now.minute)
    f = open(os.path.join(path, "입출금내역.txt"), mode="at", encoding="utf-8")
    if data == "입금":
        f.write("입금 {} | {}원 잔액 : {}원\n".format(date, amount, str(testUser.balance)))
    elif data == "출금":
        f.write("출금 {} | {}원 잔액 : {}원\n".format(date, amount, str(testUser.balance)))

def depositMoney(amount):
    global testUser
    testUser.balance += int(amount)
    dataWriter("입금", amount)

def withdrawalMoney(amount):
    global testUser
    if testUser.balance > 0 and (testUser.balance - int(amount)) >= 0:
        testUser.balance -= int(amount)
        dataWriter("출금", amount)
    elif testUser.balance == 0 or (testUser.balance - int(amount)) < 0:
        messagebox.showwarning("잔액부족", "통장에 잔액이 부족합니다.")

def main():
    login()

def menu():
    # 라벨을 생성함
    menuWindow = tk.Tk()
    label = tk.Label(menuWindow, text='메뉴')
    label.grid(row=0, column=0)

    depositButton = tk.Button(menuWindow, text='입금',command=deposit)
    depositButton.grid(row=1, column=0)

    withdrawalButton = tk.Button(menuWindow, text="출금", command=withdrawal)
    withdrawalButton.grid(row=2, column=0)

    showMyMoneyButton = tk.Button(menuWindow, text="잔액조회", command=showMoney)
    showMyMoneyButton.grid(row=3, column=0)

    showTradeListButton = tk.Button(menuWindow, text="거래내역", command=showTradeList)
    showTradeListButton.grid(row=4, column=0)

    exitButton = tk.Button(menuWindow, text="종료", command=Window_login.quit)
    exitButton.grid(row=5, column=0)

def deposit():
    depositWindow = tk.Tk()
    moneyAmount = tk.Label(depositWindow, text='금액')
    moneyAmount.grid(row=0, column=0)
    moneyInput = tk.Entry(depositWindow, textvariable=0)
    moneyInput.grid(row=0,column=1)
    depositOkButton = tk.Button(depositWindow, text='입금',command= lambda: depositMoney(moneyInput.get()))
    depositOkButton.grid(row=1,column=1)

def withdrawal():
    depositWindow = tk.Tk()
    moneyAmount = tk.Label(depositWindow, text='금액')
    moneyAmount.grid(row=0, column=0)
    moneyInput = tk.Entry(depositWindow, textvariable=0)
    moneyInput.grid(row=0,column=1)
    depositOkButton = tk.Button(depositWindow, text='출금',command= lambda: withdrawalMoney(moneyInput.get()))
    depositOkButton.grid(row=1,column=1)

def showMoney():
    showMoneyWindow = tk.Tk()
    showMoneyDisplay = tk.Label(showMoneyWindow, text='잔액 :')
    showMoneyDisplay.grid(row=0, column=0)
    myMoneyDisplay = tk.Label(showMoneyWindow, text=str(testUser.balance))
    myMoneyDisplay.grid(row=0, column=1)

def showTradeList():
    data = open(os.path.join(path, "입출금내역.txt"), mode='r', encoding="utf-8").readlines()
    tradeListWindow = tk.Tk()
    listbox = tk.Listbox(tradeListWindow, selectmode="extended", height=50, width=0)
    for line in range(len(data)):
        listbox.insert(line, str(data[line]).strip())
    listbox.xview_scroll(1, "units")
    listbox.pack()
    listbox.grid(row=0, column=0)

def login():
    # 라벨을 생성함
    label = tk.Label(Window_login, text='로그인')
    ID_label = tk.Label(Window_login, text='ID')
    Password_label = tk.Label(Window_login, text='Password')
    # 입력창을 생성한다
    ID = tk.Entry(Window_login, textvariable=inputID)
    # 아이디 입력창
    Password = tk.Entry(Window_login, textvariable=inputPassword)
    # 패스워드 입력창

    # 버튼을 생성한다
    login_button = tk.Button(Window_login, text='login',command=loginButton)
    # 로그인 버튼

    # 라벨,입력창,버튼을 배치한다
    label.grid(row=0,column=0)
    ID.grid(row=1,column=1)
    Password.grid(row=2,column=1)
    login_button.grid(row=3,column=1)
    ID_label.grid(row=1,column=0)
    Password_label.grid(row=2,column=0)
    # 창에서 위치 지정

    # 창을 띄운다
    Window_login.mainloop()

def loginButton():
    global userid
    userid = inputID.get()
    userpw = inputPassword.get()
    if userid == testUser.userid and userpw == testUser.userpw:
        messagebox.showinfo("로그인 성공", "일반 유저로 로그인하셨습니다.")
        Window_login.destroy()
        menu()
    else:
        messagebox.showwarning("로그인 실패", "아이디 혹은 비밀번호가 다릅니다.")


if __name__ == "__main__":
   main()