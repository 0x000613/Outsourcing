# student 클래스 초기화
class Student:
    name = ''
    kor = ''
    eng = ''
    mat = ''

# student 생성자
student1 = Student()
student1.name = "학생1"
student2 = Student()
student2.name = "학생2"

# 총점을 반환하는 함수
def get_total(kor, eng, mat):
    # kor, eng, mat 값을 int로 형변환하고 모두 더함
    return (int(kor) + int(eng) + int(mat))

# 평균을 반환하는 함수
def get_average(totalPoint, count):
    # 총점을 count만큼 나눔
    return int(totalPoint) / count

# student의 수만큼 반복
for i in [student1, student2]:
    # 학생의 점수를 입력받음
    i.kor = input("{}의 국어 점수 입력 : ".format(i.name))
    i.eng = input("{}의 영어 점수 입력 : ".format(i.name))
    i.mat = input("{}의 수학 점수 입력 : ".format(i.name))
    # 학생의 총점을 get_total 함수를 이용해 얻어 출력
    print("{}의 총점 : {}".format(i.name, get_total(i.kor, i.eng, i.mat)))
    # 학생의 평균을 get_average함수에 인자로 get_total함수와 count를 줘서 얻고 출력
    print("{}의 평균 : {}".format(i.name, get_average(get_total(i.kor, i.eng, i.mat), 3)))