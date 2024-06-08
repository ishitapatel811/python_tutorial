# OOP = Object Oriented programming
# OOP = Abstraction, Encapsulation, inheritance, polymorphism
# to map with real world scenarios,we started using objects in code

# Class & Object = class is blueprint for creating objects.
"""class Student:          # creating class
    name = "ishita"
s1 = Student()         # creating object (instance)
print(s1.name)"""

"""class Car:
    color = "blue"
    brand = "BMW"
car1 = Car()
print(car1.color)  """



# __init__ Function
# CONSTRUCTOR = all classes have a function called __init__(),which is always executed when
# the object is being initiated
# the SELF parameter is a reference to the current instance of the class,& is used to access
# variables that belongs to the class 
"""class Student:
    
    # default constructor
    def __init__(self):
        pass
    
    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student")
s1 = Student("ishita", 85)
print(s1.name, s1.marks)
s2 = Student("radhe", 90)
print(s2.name, s2.marks)"""




# Class & Instance Attributes
"""class Student:
    clg_name = "spu"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student")
s1 = Student("ishita", 85)
print(s1.clg_name)"""



# Methods = methods are function that belong to objects
"""class Student:
    clg_name = "spu"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student")

    def welcome(self):
        print("welcome student,", self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = Student("ishita",85)
s1.welcome()
print(s1.get_marks())"""



# create student class that takes name & marks of 3 subjects as argument in constructor
# then create method to print the average
"""class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is:",sum/3)
        
s1 = Student ("ishita",[75, 80, 85])  
s1.get_avg()
s1.name = "radhe"
s1.get_avg()"""



# Static methods = methods that don't use the self parameter(work at class level)
# @staticmethod (decorator) = it allows us to wrap another function in order to extend the 
# behavior of wrapped function,without permanently modifying it.

"""class Student:
    @staticmethod
    def hello():
        print("hello")
    hello()"""



# Abstraction = Hiding the implementation details of a class and only showing the
#               essential features to the user

"""class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("car start")
        
car1 = Car()
car1.start()"""



# Encapsulation = Wrapping data & function into a single unit(object).


# create account class with 2 attributes-balance & acc.no.
# create methods for debit, credit & printing balance
"""class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance =",self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance =",self.get_balance())
    
    def get_balance(self):
        return self.balance
        
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
print(acc1.balance)
print(acc1.acc_no)"""



# del keyword = used to delete object properties or object itself
"""class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("ish")
print(s1.name)
del s1.name
print(s1.name)"""



# Private (like) attributes & methods
# Conceptual Implementation in python
# Private attributes & methods are meant to be used only within the class and are not 
# accessible from outside the class.

"""class Person:
    __name = "ish"     # private
    def __hello(self):
        print("hello")
    def welcome(self):
        self.__hello()
        
p1 = Person()
print(p1.welcome())"""



# Inheritance = when one class(child/derived) derives the properties & methods of another
#               class (parent/base)
# types = Single, Multi-level, Multiple Inheritance

# Single Inheritance
"""class Car:
    color = "blue"
    @staticmethod
    def start():
        print("start")
    @staticmethod
    def stop():
        print("stop")
class ToyotaCar(Car):       # inheritance
    def __init__(self, name):
        self.name = name
        
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
print(car1.name)
print(car1.start())
print(car1.color)"""



# Multi-level Inheritance
"""class Car:
    @staticmethod
    def start():
        print("start")
    @staticmethod
    def stop():
        print("stop")
        
class ToyotaCar(Car):       # inheritance
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("petrol")
car1.start()  """


# Multiple Inheritance
"""class A:
    varA = "welcome to A"
class B:
    varB = "welcome to B"
    
class C(A,B):
    varC = "welcome to C"
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)"""



# Super method = it is used to access methods of the parent class
"""class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("start")
    @staticmethod
    def stop():
        print("stop")

class ToyotaCar(Car):       # inheritance
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        
car1 = ToyotaCar("prius","electric")
print(car1.type)"""



# class method = A class method is bound to the class & receives the class as an implicit
#                first argument
# note - static method can't access or modify class state & generally for utility

"""class Person:
    name = "anonymous"
    
    @classmethod      # decorator
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("ish")
print(p1.name)
print(Person.name)"""



#Property = we use @property decorator on any method in the class to use method as property
"""class Student:
    def __init__(self,phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/ 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)"""



# Polymorphism : Operator overloading
# when the same operator is allowed to have different meaning according to the context.

# Operators & Dunder(_ _) function
# a + b (addition) -> a.__add__(b)
# a / b(division)  -> a.__truediv____(b)

"""class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real, "i +",self.img, "j")
        
    def __add__(self, num2):        # addition
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    def __sub__(self, num2):        # subtraction
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    
num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(8,11)
num2.showNumber()
# num3 = num1 + num2
# num3.showNumber()
num3 = num1 - num2
num3.showNumber()"""



# define circle class to create circle with radius r using the constructor.
# define area() method of the class which calculates the area of the circle.
# define perimeter() method of class which allows to calculate perimeter of circle.
"""class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius ** 2
    def perimeter(self):
        return 2 * (22/7) *self.radius
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())"""



# define Employee class with attributes role,department,salary.this class showDetails() method
# create engineer class that inherits properties from employee & has additional attributes:name,age

"""class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)
e1 = Employee("accountant","finance","60000")
e1.showDetails()
        
class Engineer(Employee):    # inheritance
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")    
eng1 = Engineer("ish",20)
eng1.showDetails()"""



# create class Order which stores item & price.Use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2

"""class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, odr2):        # greater then
        return self.price > odr2.price
        
odr1 = Order("chips",20)
odr2 = Order("tea",15)
print(odr1 > odr2)"""

