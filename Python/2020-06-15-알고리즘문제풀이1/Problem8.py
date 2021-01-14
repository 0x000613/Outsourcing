productList = [["비누", 3, 2], ["칫솔", 5, 4], ["샴푸", 2, 1], ["치약", 4, 4], ["로션", 5, 3]]
deleteProductList = []
goodProductList = []

for i in range(len(productList)):
    if productList[i][1] >= 4 and productList[i][2] >= 4:
        goodProductList.append(productList[i])
    elif productList[i][1] < 4 and productList[i][2] < 4:
        deleteProductList.append(productList[i])

print(deleteProductList)
print(goodProductList)