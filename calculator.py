class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def division(self):
        return self.num1/self.num2
obj=calculator(20,5)
print("addition of num1 and num2 is ",obj.add())
print("subraction of num1 and num2 is ",obj.sub())
print("multiplication  of num1 and num2 is ",obj.multiply())
print("division of num1 and num2 is ",obj.division())