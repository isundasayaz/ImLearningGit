class combineall:
    number1 = 100

    def __init__(self, a , b):
        self.a = a
        self.b = b
        print("Hello Im a constructor")

    def method(self):
        print("I'm a function in the parent class")

    def addition(self, a, b):
        return a + b


class clas2(combineall):
    number = 1000

    def __init__(self):
        combineall.__init__(self)
        print("hello Im the child")

    def pnc(self):
        x = self.number1 * self.number + self.addition()
        print(x)


chill = clas2(1 , 2)
chill.addition(5,5)
chill.pnc()

