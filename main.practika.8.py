from abc import ABC, abstractmethod

class IReport(ABC):
    @abstractmethod
    def generate(self): pass

class SalesReport(IReport):
    def generate(self):
        return "Sales: 100, 200, 300"

class UserReport(IReport):
    def generate(self):
        return "Users: A, B, C"

class ReportDecorator(IReport):
    def __init__(self, r): self.r = r

class DateFilter(ReportDecorator):
    def generate(self):
        return self.r.generate() + " | DateFilter"

class Sort(ReportDecorator):
    def generate(self):
        return self.r.generate() + " | Sorted"

class CsvExport(ReportDecorator):
    def generate(self):
        return self.r.generate() + " | CSV"

class PdfExport(ReportDecorator):
    def generate(self):
        return self.r.generate() + " | PDF"

r = SalesReport()
r = DateFilter(r)
r = Sort(r)
r = CsvExport(r)
print(r.generate())


class IInternalDeliveryService(ABC):
    @abstractmethod
    def deliver(self, id): pass
    @abstractmethod
    def status(self, id): pass

class InternalService(IInternalDeliveryService):
    def deliver(self, id):
        print("Internal deliver", id)
    def status(self, id):
        return "Delivered"

class ExternalA:
    def ship(self, item):
        print("A ship", item)
    def track(self, item):
        return "A status"

class ExternalB:
    def send(self, info):
        print("B send", info)
    def check(self, code):
        return "B status"

class AdapterA(IInternalDeliveryService):
    def __init__(self, a): self.a = a
    def deliver(self, id):
        self.a.ship(id)
    def status(self, id):
        return self.a.track(id)

class AdapterB(IInternalDeliveryService):
    def __init__(self, b): self.b = b
    def deliver(self, id):
        self.b.send(str(id))
    def status(self, id):
        return self.b.check(str(id))

class Factory:
    def get(self, t):
        if t == "internal": return InternalService()
        if t == "a": return AdapterA(ExternalA())
        if t == "b": return AdapterB(ExternalB())

f = Factory()
s = f.get("a")
s.deliver(1)
print(s.status(1))