class Node :
    def __init__(self, item, left = None, right = None) :
        self.item = item
        self.left = left
        self.right = right


def getPreorder(n) :
    if n == -1 :
        print("루트 노드가 정의되지 않았습니다.'")
        return -1
        
    if n != None :
        list_item = list(n.item)

        if n.left :
            list_item += getPreorder(n.left)

        if n.right :
            list_item += getPreorder(n.right)

        return list_item

    else :
        print("루트 노드가 정의되지 않았습니다.'")
        return -1
