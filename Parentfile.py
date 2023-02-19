class Calculator:
    number= 100
    def __init__(self, a , b):
        self.a = a
        self.b = b
        print ("This is the constructor of parent file")

    def GetData(self):
        print("Iam a method in the parent class")

    def sum (self):
        return self.a + self.b + self.number


obj= Calculator (9,10)
obj.GetData()
print("Sum in parent class: " , obj.sum())

