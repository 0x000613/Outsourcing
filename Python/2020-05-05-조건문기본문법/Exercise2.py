# 음식, 음료 종류
print("Select category.")
sel = input("\t1:Food  2:Drink\n") # 음식, 음료 선택

# 음식을 선택했을 경우
if sel == '1':
    print("You have selected FOOD. Select category")
    sel = input("\t1:Korean\t2:Chinese\t3:American\n") # 한식, 중식, 양식 선택
    # 한식을 선택했을 경우
    if sel == '1':
        print("You have selected KOREAN FOOD. Select your menu")
        sel = input("\t1:Rice\t2:Bulgogi\n")
        # 밥을 선택했을 경우
        if sel == '1':
            print("You have selected KOREAN RICE.\nEnjoy your RICE!")
        # 불고기를 선택했을 경우
        elif sel == '2':
            print("You have selected KOREAN BULGOGI.\nEnjoy your BULGOGI!")
    # 중식을 선택했을 경우
    elif sel == '2':
        print("You have selected CHINESE FOOD. Select your menu")
        sel = input("\t1:Noodle\t2:Dimsum\n")
        # 국수를 선택했을 경우
        if sel == '1':
            print("You have selected CHINESE NOODLE.\nEnjoy your NOODLE!")
        # 딤섬을 선택했을 경우
        elif sel == '2':
            print("You have selected CHINESE DIMSUM.\nEnjoy your DIMSUM!")
    # 양식을 선택했을 경우
    elif sel == '3':
        print("You have selected AMERICAN FOOD. Select your menu")
        sel = input("\t1:Hamburger\t2:Salad\n")
        # 햄버거를 선택했을 경우
        if sel == '1':
            print("You have selected AMERICAN HAMBURGER.\nEnjoy your Hamburger!")
        # 샐러드를 선택했을 경우
        elif sel == '2':
            print("You have selected AMERICAN Salad.\nEnjoy your Salad!")
# 음료를 선택했을 경우 
elif sel == '2':
    print("You have selected DRINK. Select menu.")
    sel = input("\t1:Coke  2:Water  3:Orange juice\n")
    # 콜라를 선택했을 경우
    if sel == '1':
        print("You have selected Coke.\nEnjoy your Coke!")
    # 물을 선택했을 경우
    if sel == '2':
        print("You have selected WATER.\nEnjoy your WATER!")
    # 오랜지쥬스를 선택했을 경우
    if sel == '3':
        print("You have selected ORANGE JUICE.\nEnjoy your ORANGE JUICE!")
