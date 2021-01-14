# 사용자로부터 숫자들을 입력받는다.
nums = input("콤마로 구분된 숫자를 입력하세요 : ").split(',')
# 입력받은 숫자들은 사실 문자형이므로 정수형으로 형변환해준다.
nums = list(map(int, nums))
# min함수를 이용해 최솟값을 구해 minNum 변수에 선언한다.
minNum = min(nums)
# max함수를 이용해 최댓값을 구해 maxNum 변수에 선언한다.
maxNum = max(nums)
# 구한 값을 출력한다.
print("최댓값 = {}\n최솟값 = {}".format(minNum, maxNum))