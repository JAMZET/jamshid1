from abc import ABC, abstractmethod

# Интерфейс
class IVehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


# Нақты транспорттар
class Car(IVehicle):
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def drive(self):
        print(f"{self.brand} {self.model} автокөлігі қозғалып жатыр")

    def refuel(self):
        print(f"{self.brand} {self.model} автокөлігіне {self.fuel_type} құйылды")


class Motorcycle(IVehicle):
    def __init__(self, moto_type, engine_volume):
        self.moto_type = moto_type
        self.engine_volume = engine_volume

    def drive(self):
        print(f"{self.moto_type} мотоциклі қозғалып жатыр")

    def refuel(self):
        print("Мотоциклге бензин құйылды")


class Truck(IVehicle):
    def __init__(self, capacity, axles):
        self.capacity = capacity
        self.axles = axles

    def drive(self):
        print(f"{self.capacity} тонна жүк көлігі қозғалып жатыр")

    def refuel(self):
        print("Жүк көлігіне дизель отыны құйылды")


class Bus(IVehicle):
    def __init__(self, seats):
        self.seats = seats

    def drive(self):
        print(f"{self.seats} орындық автобус қозғалып жатыр")

    def refuel(self):
        print("Автобусқа газ құйылды")


# Абстракт фабрика
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


# Нақты фабрикалар
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        brand = input("Автокөлік маркасын енгізіңіз: ")
        model = input("Автокөлік моделін енгізіңіз: ")
        fuel = input("Отын түрін енгізіңіз: ")
        return Car(brand, model, fuel)


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        moto_type = input("Мотоцикл түрін енгізіңіз: ")
        engine = input("Қозғалтқыш көлемін енгізіңіз: ")
        return Motorcycle(moto_type, engine)


class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        capacity = input("Жүк көтергіштігін енгізіңіз (тонна): ")
        axles = input("Ось санын енгізіңіз: ")
        return Truck(capacity, axles)


class BusFactory(VehicleFactory):
    def create_vehicle(self):
        seats = input("Орын санын енгізіңіз: ")
        return Bus(seats)


# Негізгі бағдарлама
print("1 - Автокөлік")
print("2 - Мотоцикл")
print("3 - Жүк көлігі")
print("4 - Автобус")

choice = input("Қандай көлік түрін таңдайсыз? ")

if choice == "1":
    factory = CarFactory()
elif choice == "2":
    factory = MotorcycleFactory()
elif choice == "3":
    factory = TruckFactory()
elif choice == "4":
    factory = BusFactory()
else:
    print("Қате таңдау жасалды!")
    exit()

vehicle = factory.create_vehicle()
vehicle.drive()
vehicle.refuel()
