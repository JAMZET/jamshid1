from datetime import datetime

class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} жүйеге кірді")

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.total = 0
        self.status = "жасалды"

    def add_product(self, product, qty):
        if product.stock >= qty:
            self.items.append((product, qty))
            product.stock -= qty
            self.total += product.price * qty

    def pay(self):
        self.status = "төленді"

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        print("Төлем сәтті өтті")

class Delivery:
    def __init__(self):
        self.status = "жолда"

    def done(self):
        self.status = "жеткізілді"

user = User("Жамшид")
user.login()

product = Product("Телефон", 500, 5)

order = Order(user)
order.add_product(product, 2)
order.pay()

payment = Payment(order.total)
payment.process()

delivery = Delivery()
delivery.done()

print("Тапсырыс күйі:", order.status)
print("Жеткізу күйі:", delivery.status)
print("Жалпы сумма:", order.total)
