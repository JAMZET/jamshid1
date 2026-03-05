class ICommand:
    def execute(self):
        pass

    def undo(self):
        pass


class Light:
    def on(self):
        print("Жарық қосылды")

    def off(self):
        print("Жарық өшті")


class Door:
    def open(self):
        print("Есік ашылды")

    def close(self):
        print("Есік жабылды")


class Thermostat:
    def increase(self):
        print("Температура көтерілді")

    def decrease(self):
        print("Температура төмендеді")


class LightOnCommand(ICommand):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class DoorOpenCommand(ICommand):
    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.open()

    def undo(self):
        self.door.close()


class TempUpCommand(ICommand):
    def __init__(self, thermostat):
        self.thermostat = thermostat

    def execute(self):
        self.thermostat.increase()

    def undo(self):
        self.thermostat.decrease()

class RemoteControl:
    def __init__(self):
        self.history = []

    def press(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()
        else:
            print("Отменять нечего")

class Beverage:

    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Суды қайнату")

    def pour(self):
        print("Кесеге құю")

    def brew(self):
        pass

    def add_condiments(self):
        pass

    def customer_wants_condiments(self):
        return True


class Tea(Beverage):

    def brew(self):
        print("Шайды демдеу")

    def add_condiments(self):
        print("Лимон қосу")


class Coffee(Beverage):

    def brew(self):
        print("Кофені дайындау")

    def add_condiments(self):
        print("Сүт және қант қосу")

    def customer_wants_condiments(self):
        answer = input("Қоспа керек пе? (yes/no): ")
        return answer.lower() == "yes"
    
class ChatRoom:

    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message, sender)


class User:

    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom
        chatroom.add_user(self)

    def send(self, message):
        print(self.name, "жазады:", message)
        self.chatroom.send(message, self)

    def receive(self, message, sender):
        print(self.name, "алды:", sender.name, "-", message)

print("----- COMMAND PATTERN -----")

light = Light()
door = Door()
thermo = Thermostat()

remote = RemoteControl()

remote.press(LightOnCommand(light))
remote.press(DoorOpenCommand(door))
remote.press(TempUpCommand(thermo))

remote.undo()

print("\n----- TEMPLATE METHOD -----")

tea = Tea()
tea.prepare()

print("------")

coffee = Coffee()
coffee.prepare()

print("\n----- MEDIATOR PATTERN -----")

chat = ChatRoom()

u1 = User("Ali", chat)
u2 = User("Dana", chat)
u3 = User("Nurlan", chat)

u1.send("Сәлем!")
