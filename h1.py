# 1. Create a parent class Payment and child classes UPI, CreditCard, and Cash. 
#    Implement a method in Payment to pay amount and specific methods in each child for payment type.
class Payment:
    def pay(self,amount):
        self.amount = amount
        print(f"Paying amount: {self.amount}")
class Upi(Payment):
    def pay_amount(self):
        print(f"Paying through upi: {self.amount}")
class CreditCard(Payment):
    def pay_amount(self):
        print(f"Paying through credit card: {self.amount}")
class Cash(Payment):
    def pay_cash(self):
        print(f"Paying through cash : {self.amount}")

p = Upi()
p.pay(500)
p.pay_amount()

# 2. Create a parent class Exam and child classes OnlineExam and OfflineExam. 
#    Add functionality for starting the exam and special features for each exam mode.
class Exam:
    def start(self,student):
        self.student = student
        print(f"The exam is going to start for the student: {self.student}")
class OnlineExam(Exam):
    def online(self):
        print(f"Online exam for {self.student} is going to start")
        print("Camera is turning on")
class OfflineExam(Exam):
    def offline(self):
        print(f"Offline exam for {self.student} is going to start")
        print("Invigilators are ready")
o = OnlineExam()
o.start("Kevin")
o.online()

of = OfflineExam()
of.start("Kevin")
of.offline()

# 3. Create a parent class Transport and child classes Train, Flight, and Ship. 
#    Implement common travel method and specialized travel methods for each transport type.

class Transport:
    def travel(self,destination):
        self.destination = destination
        print(f"The travel destination is {self.destination}")
class Train(Transport):
    def train_travel(self):
        print(f"Traveling to the {self.destination} through train")
class Flight(Transport):
    def flight_travel(self):
        print(f"traveling to the {self.destination} through flight")
class Ship(Transport):
    def ship_travel(self):
        print(f"traveling to the {self.destination} through ship")
t = Train()
t.travel("Scotland")
t.train_travel()


# 4. Create a parent class Content and child classes Blog, Video, and Podcast. 
#    Implement content publishing and specialized creation methods in each content type.

class Content:
    def vid(self,con):
        self.con = con
        print(f"Ur content is {self.con}")
class Blog(Content):
    def blog(self):
        print("The content for ur blog is {self.con}")
class Video(Content):
    def video(self):
        print("The content for ur video is {self.content}")
class Podcast(Content):
    def pod(self):
        print("The content for ur podcast is {self.content}")
b = Blog()
b.vid("entertainment")
b.blog()

v = Video()
v.vid("comedy")
v.video()

# 5. Create a parent class Ticket and child classes MovieTicket, BusTicket, and FlightTicket. 
#    Add ticket booking functionality and special booking details for each ticket type.

class Ticket:
    def confirm(self,num):
        self.num = num
        print(f"Ur ticket are booked")
class MovieTicket(Ticket):
    def mov(self):
        print(f"Number of movie tickets booked are {self.num}")
class BusTicket(Ticket):
    def bus(self):
        print(f"Number of bus tickets booked are : {self.num}")
class FlightTicket(Ticket):
    def flight(self):
        print(f"Number of flight tickets booked are: {self.num}")
m = MovieTicket()
m.confirm(5)
m.mov()

b = BusTicket()
b.confirm(10)
b.bus()

# 6. Create a parent class File and child classes PDF, ImageFile, and AudioFile. 
#    Implement file opening method and specialized actions for each file type.
class File:
    def action(self,stat):
        self.stat = stat
        print(f"The file is {self.stat}")
class PDF(File):
    def pdf(self):
        print(f"The file is {self.stat} in pdf format")
class ImageFile(File):
    def image(self):
        print(f"The file is {self.stat} in image format")
class AudioFile(File):
    def audio(self):
        print(f"The file is {self.stat} in audio format")
p = PDF()
p.action("open")
p.pdf()

a = AudioFile()
a.action("close")
a.audio()

# 7. Create a parent class Service and child classes Cleaning, Repair, and Delivery. 
#     Implement service request functionality and specialized service methods for each service type.
class Service:
    def s(self,service):
        self.service  = service
        print(f"The service is scheduled in {self.service} days")
class Cleaning(Service):
    def clean(self):
        print("The service for cleaning is under process")
class Repair(Service):
    def rep(self):
        print("The service for repair is under process")
class Delivery(Service):
    def deli(self):
        print("The service for delivery is under process")
c = Cleaning()
c.s(7)
c.clean()

# 8. Create a parent class Notification and child classes Email, SMS, and Push. 
#    Implement a general send method and specific send methods for each notification type.
class Notification:
    def send(self, message):
        self.message = message
        print(f"Sending notification: {self.message}")
class Email(Notification):
    def send_email(self):
        print(f"Email sent with message: {self.message}")
class SMS(Notification):
    def send_sms(self):
        print(f"SMS sent with message: {self.message}")
class Push(Notification):
    def send_push(self):
        print(f"Push notification sent with message: {self.message}")
email = Email()
email.send("Exam results published")
email.send_email()

print()

sms = SMS()
sms.send("OTP for login")
sms.send_sms()

print()

push = Push()
push.send("New update available")
push.send_push()


# 9. Create a parent class Employee and child classes HR, Engineer, and Sales. 
#    Implement attendance functionality and specific job-related methods in each child.

class Employee:
    def mark_attendance(self, name):
        self.name = name
        print(f"Attendance marked for employee: {self.name}")
class HR(Employee):
    def conduct_interview(self):
        print(f"{self.name} is conducting interviews")
class Engineer(Employee):
    def write_code(self):
        print(f"{self.name} is writing code")
class Sales(Employee):
    def sell_product(self):
        print(f"{self.name} is selling products")
hr = HR()
hr.mark_attendance("Kevin")
hr.conduct_interview()
print()
eng = Engineer()
eng.mark_attendance("Alex")
eng.write_code()
print()
sales = Sales()
sales.mark_attendance("Riya")
sales.sell_product()

# 10. Create a parent class Order and child classes FoodOrder, GroceryOrder, and MedicineOrder. 
#    Add order placement method and specialized processing methods for each order type.

class Order:
    def place_order(self, order_id):
        self.order_id = order_id
        print(f"Order placed successfully. Order ID: {self.order_id}")
class FoodOrder(Order):
    def process_food(self):
        print(f"Food order {self.order_id} is being prepared and packed")
class GroceryOrder(Order):
    def process_grocery(self):
        print(f"Grocery order {self.order_id} is being packed and ready for delivery")
class MedicineOrder(Order):
    def process_medicine(self):
        print(f"Medicine order {self.order_id} is being verified and dispatched")
food = FoodOrder()
food.place_order("FO123")
food.process_food()
print()
grocery = GroceryOrder()
grocery.place_order("GO456")
grocery.process_grocery()
print()
medicine = MedicineOrder()
medicine.place_order("MO789")
medicine.process_medicine()

