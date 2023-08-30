# Inheritance, to inherite/use properties of paraent class
from Day10ConstructorInstaceVariable import calculator


class InheritateCalculator(calculator):
    num2 = 35

    def __init__(self):
        calculator.__init__(self, 15, 20)

    def newgetData(self):
        print("Total addition of parent & child class")
        return self.num + self.num2 + self.summation()


obj = InheritateCalculator()
print(obj.newgetData())