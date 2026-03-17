from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def cost(self): pass
    @abstractmethod
    def desc(self): pass

class Espresso(Beverage):
    def cost(self): return 2
    def desc(self): return "Espresso"

class Tea(Beverage):
    def cost(self): return 1.5
    def desc(self): return "Tea"

class Latte(Beverage):
    def cost(self): return 3
    def desc(self): return "Latte"

class Decorator(Beverage):
    def __init__(self, b): self.b = b

class Milk(Decorator):
    def cost(self): return self.b.cost() + 0.5
    def desc(self): return self.b.desc() + ", Milk"

class Sugar(Decorator):
    def cost(self): return self.b.cost() + 0.2
    def desc(self): return self.b.desc() + ", Sugar"

class Cream(Decorator):
    def cost(self): return self.b.cost() + 0.7
    def desc(self): return self.b.desc() + ", Cream"

d = Espresso()
d = Milk(d)
d = Sugar(d)
print(d.desc(), d.cost())

class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount): pass

class PayPal(IPaymentProcessor):
    def process(self, amount):
        print("PayPal:", amount)

class StripeService:
    def make_transaction(self, total):
        print("Stripe:", total)

class StripeAdapter(IPaymentProcessor):
    def __init__(self, s): self.s = s
    def process(self, amount):
        self.s.make_transaction(amount)

p1 = PayPal()
p1.process(100)

p2 = StripeAdapter(StripeService())
p2.process(200)