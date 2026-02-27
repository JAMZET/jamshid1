from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Card(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} теңге карта арқылы төленді.")


class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} теңге PayPal арқылы төленді.")


class Crypto(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} теңге крипто арқылы төленді.")


class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


class CurrencyExchange:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def set_rate(self, rate):
        for observer in self.observers:
            observer(rate)


def mobile(rate):
    print(f"📱 Қосымша: {rate}")


def bank(rate):
    print(f"🏦 Банк: {rate}")


def investor(rate):
    print(f"💰 Инвестор: {rate}")


if __name__ == "__main__":

    while True:
        print("\n1-Төлем  2-Курс  0-Шығу")
        choice = input("Таңдау: ")

        if choice == "1":
            amount = float(input("Сома: "))
            methods = {"1": Card(), "2": PayPal(), "3": Crypto()}
            m = input("1-Карта 2-PayPal 3-Крипто: ")
            if m in methods:
                PaymentContext(methods[m]).pay(amount)

        elif choice == "2":
            exchange = CurrencyExchange()
            exchange.attach(mobile)
            exchange.attach(bank)
            exchange.attach(investor)
            rate = float(input("Жаңа курс: "))
            exchange.set_rate(rate)

        elif choice == "0":
            break
        