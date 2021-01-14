# GUI 관련 모듈 Import
from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

global order
guest_num = 0
sold_out = 7        
count = 10

Menu_list = {"짜장면": ["짜장면", "단무지", "양파", "춘장"],
             "라면": ["라면", "라면", "김치"],
             "피자": ["피자", "피클"],
             "치킨": ["치킨", "치킨무"],
             "삼겹살": ["삼겹살", "상추", "김치", "고추장"],
             "갈비탕": ["갈비탕", "깍두기", "김치"],
             "백반": ["밥", "국", "김치", "콩나물", "고등어구이"]}

left_list = {"짜장면": count, "라면": count, "피자": count, "치킨": count,
             "삼겹살": count, "갈비탕": count, "백반": count}

sold_count = {"짜장면": 0, "라면": 0, "피자": 0, "치킨": 0,
              "삼겹살": 0, "갈비탕": 0, "백반": 0}

Order_list = ["짜장면", "피자", "치킨", "라면", "짜장면", "백반", "치킨", "갈비탕", "삼겹살", "치킨",
              "라면", "치킨", "백반", "백반", "치킨", "백반", "짜장면", "갈비탕", "삼겹살", "삼겹살",
              "짜장면", "피자", "치킨", "라면", "짜장면", "백반", "치킨", "갈비탕", "삼겹살", "치킨",
              "라면", "치킨", "백반", "백반", "치킨", "백반", "짜장면", "갈비탕", "삼겹살", "삼겹살",
              "짜장면", "피자", "치킨", "라면", "짜장면", "백반", "치킨", "갈비탕", "삼겹살", "치킨",
              "라면", "치킨", "백반", "백반", "치킨", "백반", "짜장면", "갈비탕", "삼겹살", "삼겹살"
              ] #메뉴 주문 검증 


def food_service_robot(menu, guest):
    global sold_out

    for s in left_list:
        if left_list[s] == 0:
            sold_out -= 1
    if sold_out == 0:
        return -1
    else:
        for m in Menu_list:
            if menu == m:
                if left_list[m] == 0:
                    print(m, "은(는) 모두 팔렸습니다. 다른 메뉴를 선택하여 주십시오.\n")
                    return 0
                for g in range(len(Menu_list[m])):
                    if g == 0:
                        print(Menu_list[m][g], "을(를) 주메뉴 칸에 담습니다.")
                    else:
                        print(Menu_list[m][g], "을(를) 반찬", g, "칸에 담습니다.")
                print(guest + 1, "번 고객님", menu, "이(가) 준비되었습니다.")
                left_list[m] -= 1
                sold_count[m] += 1
                print("남은", menu, "은(는)", left_list[m], "인분입니다.\n")
                return 1
        print("주문하신 메뉴는 존재하지 않습니다. 다시 주문하여 주십시오.\n")
        return 0

if __name__ == "__main__":
        while True:
            keys = Menu_list.keys()
            print("오늘의 메뉴: ", end='')
            print(list(keys))
            try:
                root.quit()
            except:
                pass
            order = input("\n어떤 음식을 주문하시겠습니까? ")
            result = food_service_robot(order, guest_num)
            if result == 1:
                guest_num += 1
                # gui 출력
                class Example(Frame):
                    def __init__(self):
                        super().__init__()   
                            
                        self.initUI()

                        
                    def initUI(self):

                        foodlist = []
                        
                        
                        self.master.title("식판")
                        self.pack(fill=BOTH, expand=1)
                        
                        Style().configure("TFrame", background="#333")
                        
                        if order == "갈비탕":
                            img = Image.open("갈비탕.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label1 = Label(self, image=foodlist[0])
                            label1.image = foodlist[0]
                            label1.grid(row=1, column = 0)

                            img = Image.open("깍두기.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[1])
                            label2.image = foodlist[1]
                            label2.grid(row=0, column = 0)

                            img = Image.open("김치.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[2])
                            label2.image = foodlist[2]
                            label2.grid(row=0, column = 1)
                        
                        elif order == "백반":
                            img = Image.open("밥.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label1 = Label(self, image=foodlist[0])
                            label1.image = foodlist[0]
                            label1.grid(row=1, column = 0)

                            img = Image.open("국.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[1])
                            label2.image = foodlist[1]
                            label2.grid(row=0, column = 0)

                            img = Image.open("김치.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[2])
                            label2.image = foodlist[2]
                            label2.grid(row=0, column = 1)

                            img = Image.open("콩나물.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[3])
                            label2.image = foodlist[3]
                            label2.grid(row=0, column = 2)

                            img = Image.open("고등어구이.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[4])
                            label2.image = foodlist[4]
                            label2.grid(row=0, column = 3)

                        elif order == "삼겹살":
                            img = Image.open("삼겹살.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label1 = Label(self, image=foodlist[0])
                            label1.image = foodlist[0]
                            label1.grid(row=1, column = 0)

                            img = Image.open("상추.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[1])
                            label2.image = foodlist[1]
                            label2.grid(row=0, column = 0)

                            img = Image.open("김치.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[2])
                            label2.image = foodlist[2]
                            label2.grid(row=0, column = 1)

                            img = Image.open("고추장.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[3])
                            label2.image = foodlist[3]
                            label2.grid(row=0, column = 2)

                        elif order == "치킨":
                            img = Image.open("치킨.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label1 = Label(self, image=foodlist[0])
                            label1.image = foodlist[0]
                            label1.grid(row=1, column = 0)

                            img = Image.open("치킨무.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[1])
                            label2.image = foodlist[1]
                            label2.grid(row=0, column = 0)

                        elif order == "피자":
                            img = Image.open("피자.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label1 = Label(self, image=foodlist[0])
                            label1.image = foodlist[0]
                            label1.grid(row=1, column = 0)

                            img = Image.open("피클.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[1])
                            label2.image = foodlist[1]
                            label2.grid(row=0, column = 0)

                        elif order == "짜장면":
                            img = Image.open("짜장면.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label1 = Label(self, image=foodlist[0])
                            label1.image = foodlist[0]
                            label1.grid(row=1, column = 0)

                            img = Image.open("단무지.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[1])
                            label2.image = foodlist[1]
                            label2.grid(row=0, column = 0)

                            img = Image.open("양파.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[2])
                            label2.image = foodlist[2]
                            label2.grid(row=0, column = 1)

                            img = Image.open("춘장.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[3])
                            label2.image = foodlist[3]
                            label2.grid(row=0, column = 2)

                        elif order == "라면":
                            img = Image.open("라면.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label1 = Label(self, image=foodlist[0])
                            label1.image = foodlist[0]
                            label1.grid(row=1, column = 0)

                            img = Image.open("김치.gif")
                            foodlist.append(ImageTk.PhotoImage(img))
                            label2 = Label(self, image=foodlist[1])
                            label2.image = foodlist[1]
                            label2.grid(row=0, column = 0)
                root = Tk()
                root.geometry("1000x500")
                app = Example()
                root.mainloop()
            elif result == 0:
                continue
            else:
                print("모든 메뉴가 소진되었습니다. 영업을 종료합니다.")
                break
        for j in Menu_list:
            print(j, "\t[ 판매량:", sold_count[j], "재고량:", left_list[j], "]")
