
# to call construtor in class you have to use
# def __init__(self): => by default constructor
#self => used to call instance variable for methods return

class calculator():
    num = 15
    def __init__(self, a, b):
        print("Constructor will call once object of class is created by default")
        self.FirstNo = a
        self.SecondNo =b


    def getData(self):
        print("Method in class Calculator")


    def summation(self):
        print("Print addition of provided numbers")
        return self.FirstNo + self.SecondNo + calculator.num

obj = calculator(4, 5)
obj.getData()
obj.summation()
print(obj.summation())

obj1 = calculator(7, 8)
obj1.getData()
obj1.summation()
print(obj1.summation())
