class Command:
    def execute(self): pass
    def undo(self): pass


class Light:
    def on(self): print("Жарық қосылды")
    def off(self): print("Жарық өшірілді")


class TV:
    def on(self): print("Теледидар қосылды")
    def off(self): print("Теледидар өшірілді")


class LightOn(Command):
    def __init__(self,l): self.l=l
    def execute(self): self.l.on()
    def undo(self): self.l.off()


class TVOn(Command):
    def __init__(self,t): self.t=t
    def execute(self): self.t.on()
    def undo(self): self.t.off()


class MacroCommand(Command):
    def __init__(self,cmds): self.cmds=cmds
    def execute(self):
        for c in self.cmds:
            c.execute()


class Remote:
    def __init__(self):
        self.history=[]

    def press(self,cmd):
        cmd.execute()
        self.history.append(cmd)

    def undo(self):
        if self.history:
            self.history.pop().undo()
        else:
            print("Бас тартатын команда жоқ")


class Report:
    def generate(self):
        self.header()
        self.body()
        self.save()

    def header(self):
        print("Есептің тақырыбы")

    def body(self): pass
    def save(self): pass


class PdfReport(Report):
    def body(self): print("PDF есеп мазмұны")
    def save(self): print("PDF файлы сақталды")


class ExcelReport(Report):
    def body(self): print("Excel есеп мазмұны")
    def save(self): print("Excel файлы сақталды")


class HtmlReport(Report):
    def body(self): print("HTML есеп мазмұны")
    def save(self): print("HTML файлы сақталды")


class ChannelMediator:
    def __init__(self):
        self.channels={}

    def join(self,user,channel):
        self.channels.setdefault(channel,[]).append(user)
        print(user.name,"арнаға қосылды:",channel)

    def send(self,msg,user,channel):
        for u in self.channels.get(channel,[]):
            if u!=user:
                u.receive(msg)


class User:
    def __init__(self,name,med):
        self.name=name
        self.med=med

    def send(self,msg,channel):
        print(self.name,"жазады:",msg)
        self.med.send(msg,self,channel)

    def receive(self,msg):
        print(self.name,"хабар алды:",msg)


print("КОМАНДА ПАТТЕРНІ")

light=Light()
tv=TV()

r=Remote()
r.press(LightOn(light))
r.press(TVOn(tv))
r.undo()

macro=MacroCommand([LightOn(light),TVOn(tv)])
r.press(macro)


print("\nШАБЛОНДЫ ӘДІС")

PdfReport().generate()
ExcelReport().generate()
HtmlReport().generate()


print("\nПОСРЕДНИК (ЧАТ)")

med=ChannelMediator()

u1=User("Али",med)
u2=User("Дана",med)

med.join(u1,"жалпы")
med.join(u2,"жалпы")

u1.send("Сәлем!", "жалпы")
