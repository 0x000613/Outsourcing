import tkinter
import json
import os
from tkinter import ttk
from tkinter import messagebox

# TK GUI 윈도우 기본 설정
window=tkinter.Tk()
window.title("Manager")
window.geometry("900x400+600+300")
window.resizable(False, False)

# 문장 정렬 함수
def defineString(idx, string, blank=50):
    stringList = string.split(',')
    resString = str(idx).ljust(blank)
    for i in stringList:
        resString += i.ljust(blank)
    return resString

# 상품 가격정보
with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Price.json")), mode='r', encoding="utf-8") as priceJson:
    prodPrice = json.load(priceJson)

# 상품 재고수량
with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Stock.json")), mode='r', encoding="utf-8") as stockJson:
    prodStock = json.load(stockJson)

# 판매할 상품이 담길 딕셔너리
sellList = {}
# 총 판매 금액
sellPrice = 0

def alertMessage(title, content):
    messagebox.showinfo(title, content)

# 새 제품 추가 버튼 클릭시
def addNewProdOk(prodCategory, prodName, prodPrice_, prodAmount):
    global prodPrice
    global prodStock
    prodStock[prodName] = prodAmount
    prodPrice[prodName] = prodPrice_
    # 제품, 재고 저장
    with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Stock.json")), mode='w', encoding="utf-8") as makeFile:
        json.dump(prodStock, makeFile, indent="\t", ensure_ascii=False)
    with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Price.json")), mode='w', encoding="utf-8") as makeFile:
        json.dump(prodPrice, makeFile, indent="\t", ensure_ascii=False)
    f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), "SellLog.txt")), mode="at", encoding="utf-8")
    f.write("{},{},추가\n".format(prodName, prodAmount))
    f.close()
    alertMessage("안내", "({}) 상품이 {}개 추가되었습니다.".format(prodName, prodAmount))

# 기존 상품 리스트 메뉴 확인 버튼 클릭시
def prodListShowOK(option, prodName='', prodAmount=0):
    global prodStock
    global prodPrice
    if option == 1:
        prodStock[prodName] += prodAmount
        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Stock.json")), mode='w', encoding="utf-8") as makeFile:
            json.dump(prodStock, makeFile, indent="\t", ensure_ascii=False)
    elif option == 2:
        del(prodStock[prodName])
        del(prodPrice[prodName])
        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Stock.json")), mode='w', encoding="utf-8") as makeFile:
            json.dump(prodStock, makeFile, indent="\t", ensure_ascii=False)
        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Price.json")), mode='w', encoding="utf-8") as makeFile:
            json.dump(prodPrice, makeFile, indent="\t", ensure_ascii=False)
    

# 상품목록
def prodListShow():
    top = tkinter.Toplevel()
    top.title("상품목록")
    top.geometry("800x800+600+300")

    # 선택박스
    Radiovar = tkinter.IntVar()
    Radio_button1 = tkinter.Radiobutton(top, text="입고",variable=Radiovar,value=1)
    Radio_button2 = tkinter.Radiobutton(top, text="삭제",variable=Radiovar,value=2)
    Radio_button1.place(x=10, y=30)
    Radio_button2.place(x=10, y=60)

    # 상품명, 수량
    nameLabel = tkinter.Label(top, text="상품명")
    nameLabel.place(x=10, y= 110)
    priceLabel = tkinter.Label(top, text="수량")
    priceLabel.place(x=10, y= 140)

    # 상품명, 수량 입력 박스
    prodName = tkinter.StringVar()
    prodAmount = tkinter.IntVar()

    prodNameEntry = ttk.Entry(top, width=15, textvariable=prodName)
    prodAmountEntry = ttk.Entry(top, width=15, textvariable=prodAmount)

    prodNameEntry.place(x=60, y=110)
    prodAmountEntry.place(x=60, y=140)

    confirmBtn = tkinter.Button(top, text="확인", command=lambda:prodListShowOK(Radiovar.get(), prodName.get(), prodAmount.get()))
    confirmBtn.place(x=10, y=200, width=100)

    prodListBox = tkinter.Listbox(top, selectmode='extended', height=0, borderwidth=5)
    # 상품 로그 추가
    idx = 0
    for i in prodStock:
        prodListBox.insert(idx, str(idx).ljust(5) + str(i).ljust(30) + str(prodPrice[i]).ljust(20) + str(prodStock[i]).rjust(10))
        idx +=1
    prodListBox.place(x=200, y=30, width=500, height=550)

    prodRecordListNumLabel=tkinter.Label(top, text="Code")
    prodRecordListNumLabel.place(x=200, y=10)
    prodRecordListProdNameLabel=tkinter.Label(top, text="상품명")
    prodRecordListProdNameLabel.place(x=240, y=10)
    prodRecordListProdAmountLabel=tkinter.Label(top, text="가격")
    prodRecordListProdAmountLabel.place(x=400, y=10)
    prodRecordListProdStatusLabel=tkinter.Label(top, text="재고")
    prodRecordListProdStatusLabel.place(x=480, y=10)

# 상품 기록 메뉴
def prodRecord():
    top = tkinter.Toplevel()
    top.title("상품기록")
    top.geometry("700x600+600+300")
    f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), "SellLog.txt")), mode="r", encoding="utf-8")
    prodRecordList = f.readlines()
    print(prodRecordList)

    prodRecordListBox = tkinter.Listbox(top, selectmode='extended', height=0, borderwidth=5)
    # 상품 로그 추가
    for i in range(len(prodRecordList)):
        prodRecordListBox.insert(i, defineString(i, prodRecordList[i], blank=30))
    prodRecordListBox.place(x=10, y=30, width=680, height=550)

    prodRecordListNumLabel=tkinter.Label(top, text="NUM")
    prodRecordListNumLabel.place(x=10, y=10)
    prodRecordListProdNameLabel=tkinter.Label(top, text="상품명")
    prodRecordListProdNameLabel.place(x=150, y=10)
    prodRecordListProdAmountLabel=tkinter.Label(top, text="개수")
    prodRecordListProdAmountLabel.place(x=290, y=10)
    prodRecordListProdStatusLabel=tkinter.Label(top, text="상태")
    prodRecordListProdStatusLabel.place(x=420, y=10)

# 상품 추가 함수
def addNewProd():
    top = tkinter.Toplevel()
    top.title("상품추가")
    top.geometry("300x200+600+300")

    # 선택박스
    Radiovar = tkinter.IntVar()
    Radio_button1 = tkinter.Radiobutton(top, text="상의",variable=Radiovar,value=1)
    Radio_button2 = tkinter.Radiobutton(top, text="하의",variable=Radiovar,value=2)
    Radio_button3 = tkinter.Radiobutton(top, text="신발",variable=Radiovar,value=3)
    Radio_button4 = tkinter.Radiobutton(top, text="기타",variable=Radiovar,value=4)
    Radio_button1.place(x=10, y=30)
    Radio_button2.place(x=10, y=60)
    Radio_button3.place(x=10, y=90)
    Radio_button4.place(x=10, y=120)

    # 상품명, 가격, 수량
    nameLabel = tkinter.Label(top, text="상품명")
    nameLabel.place(x=100, y= 50)

    priceLabel = tkinter.Label(top, text="가격")
    priceLabel.place(x=100, y= 80)

    amountLabel = tkinter.Label(top, text="수량")
    amountLabel.place(x=100, y= 110)

    # 상품명, 가격, 수량 입력 박스
    prodName = tkinter.StringVar()
    prodPrice = tkinter.IntVar()
    prodAmount = tkinter.IntVar()

    prodNameEntry = ttk.Entry(top, width=15, textvariable=prodName)
    prodPriceEntry = ttk.Entry(top, width=15, textvariable=prodPrice)
    prodAmountEntry = ttk.Entry(top, width=15, textvariable=prodAmount)

    prodNameEntry.place(x=145, y=50)
    prodPriceEntry.place(x=145, y=80)
    prodAmountEntry.place(x=145, y=110)

    confirmBtn = tkinter.Button(top, text="추가", command=lambda:addNewProdOk(Radiovar.get(), prodName.get(), prodPrice.get(), prodAmount.get()))
    confirmBtn.place(x=150, y=150)

# 상의 메뉴 버튼 클릭 이벤트 관리 함수
def topMenuBtnClicked():
    productBtn1.configure(text="흰색 반팔티")
    productBtn2.configure(text="검은색 반팔티")
    productBtn3.configure(text="주황색 반팔티")
    productBtn4.configure(text="흰색 긴팔티")
    productBtn5.configure(text="검은색 긴팔티")
    productBtn6.configure(text="회색 후드티")
    productBtn7.configure(text="")
    productBtn8.configure(text="")

# 하의 메뉴 버튼 클릭 이벤트 관리 함수
def bottomMenuBtnClicked():
    productBtn1.configure(text="진한 청바지")
    productBtn2.configure(text="연한 청바지")
    productBtn3.configure(text="검은색 슬랙스")
    productBtn4.configure(text="츄리닝 바지")
    productBtn5.configure(text="면바지")
    productBtn6.configure(text="5부 반바지")
    productBtn7.configure(text="")
    productBtn8.configure(text="")

# 신발 메뉴 버튼 클릭 이벤트 관리 함수
def sMenuBtnClicked():
    productBtn1.configure(text="검은색 운동화")
    productBtn2.configure(text="흰색 스니커즈")
    productBtn3.configure(text="샌들")
    productBtn4.configure(text="슬리퍼")
    productBtn5.configure(text="")
    productBtn6.configure(text="")
    productBtn7.configure(text="")
    productBtn8.configure(text="")

# 기타 메뉴 버튼 클릭 이벤트 관리 함수
def oMenuBtnClicked():
    productBtn1.configure(text="백팩")
    productBtn2.configure(text="메신저백")
    productBtn3.configure(text="검정색 모자")
    productBtn4.configure(text="비니")
    productBtn5.configure(text="양말")
    productBtn6.configure(text="회색 후드티")
    productBtn7.configure(text="")
    productBtn8.configure(text="")

# 제품 버튼이 클릭되었을때 해당 상품을 sellList에 추가하는 함수
def addProd(prod):
    global sellList
    global sellPrice
    global prodListBox
    global prodAmountListBox
    global prodPriceListBox

    # 상품리스트 박스를 클리어
    try:
        prodListBox.delete(0, tkinter.END)
        prodAmountListBox.delete(0, tkinter.END)
        prodPriceListBox.delete(0, tkinter.END)
    except:
        pass
    # 판매금액 추가
    sellPrice += prodPrice[prod["text"]]
    try: sellingCountBox.delete(0, tkinter.END)
    except: pass
    sellingCountBox.insert(0, sellPrice)
    # 판매목록에 이미 해당 상품이 있을 경우
    if prod["text"] in sellList:
        # 해당 상품의 수량을 1 증가시킴
        sellList[prod["text"]][0] += 1
        sellList[prod["text"]][1] += prodPrice[prod["text"]]
    else:
        # 해당 상품의 수량을 1, 가격을 12000으로 새로 생성함
        sellList[prod["text"]] = [1, prodPrice[prod["text"]]]
    idx=0
    for product in sellList:
        prodListBox.insert(idx, product)
        prodAmountListBox.insert(idx, sellList[product][0])
        prodPriceListBox.insert(idx, sellList[product][1])
        idx += 1

def sellBtnClicked():
    global sellList
    global prodPrice
    global prodStock
    f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), "SellLog.txt")), mode="at", encoding="utf-8")
    for i in sellList:
        prodStock[i] -= sellList[i][0]
        f.write("{},{},판매\n".format(i, sellList[i][0]))
    # 재고 변경사항 저장
    with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "Stock.json")), mode='w', encoding="utf-8") as makeFile:
        json.dump(prodStock, makeFile, indent="\t", ensure_ascii=False)

    returnPrice.set(receivingPrice.get() - sellPrice)
    sellList = {}

# 상의 메뉴 버튼 생성자
topMenuBtn=tkinter.Button(window, text="상의", command=topMenuBtnClicked)
topMenuBtn.place(x=10, y=10, width=100, height=50)

# 하의 메뉴 버튼 생성자
bottomMenuBtn=tkinter.Button(window, text="하의", command=bottomMenuBtnClicked)
bottomMenuBtn.place(x=120, y=10, width=100, height=50)

# 신발 메뉴 버튼 생성자
sMenuBtn=tkinter.Button(window, text="신발", command=sMenuBtnClicked)
sMenuBtn.place(x=230, y=10, width=100, height=50)

# 기타 메뉴 버튼 생성자
oMenuBtn=tkinter.Button(window, text="기타", command=oMenuBtnClicked)
oMenuBtn.place(x=340, y=10, width=100, height=50)

# 제품 버튼
productBtn1=tkinter.Button(window, text="", command=lambda:addProd(productBtn1))
productBtn1.place(x=10, y=70, width=100, height=50)

productBtn2=tkinter.Button(window, text="", command=lambda:addProd(productBtn2))
productBtn2.place(x=120, y=70, width=100, height=50)

productBtn3=tkinter.Button(window, text="", command=lambda:addProd(productBtn3))
productBtn3.place(x=230, y=70, width=100, height=50)

productBtn4=tkinter.Button(window, text="", command=lambda:addProd(productBtn4))
productBtn4.place(x=340, y=70, width=100, height=50)

productBtn5=tkinter.Button(window, text="", command=lambda:addProd(productBtn5))
productBtn5.place(x=10, y=130, width=100, height=50)

productBtn6=tkinter.Button(window, text="", command=lambda:addProd(productBtn6))
productBtn6.place(x=120, y=130, width=100, height=50)

productBtn7=tkinter.Button(window, text="", command=lambda:addProd(productBtn7))
productBtn7.place(x=230, y=130, width=100, height=50)

productBtn8=tkinter.Button(window, text="", command=lambda:addProd(productBtn8))
productBtn8.place(x=340, y=130, width=100, height=50)

# 계산기
class CalcBtn:
    seven = tkinter.Button(window, text="7")
    eight = tkinter.Button(window, text="8")
    nine = tkinter.Button(window, text="9")

    six = tkinter.Button(window, text="6")
    five = tkinter.Button(window, text="5")
    four = tkinter.Button(window, text="4")

    three = tkinter.Button(window, text="3")
    two = tkinter.Button(window, text="2")
    one = tkinter.Button(window, text="1")

    c = tkinter.Button(window, text="C")
    zero = tkinter.Button(window, text="0")
    remove = tkinter.Button(window, text="<-")

    textbox = ttk.Entry(window, width=20, textvariable=str)

CalcBtn.seven.place(x=280, y=190, width=50, height=30)
CalcBtn.eight.place(x=335, y=190, width=50, height=30)
CalcBtn.nine.place(x=390, y=190, width=50, height=30)

CalcBtn.six.place(x=280, y=225, width=50, height=30)
CalcBtn.five.place(x=335, y=225, width=50, height=30)
CalcBtn.four.place(x=390, y=225, width=50, height=30)

CalcBtn.three.place(x=280, y=260, width=50, height=30)
CalcBtn.two.place(x=335, y=260, width=50, height=30)
CalcBtn.one.place(x=390, y=260, width=50, height=30)

CalcBtn.c.place(x=280, y=295, width=50, height=30)
CalcBtn.zero.place(x=335, y=295, width=50, height=30)
CalcBtn.remove.place(x=390, y=295, width=50, height=30)

# 텍스트 박스
CalcBtn.textbox.place(x=280, y=330, width=160, height=30)

# 상품 목록 버튼
prodListBtn=tkinter.Button(window, text="상품목록", command=prodListShow)
prodListBtn.place(x=10, y=190, width=210, height=50)

# 상품 기록 버튼
prodListBtn=tkinter.Button(window, text="상품기록", command=prodRecord)
prodListBtn.place(x=10, y=250, width=210, height=50)

# 상품 추가 버튼
prodListBtn=tkinter.Button(window, text="상품추가", command=addNewProd)
prodListBtn.place(x=10, y=310, width=210, height=50)

# 결제 상품 상품명 리스트
prodListBox = tkinter.Listbox(window, selectmode='extended', height=0, borderwidth=5)
prodListBox.place(x=460, y=30, width=180, height=220)
prodListLabel=tkinter.Label(window, text="상품명")
prodListLabel.place(x=460, y=10)

# 결제 상품 수량 리스트
prodAmountListBox = tkinter.Listbox(window, selectmode='extended', height=0, borderwidth=5)
prodAmountListBox.place(x=630, y=30, width=140, height=220)
prodListLabel=tkinter.Label(window, text="수량")
prodListLabel.place(x=630, y=10)

# 결제 상품 가격
prodPriceListBox = tkinter.Listbox(window, selectmode='extended', height=0, borderwidth=5)
prodPriceListBox.place(x=760, y=30, width=130, height=220)
prodListLabel=tkinter.Label(window, text="가격")
prodListLabel.place(x=760, y=10)

# 금액 표시란
sellingCountLabel = tkinter.Label(window, text="판매금액", width=10, height=1, relief="solid")
receivedCountLabel = tkinter.Label(window, text="받은금액", width=10, height=1, relief="solid")
returnCountLabel = tkinter.Label(window, text="거스름돈", width=10, height=1, relief="solid")
sellingCountLabel.place(x=460, y=260)
receivedCountLabel.place(x=460, y=300)
returnCountLabel.place(x=460, y=340)

# 금액 입력란
sellingPrice = tkinter.IntVar()
receivingPrice = tkinter.IntVar()
returnPrice = tkinter.IntVar()
sellingCountBox = ttk.Entry(window, width=35, textvariable=sellingPrice)
receivedCountBox = ttk.Entry(window, width=35, textvariable=receivingPrice)
returnCountBox = ttk.Entry(window, width=35, textvariable=returnPrice)
sellingCountBox.place(x=540, y=260)
receivedCountBox.place(x=540, y=300)
returnCountBox.place(x=540, y=340)

# 판매 버튼
sellBtn=tkinter.Button(window, text="판매", command= sellBtnClicked)
sellBtn.place(x=800, y=260, width=80, height=100)

window.mainloop()