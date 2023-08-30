
# classes are user defined
# classes contain variables, methods, constructors etc
# to call class, need to create object of class,

class calculator():
    num = 10
    def getData(self):
        print("This is first method in class by me")

obj = calculator()
obj.getData()
obj.num
print(obj.num)