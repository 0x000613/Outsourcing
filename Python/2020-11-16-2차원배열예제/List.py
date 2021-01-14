def CREAT_LIST():
    arr = []
    return arr
    
def INPUT_LIST(arr):
    print("- 리스트 크기 입력- ")
    x = int(input("x값 입력: "))
    y = int(input("y값 입력: "))
    print('\n- 리스트 요소 입력 -')
    for xitem in range(x):
        arr.append([])
        for yitem in range(y):
            arr[xitem].append(int(input("arr[{}][{}] 값 입력: ".format(xitem, yitem))))
    return arr, x, y

def PRINT_LIST(arr, x, y):
    print("\n- 리스트 출력 -", end='')
    for xitem in range(x):
        print()
        for yitem in range(y):
            print(arr[xitem][yitem], end=' ')

inputReturnData = INPUT_LIST(CREAT_LIST())
PRINT_LIST(inputReturnData[0], inputReturnData[1], inputReturnData[2]) 