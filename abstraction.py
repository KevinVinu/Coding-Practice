# ABSTRACTION OOPS PRACTICE QUESTIONS IN PYTHON

# 1. Create an abstract class Animal with abstract method sound() and implement it in Dog class.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
dog = Dog()
dog.sound()


# 2. Create an abstract class Shape with abstract method area() and implement it in Rectangle class.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,a,b):
        print(a*b)
r = Rectangle()
r.area(1,5)

# 3. Create an abstract class Bank with abstract method interest_rate() and implement it in SBI class.
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass
class SBI(Bank):
    def interest_rate(self,p,r,t):
        print((p*r*t)/100)
s = SBI()
s.interest_rate(5000,5,2)
# 4. Create an abstract class Vehicle with abstract method speed() and implement it in Car class.
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass
class Car(Vehicle):
    def speed(self,s):
        print("speed is ",s)
c = Car()
c.speed(100)
# 5. Create an abstract class Employee with abstract method salary() and implement it in Developer class.
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class Developer(Employee):
    def salary(self,sal):
        print("Salary is",sal)
d = Developer()
d.salary(1000)
# 6. Create an abstract class Payment with abstract method pay(amount) and implement it in UPI class.
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print(f"Payment to be done is ${amount}")
u = UPI()
u.pay(20)
# 7. Create an abstract class Mobile with abstract method features() and implement it in Samsung class.
from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def features(self):
        pass
class Samsung(Mobile):
    def features(self):
        print("It has camera features of its own")
s = Samsung()
s.features()
# 8. Create an abstract class Course with abstract method duration() and implement it in PythonCourse class.
from abc import ABC,abstractmethod
class Course(ABC):
    @abstractmethod
    def duration(self):
        pass
class PythonCourse(Course):
    def duration(self,d):
        print(f"The duration for the course is {d} months")
p = PythonCourse()
p.duration(10)
# 9. Create an abstract class Food with abstract method price() and implement it in Pizza class.
from abc import ABC,abstractmethod
class Food(ABC):
    @abstractmethod
    def price(self):
        pass
class Pizza(Food):
    def price(self,p):
        print(f"The price of the pizza is {p}rs per slice")
p = Pizza()
p.price(14)
# 10. Create an abstract class Electronics with abstract method warranty() and implement it in Laptop class.
from abc import ABC,abstractmethod
class Electronics(ABC):
    @abstractmethod
    def warranty(self):
        pass
class Laptop(Electronics):
    def warranty(self,t):
        print(f"The warranty is {t} years")
l = Laptop()
l.warranty(3)