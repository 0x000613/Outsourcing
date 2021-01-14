# 숫자를 입력받아서 한글로 출력하는 함수
# 1~999
def readNumber(n):
  units = [''] + list('십백천')
  nums = '일이삼사오육칠팔구'
  result = []
  i = 0
  while n > 0:
    n, r = divmod(n, 10)
    if r > 0:
      result.append(nums[r-1] + units[i])
    i += 1
  return ''.join(result[::-1])

# 구구단 결과 1
for dan in range(9, 1, -1):
    print(">>> 구구단 <<<")
    print("==={}단===".format(dan))
    for x in range(9, 0, -1):
        print("{} X {} = {}".format(dan, x, dan*x))

# 구구단 결과 2
for dan in range(9, 1, -1):
    print(">>> 구구단 <<<")
    print("==={}단===".format(dan))
    for x in range(9, 0, -1):
        print("{} X {} = {}".format(readNumber(dan), readNumber(x), dan*x))

# 구구단 결과 3
for dan in range(9, 1, -1):
    print(">>> 구구단 <<<")
    print("==={}단===".format(dan))
    for x in range(9, 0, -1):
        print("{} X {} = {}".format(readNumber(dan), readNumber(x), readNumber(dan*x)))

# 구구단 결과 4
for dan in range(2, 10):
    print(">>> 구구단 <<<")
    print("==={}단===".format(dan))
    for x in range(1, 10):
        print("{} X {} = {}".format(readNumber(dan), readNumber(x), readNumber(dan*x)))