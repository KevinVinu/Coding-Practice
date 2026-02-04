# ENCAPSULATION OOP PRACTICE QUESTIONS
# 1. Create a Student class where marks are private and accessed using getter method.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  
    def get_marks(self):
        return self.__marks
s1 = Student("Kevin", 92)
print("Student Name:", s1.name)
print("Marks:", s1.get_marks())



# 2. Create a BankAccount class with private balance and methods to deposit and check balance.
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,mon):
        self.mon = mon
        self.__balance = self.__balance+ self.mon
    def balance(self):
        print(f"The balance after deposit is {self.__balance}")
b = BankAccount(1000)
b.deposit(500)
b.balance()
    
        

# 3. Create a Person class where age is private and cannot be negative.
class Person:
    def __init__(self,age):
        self.__age = age
    def check(self):
        if(self.__age<1):
            print("Wrong")
        else:
            print("Age updated")
p = Person(-10)
p.check()
    

# 4. Create a User class that hides password and verifies it using a method.
class User:
    def __init__(self,password):
        self.__password = password
    def auth(self):
        if(self.__password=="12345678"):
            print("Logged in")
        else:
            print("retry")
u = User("12345678")
u.auth()

# 5. Create an Employee class where salary is private and can be increased.
class Employee:
    def __init__(self,salary):
        self.__salary = salary
    def inc(self):
        print("After bonus : ",self.__salary+1000)
e = Employee(15000)
e.inc()

# 6. Create a Car class with private speed and methods accelerate and brake.
class Car:
    def __init__(self,speed):
        self.__speed = speed
    def acc(self):
        print("After acceleration the speed is: ",self.__speed+50)
    def brake(self):
        print("Braking applied ,speed reduced to 0")
c = Car(30)
c.acc()
c.brake()
# 7. Create a Mobile class where battery percentage is private and decreases when used.
class Mobile:
    def __init__(self, battery):
        self.__battery = battery   
    def use(self, usage):
        if usage <= self.__battery:
            self.__battery -= usage
            print(f"Mobile used for {usage}%. Battery left: {self.__battery}%")
        else:
            print("Not enough battery!")
    def show_battery(self):
        print(f"Current battery: {self.__battery}%")
m = Mobile(100)
m.use(30)
m.use(50)
m.show_battery()
# 8. Create an ATM class with hidden PIN and verification method.
class ATM:
    def __init__(self, pin):
        self.__pin = pin   
    def verify_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("PIN verified. Access granted.")
        else:
            print("Incorrect PIN. Access denied.")
atm = ATM(1234)
atm.verify_pin(1234)
atm.verify_pin(1111)


# 9. Create a Book class where price is private and cannot be negative.
class Book:
    def __init__(self, price):
        self.set_price(price)

    def set_price(self, price):
        if price >= 0:
            self.__price = price 
        else:
            print("Price cannot be negative!")
            self.__price = 0

    def get_price(self):
        return self.__price
b1 = Book(450)
print("Book price:", b1.get_price())

b2 = Book(-100)
print("Book price:", b2.get_price())


# 10. Create a Result class where marks list is private and modified using methods.
class Result:
    def __init__(self):
        self.__marks = [] 
    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
            print(f"Mark {mark} added")
        else:
            print("Invalid mark!")

    def remove_mark(self, mark):
        if mark in self.__marks:
            self.__marks.remove(mark)
            print(f"Mark {mark} removed")
        else:
            print("Mark not found")

    def show_marks(self):
        print("Marks:", self.__marks)
r = Result()
r.add_mark(85)
r.add_mark(90)
r.add_mark(120)
r.remove_mark(85)
r.show_marks()
