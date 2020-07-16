'''
     Inheritance
     ------------
     -> it is a powerful object oriented programming
     -> it allow us to define a class with  a methods and properties

     Inheritance has two classes
    ------------------------------
     1. derived class or child class
     2.base class or parent class

     Syntax
     -------
    class parent _class :
            body of the class
    class derived_class(parent):
            body of derived class

    Inheritance we have few type :
    ---------------------------------
    1. single level
        Only one parent class and child class 
    2. multi level
        one or more parent class and one child class 
    3. multiple level
        more than one parent class and one child class

'''

#Single Level inheritance

class classA():
    a= 10
    b= 20
    def method1():
        return "I am From IIIT Srikakulam "
class classB(classA):
    c = 30
    d = 40
    def method2():
        return "I am From K-7 CSE-2D"
ob = classB
print(ob.a,ob.b,ob.method1())
print(ob.c,ob.d,ob.method2())

#Multilevel Inheritance

class ClassA:
    a = 10
    b = 20
    def display1():
        return "I am from Class A "
class ClassB(ClassA):
    c = 30
    d = 40
    def display2():
        return "I am From Class B"
class ClassC(ClassB):
    e = 50
    f = 60
    def display3():
        return "I am From Class C "
obj = ClassC
print(obj.a,obj.b,obj.display1())
print(obj.c,obj.d,obj.display2())
print(obj.e,obj.f,obj.display3())

#MultipleLevel Inheritance

class C1:
    p,q = 10,20
    def m1():
        return "THis is Guru1"
class C2(C1):
    x,y = 30,40
    def m2():
        return "THis is Guru2"
class C3:
    pp,q1 = 100,200
    def m3():
        return "THis is Guru3"
class C4(C2,C3):
    xx,yy = 1000,2000
    def m4():
        return "THis is Guru4"
ob1 = C4
print(ob1.x,ob1.y,ob1.m1())
print(ob1.p,ob1.q,ob1.m2())
print(ob1.pp,ob1.q1,ob1.m3())
print(ob1.xx,ob1.yy,ob1.m4())


