import threading
import copy
from abc import ABC, abstractmethod


class ConfigurationManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.settings = {}
        return cls._instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key, "Табылмады")


class Report:
    def __init__(self):
        self.header = ""
        self.content = ""
        self.footer = ""

    def show(self):
        print(self.header)
        print(self.content)
        print(self.footer)


class IReportBuilder(ABC):
    @abstractmethod
    def set_header(self, h): pass

    @abstractmethod
    def set_content(self, c): pass

    @abstractmethod
    def set_footer(self, f): pass

    @abstractmethod
    def get_report(self): pass


class TextReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, h):
        self.report.header = f"*** {h} ***"

    def set_content(self, c):
        self.report.content = c

    def set_footer(self, f):
        self.report.footer = f"--- {f} ---"

    def get_report(self):
        return self.report


class ReportDirector:
    def build(self, builder):
        builder.set_header("2026 жылғы есеп")
        builder.set_content("Сатылым +20% өсті")
        builder.set_footer("Есеп соңы")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.products = []
        self.delivery = 0
        self.payment = ""

    def add_product(self, product):
        self.products.append(product)

    def clone(self):
        return copy.deepcopy(self)

    def show(self):
        for p in self.products:
            print(p.name, p.price)
        print("Жеткізу:", self.delivery)
        print("Төлем түрі:", self.payment)


if __name__ == "__main__":

    c1 = ConfigurationManager()
    c2 = ConfigurationManager()
    c1.set("режим", "жөндеу")
    print("Бір ғана объект:", c1 is c2)

    director = ReportDirector()
    builder = TextReportBuilder()
    director.build(builder)
    report = builder.get_report()
    report.show()

    print("------")

    order1 = Order()
    order1.add_product(Product("Телефон", 200000))
    order1.delivery = 2000
    order1.payment = "Kaspi"

    order2 = order1.clone()
    order2.payment = "Қолма-қол"

    order1.show()
    print("------")
    order2.show()
