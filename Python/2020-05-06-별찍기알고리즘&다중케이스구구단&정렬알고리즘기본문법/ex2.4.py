j = 7
k = -1
# 리본 상단부
for i in range(1, 5):
    if k == -1: print('*' + ' '*k + ' '*j + '*'*i)
    elif i == 4: print('*' + ' '*(i-1) + '*' + ' '*(i-1) + '*')
    else: print('*' + ' '*k + '*' + ' '*j + '*' + ' '*k + '*')
    j -= 2
    k+=1

# 리본 하단부
j = 3
k = 1
for i in range(1, 3):
    print('*' + ' '*k + '*' + ' '*(j) + '*' + ' '*k + '*')
    k -= 1
    j += 2
print('*' + ' '*7 + '*')