import threading
import copy
from abc import ABC, abstractmethod


class Logger:
    _instance = None
    _lock = threading.Lock()
    LEVELS = {"INFO": 1, "WARNING": 2, "ERROR": 3}

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.level = 1
                    cls._instance.file = "log.txt"
        return cls._instance

    def set_level(self, level):
        self.level = self.LEVELS[level]

    def log(self, msg, level):
        if self.LEVELS[level] >= self.level:
            with open(self.file, "a", encoding="utf-8") as f:
                f.write(f"{level}: {msg}\n")


class LogReader:
    def __init__(self, file):
        self.file = file

    def read(self, level):
        print("\nСүзілген жазбалар:")
        with open(self.file, encoding="utf-8") as f:
            for line in f:
                if level in line:
                    print(line.strip())


class Report:
    def __init__(self):
        self.header = ""
        self.footer = ""

    def show(self):
        print(self.header)
        print(self.footer)


class Builder(ABC):
    @abstractmethod
    def set_header(self, h): pass

    @abstractmethod
    def set_footer(self, f): pass

    @abstractmethod
    def get(self): pass


class TextBuilder(Builder):
    def __init__(self):
        self.report = Report()

    def set_header(self, h):
        self.report.header = f"*** {h} ***"

    def set_footer(self, f):
        self.report.footer = f"--- {f} ---"

    def get(self):
        return self.report


class Character:
    def __init__(self, hp):
        self.hp = hp

    def clone(self):
        return copy.deepcopy(self)

    def show(self):
        print("Денсаулық:", self.hp)


if __name__ == "__main__":

    logger = Logger()
    logger.set_level("INFO")
    logger.log("Бағдарлама іске қосылды", "INFO")

    reader = LogReader("log.txt")
    reader.read("INFO")

    b = TextBuilder()
    b.set_header("Есеп 2026")
    b.set_footer("Есеп аяқталды")
    b.get().show()

    print("-------------")

    hero = Character(100)
    clone = hero.clone()
    clone.hp = 150

    hero.show()
    clone.show()
