class raise_exception:
    def exception_raise_method1(self):
        num = 0
        if num != 2:
            raise Exception("Excepted condition is failing")
            # print("Failing of test cases")

    def exception_raise_method2(self):
        num1 = 0
        assert (num1 == 2)

classObj1 = raise_exception()
classObj1.exception_raise_method2()
classObj = raise_exception()
classObj.exception_raise_method1()

