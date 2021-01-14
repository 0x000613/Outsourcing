class student():
    name = ""
    midterm = 0
    finals = 0
    assignment = 0
    addAllPoint = 0
    avgPoint = 0

mystudent = student()

def addAll(num1, num2, num3):
    return num1 + num2 + num3

def getAvg(allNum, count):
    return int(allNum)/int(count)

mystudent.name = input("이름 입력 : ")
mystudent.midterm = input("중간고사 성적 입력 : ")
mystudent.finals = input("기말고사 성적 입력 : ")
mystudent.assignment = input("과제 성적 입력 : ")
print("\n")

mystudent.addAllPoint = addAll(mystudent.midterm, mystudent.finals, mystudent.assignment)
mystudent.avgPoint = getAvg(mystudent.addAllPoint, 3)

print("학생이름 = {}\n합계 = {}\n평균 = {}".format(mystudent.name, mystudent.addAllPoint, mystudent.avgPoint))