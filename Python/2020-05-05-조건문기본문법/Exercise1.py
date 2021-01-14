# rank와 credit을 초기화 선언
rank = {'A':0, 'B':0, 'C':0, 'D':0}
credit = 0

print("To calculate your GPA, type your rank and credits.")
# 반복적으로 입력받기위해 while 선언
while True:
    # t(temp)_rank와 credit을 input 함수를 통해 입력받음
    t_rank, t_credit = input("Type your rank and credit:").split()
    # credit에 새로 입력받은 t_credit을 합연산하여 조건으로 사용
    if credit + int(t_credit) > 18: # credit의 합이 18을 초과할경우
        print("Total credit should be 18")
        break
    else: # credit의 합연산 결과가 18을 초과하지 않을 경우
        credit += int(t_credit) # credit에 t_credit을 합연산하여 저장
        try:
            rank[t_rank] += int(t_credit) # 딕셔너리 형태의 rank에서 t_rank라는 key를 찾아 해당 key의 value를 t_credit만큼 합연산하여 저장
        except KeyError: # rank에서 해당 key를 찾지 못할 경우 에러발생
            print("Wrong 'RANK' input")
            break
        if credit == 18: # credit의 합이 18일 경우
            res = float(((rank['A'] * 4.0) + (rank['B'] * 3.0) + (rank['C'] * 2.0 + rank['D'] * 1.0))/18) # GPA 계산
            print("Your GPA is {}".format(round(res, 2)))