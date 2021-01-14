from reference import Node, getPreorder

def getRoot(trueOrderList, myOrderList) :

    # 정답과 자기 자신의 답안을 비교하여 다르면 -1을 반환하도록 구조됨
    if len(trueOrderList) != len(myOrderList):
      return False
    if len(trueOrderList) and len(myOrderList) == 0 :
      return False

    # num 변수에 trueOrderList의 인덱스 길이를 저장
    num = len(trueOrderList)
    # pindex에 list 형태의 num에서 1을 뺀 값을 저장
    pindex = [num-1]
    RootNode = Node(myOrderList[pindex[0]])
    pindex[0]-=1
    lsize = 0

    # num의 범위만큼 반복문을 실행, 이때 item에는 매 반복되는 num의 값이 기입됨
    for item in range(num) :
       if trueOrderList[item] == myOrderList[pindex[0]+1] :
         lsize = item
         break      
    # num에 저장된 값이 2일경우
    if num==2:
      RootNode = Node(myOrderList[::-1])
      return RootNode
   
    if lsize == pindex[0]+1 :
      return RootNode

    trueOrderList1 = trueOrderList[lsize+1:pindex[0]+2] 
    trueOrderList2 = trueOrderList[0:lsize]
    myOrderList1 = myOrderList[lsize:pindex[0]+1]
    myOrderList2 = myOrderList[0:lsize]
                  
    RootNode.left = getRoot(trueOrderList2, myOrderList2)
    RootNode.right = getRoot(trueOrderList1, myOrderList1)   
   
    return RootNode
    
if __name__ == '__main__' :

    # 예제 문제 1
    trueOrderList = ['B', 'A', 'C']
    myOrderList = ['B', 'C', 'A']

    ## 본인이 작성한 코드를 통해 Root Node 구하기
    root = getRoot(trueOrderList, myOrderList)

    ## Root Node 기준으로 전위순회 출력하기
    preorderList = getPreorder(root)

    print("예제 문제 1")
    print("==============================")
    print("본인 답안 :", preorderList)
    print("------------------------------")
    print("  정 답   :", ['A', 'B', 'C'])
    print("==============================", end ="\n\n")


    # 예제 문제 2
    trueOrderList = ['J', 'E', 'N', 'K', 'O', 'P', 'B', 'F', 'A', 'C', 'L', 'G', 'M', 'D', 'H', 'I']
    myOrderList = ['J', 'N', 'O', 'P', 'K', 'E', 'F', 'B', 'C', 'L', 'M', 'G', 'H', 'I', 'D', 'A']

    ## 본인이 작성한 코드를 통해 Root Node 구하기
    root = getRoot(trueOrderList, myOrderList)

    ## Root Node 기준으로 전위순회 출력하기
    preorderList = getPreorder(root)
    
    print("예제 문제 2")
    print("==============================")
    print("본인 답안 :", preorderList)
    print("------------------------------")
    print("  정 답   :", ['A', 'B', 'E', 'J', 'K', 'N', 'P', 'O', 'F', 'D', 'G', 'L', 'C', 'M', 'I', 'H'])
    print("==============================", end ="\n\n")
