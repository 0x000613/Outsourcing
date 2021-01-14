import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

bookFilePath = os.path.join(os.path.realpath(os.path.dirname(__file__)), "도서목록.txt")

now = datetime.now()

Window_login = tk.Tk()
inputID = tk.StringVar()
inputPassword = tk.StringVar()

class user():
    usermode = 'default'
    userid = ''
    userpw = ''
    name = ''
    balance = 0

testUser = user()
testUser.name = "test"
testUser.userid = "test"
testUser.userpw = "test123"

adminUser = user()
adminUser.name = "admin"
adminUser.userid = "admin"
adminUser.userpw = "admin123"

try:
    bookList = open(bookFilePath, mode='r', encoding="utf-8").readlines()
except:
    bookList = []

def addBook():
    addBookWindow = tk.Tk()
    addBookWindow.title("도서 추가")
    bookNameLabel = tk.Label(addBookWindow, text="도서명")
    bookNameLabel.grid(row=0, column=0)
    bookPriceLabel = tk.Label(addBookWindow, text="도서가격")
    bookPriceLabel.grid(row=1, column=0)

    bookName = tk.Entry(addBookWindow, textvariable=str)
    bookName.grid(row=0, column=1)
    bookPrice = tk.Entry(addBookWindow, textvariable=str)
    bookPrice.grid(row=1, column=1)

    confirmButton = tk.Button(addBookWindow, text="추가", command=lambda: addNewBook(bookName.get(), bookPrice.get()))
    confirmButton.grid(row=2, column=0)

def delBook():
    delBookWindow = tk.Tk()
    delBookWindow.title("도서 삭제")

    bookNameLabel = tk.Label(delBookWindow, text="도서명")
    bookNameLabel.grid(row=0, column=0)

    bookName = tk.Entry(delBookWindow, textvariable=str)
    bookName.grid(row=0, column=1)

    confirmButton = tk.Button(delBookWindow, text="삭제", command=lambda: delBookBtn(bookName.get()))
    confirmButton.grid(row=2, column=0)

def rePriceBook():
    rePriceBookWindow = tk.Tk()
    rePriceBookWindow.title("도서가격 변경")

    bookNameLabel = tk.Label(rePriceBookWindow, text="도서명")
    bookNameLabel.grid(row=0, column=0)

    bookName = tk.Entry(rePriceBookWindow, textvariable=str)
    bookName.grid(row=0, column=1)

    bookPriceLabel = tk.Label(rePriceBookWindow, text="가격")
    bookPriceLabel.grid(row=1, column=0)

    bookPrice = tk.Entry(rePriceBookWindow, textvariable=str)
    bookPrice.grid(row=1, column=1)

    confirmButton = tk.Button(rePriceBookWindow, text="수정", command=lambda: rePriceBtn(bookName.get(), bookPrice.get()))
    confirmButton.grid(row=2, column=0)

def addNewBook(bookName, bookPrice):
    open(bookFilePath, mode="at", encoding="utf-8").write("{},{}\n".format(bookName, bookPrice))

def delBookBtn(bookName):
    try:
        bookList = open(bookFilePath, mode='r', encoding="utf-8").readlines()
    except:
        bookList = []
    find = False
    for book in bookList:
        if str(book).split(',')[0] == bookName:
            del bookList[bookList.index(book)]
            f = open(bookFilePath, mode="w", encoding="utf-8")
            f.writelines(bookList)
            find = True
    if find == False:
        messagebox.showwarning("검색 실패", "해당 도서와 일치하는 도서를 찾을 수 없습니다.")

def rePriceBtn(bookName, rePrice):
    try:
        bookList = open(bookFilePath, mode='r', encoding="utf-8").readlines()
    except:
        bookList = []
    find = False
    for book in bookList:
        if str(book).split(',')[0] == bookName:
            f = open(bookFilePath, mode="w", encoding="utf-8")
            bookList[bookList.index(book)] = "{},{}\n".format(bookName, str(rePrice))
            f.writelines(bookList)
            find = True
    if find == False:
        messagebox.showwarning("검색 실패", "해당 도서와 일치하는 도서를 찾을 수 없습니다.")

def main():
    login()

def adminMenu():
    menuWindow = tk.Tk()
    label = tk.Label(menuWindow, text='메뉴')
    label.grid(row=0, column=0)

    addBookButton = tk.Button(menuWindow, text='도서명/가격 추가',command=addBook)
    addBookButton.grid(row=1, column=0)

    delBookButton = tk.Button(menuWindow, text="도서명/가격 삭제", command=delBook)
    delBookButton.grid(row=2, column=0)

    rePriceButton = tk.Button(menuWindow, text="가격 수정", command=rePriceBook)
    rePriceButton.grid(row=3, column=0)


def findBookBtn(bookName):
    find = False
    try:
        bookList = open(bookFilePath, mode='r', encoding="utf-8").readlines()
    except:
        bookList = []
    for book in bookList:
        if str(book).split(',')[0] == bookName:
            find = True
            messagebox.showinfo("검색 성공", "검색하신 도서와 일치하는 도서를 찾았습니다.\n도서명 : {}\n가격 : {}".format(bookName, str(book).split(',')[1]))
    if find == False:
        messagebox.showwarning("검색 실패", "검색하신 도서의 재고가 없습니다.")


def findBook():
    findBookWindow = tk.Tk()
    findBookWindow.title("도서 검색")

    bookNameLabel = tk.Label(findBookWindow, text="도서명")
    bookNameLabel.grid(row=0, column=0)

    bookName = tk.Entry(findBookWindow, textvariable=str)
    bookName.grid(row=0, column=1)

    confirmButton = tk.Button(findBookWindow, text="검색", command=lambda: findBookBtn(bookName.get()))
    confirmButton.grid(row=2, column=0)

def wantBookBtn():
    messagebox.showinfo("도서 신청", "도서 신청이 정상적으로 완료되었습니다.")

def wantBook():
    findBookWindow = tk.Tk()
    findBookWindow.title("도서 신청")

    bookNameLabel = tk.Label(findBookWindow, text="도서명")
    bookNameLabel.grid(row=0, column=0)

    bookName = tk.Entry(findBookWindow, textvariable=str)
    bookName.grid(row=0, column=1)

    confirmButton = tk.Button(findBookWindow, text="신청", command=wantBookBtn)
    confirmButton.grid(row=2, column=0)

def buyBookBtn(bookName):
    find = False
    try:
        bookList = open(bookFilePath, mode='r', encoding="utf-8").readlines()
    except:
        bookList = []
    for book in bookList:
        if str(book).split(',')[0] == bookName:
            find = True
            order = messagebox.askquestion("검색 성공", "검색하신 도서와 일치하는 도서를 찾았습니다.\n도서명 : {}\n가격 : {}\n 구매하시겠습니까?".format(bookName, str(book).split(',')[1]))
            if order == "yes":
                messagebox.showinfo("주문 완료", "주문이 완료되었습니다. 이용해주셔서 감사합니다.")
            else:
                messagebox.showinfo("주문 취소", "주문이 취소되었습니다. 이용해주셔서 감사합니다.")
    if find == False:
        messagebox.showwarning("검색 실패", "검색하신 도서의 재고가 없습니다.")
    

def buyBook():
    buyBookWindow = tk.Tk()
    buyBookWindow.title("도서 주문")

    bookNameLabel = tk.Label(buyBookWindow, text="도서명")
    bookNameLabel.grid(row=0, column=0)

    bookName = tk.Entry(buyBookWindow, textvariable=str)
    bookName.grid(row=0, column=1)

    confirmButton = tk.Button(buyBookWindow, text="주문", command=lambda: buyBookBtn(bookName.get()))
    confirmButton.grid(row=2, column=0)

def menu():
    # 라벨을 생성함
    menuWindow = tk.Tk()
    label = tk.Label(menuWindow, text='메뉴')
    label.grid(row=0, column=0)

    findBookButton = tk.Button(menuWindow, text='도서 찾기',command=findBook)
    findBookButton.grid(row=1, column=0)

    wantBookButton = tk.Button(menuWindow, text="도서 신청", command=wantBook)
    wantBookButton.grid(row=2, column=0)

    buyBookButton = tk.Button(menuWindow, text="도서 주문", command=buyBook)
    buyBookButton.grid(row=3, column=0)

    exitButton = tk.Button(menuWindow, text="종료", command=Window_login.quit)
    exitButton.grid(row=4, column=0)

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
    elif userid == adminUser.userid and userpw == adminUser.userpw:
        messagebox.showinfo("로그인 성공", "관리자로 로그인하셨습니다.")
        Window_login.destroy()
        adminMenu()
    else:
        messagebox.showwarning("로그인 실패", "아이디 혹은 비밀번호가 다릅니다.")


if __name__ == "__main__":
   main()