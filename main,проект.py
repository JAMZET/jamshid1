class VirtualServer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.os = None
        self.storage = None
        self.storage_type = None
        self.network = None
        self.options = []

    def show_config(self):
        print("===== Сервер конфигурациясы =====")
        print(f"Процессор: {self.cpu} ядро")
        print(f"Жедел жады: {self.memory} GB")
        print(f"Операциялық жүйе: {self.os}")
        print(f"Диск: {self.storage} GB {self.storage_type}")
        print(f"Желі конфигурациясы: {self.network}")
        print("Қосымша опциялар:", ", ".join(self.options))

class Server:
    def __init__(self):
        self.server = VirtualServer()

    def set_cpu(self, cores):
        self.server.cpu = cores
        return self

    def set_memory(self, size):
        self.server.memory = size
        return self

    def set_operating_system(self, os_type):
        self.server.os = os_type
        return self

    def set_storage(self, size, storage_type):
        self.server.storage = size
        self.server.storage_type = storage_type
        return self

    def set_network_configuration(self, config):
        self.server.network = config
        return self

    def add_option(self, option):
        self.server.options.append(option)
        return self

    def build(self):
        return self.server

development_server = (
    Server()
    .set_cpu(2)
    .set_memory(4)
    .set_operating_system("Linux")
    .set_storage(100, "SSD")
    .set_network_configuration("192.168.1.10")
    .add_option("Резервтік көшіру")
    .build()
)

print("=== Даму сервері ===")
development_server.show_config()

print()

production_server = (
    Server()
    .set_cpu(16)
    .set_memory(64)
    .set_operating_system("Windows Server")
    .set_storage(1000, "SSD")
    .set_network_configuration("10.0.0.1")
    .add_option("Мониторинг")
    .add_option("Автоматты жаңарту")
    .build()
)

print("=== Продакшн сервері ===")
production_server.show_config()

