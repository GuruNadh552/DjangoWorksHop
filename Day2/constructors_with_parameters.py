class operations:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self,c):
        return ("Addition of the Numbers is " + (str(a+b+c)))
    def sub(self):
        return ("Subtraction of two numbers  is " + str(a-b))

a =int(input("Enter A Value : "))
b = int(input("Enter B Value : "))
c = int(input("Enter C Value : "))
ob = operations(a,b)
print(ob.add(c))
print(ob.sub())
