from abc import ABC, abstractmethod

# Абстракт класс
class Document(ABC):
    @abstractmethod
    def open(self):
        pass


# Нақты құжаттар
class Report(Document):
    def open(self):
        print("Есеп (Report) ашылды")


class Resume(Document):
    def open(self):
        print("Түйіндеме (Resume) ашылды")


class Letter(Document):
    def open(self):
        print("Хат (Letter) ашылды")


class Invoice(Document):
    def open(self):
        print("Шот-фактура (Invoice) ашылды")


# Абстракт фабрика
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass


# Нақты фабрикалар
class ReportCreator(DocumentCreator):
    def create_document(self):
        return Report()


class ResumeCreator(DocumentCreator):
    def create_document(self):
        return Resume()


class LetterCreator(DocumentCreator):
    def create_document(self):
        return Letter()


class InvoiceCreator(DocumentCreator):
    def create_document(self):
        return Invoice()


# Негізгі бағдарлама (динамикалық таңдау)
print("Құжат түрін таңдаңыз:")
print("1 - Есеп (Report)")
print("2 - Түйіндеме (Resume)")
print("3 - Хат (Letter)")
print("4 - Шот-фактура (Invoice)")

choice = input("Таңдау: ")

if choice == "1":
    creator = ReportCreator()
elif choice == "2":
    creator = ResumeCreator()
elif choice == "3":
    creator = LetterCreator()
elif choice == "4":
    creator = InvoiceCreator()
else:
    print("Қате таңдау!")
    exit()

document = creator.create_document()
document.open()
