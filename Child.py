from Parentfile import Calculator

class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 1 , 3)

    def GetCompleteData(self):
        return self.num2 + self.number + self.sum()


obj2 = Child()
print (obj2.GetCompleteData())


