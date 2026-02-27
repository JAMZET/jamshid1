from abc import ABC, abstractmethod


class CostStrategy(ABC):
    @abstractmethod
    def calculate(self, d, p, c):
        pass


class Plane(CostStrategy):
    def calculate(self, d, p, c):
        base = d * 0.5
        if c == "business":
            base *= 1.5
        return base * p


class Train(CostStrategy):
    def calculate(self, d, p, c):
        base = d * 0.3
        if c == "business":
            base *= 1.3
        return base * p


class Bus(CostStrategy):
    def calculate(self, d, p, c):
        return d * 0.2 * p


class Travel:
    def __init__(self, strategy):
        self.strategy = strategy

    def calc(self, d, p, c):
        return self.strategy.calculate(d, p, c)


class StockExchange:
    def __init__(self):
        self.subs = {}

    def subscribe(self, stock, obs):
        self.subs.setdefault(stock, []).append(obs)

    def set_price(self, stock, price):
        print(f"{stock} = {price}")
        for o in self.subs.get(stock, []):
            o(stock, price)


def trader(stock, price):
    print(f"Трейдер: {stock} {price}")


def robot(limit):
    return lambda s, p: print(f"Робот сатып алды {s}") if p < limit else None


if __name__ == "__main__":

    while True:
        print("\n1-Travel 2-Stock 0-Exit")
        ch = input("Таңдау: ")

        if ch == "1":
            try:
                d = float(input("Қашықтық: "))
                p = int(input("Жолаушы: "))
                c = input("econom/business: ")
                types = {"1": Plane(), "2": Train(), "3": Bus()}
                t = input("1-Plane 2-Train 3-Bus: ")
                if t in types:
                    cost = Travel(types[t]).calc(d, p, c)
                    if input("Жеңілдік бар ма? yes/no: ") == "yes":
                        cost *= 0.9
                    print("Баға:", round(cost, 2))
            except:
                print("Қате!")

        elif ch == "2":
            ex = StockExchange()
            ex.subscribe("AAPL", trader)
            ex.subscribe("AAPL", robot(100))
            s = input("Акция (AAPL): ")
            try:
                price = float(input("Баға: "))
                ex.set_price(s, price)
            except:
                print("Қате!")

        elif ch == "0":
            break