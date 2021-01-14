class Calc:
    def __init__(self, num=0):
        self.number = num

    def add(self, num):
        self.number += num

    def minus(self, num):
        self.number -= num

    def setvalue(self, num):
        self.number = num

    def print(self):
        print(self.number)

    def getvalue(self):
        return self.number

cal1 = Calc()
cal2 = Calc(5)
cal1.setvalue(10)
cal1.add(20)
cal1.minus(5)
cal1.print()
cal2.add(cal1.getvalue())
cal2.print()