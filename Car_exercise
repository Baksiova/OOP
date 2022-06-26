class Car:
    def __init__(self,naklad = 0):
        self.naklad = naklad
    def nalozit(self, nalozene_mnozstvi):
        self.naklad = self.naklad +nalozene_mnozstvi
    def vylozit(self,vylozene_mnozstvi):
        self.naklad = self.naklad -vylozene_mnozstvi
    def vysledek(self):
        return self.naklad

auto=Car()

def preprava():
    if auto.naklad >=0 and auto.naklad <= 3000:
        akce= input("Chces nalozit, vylozit, nebo skoncit?")
        if akce == "nalozit":
            mnozstvi = int(input("Kolik v kg chces nalozit?"))
            auto.nalozit(mnozstvi)
            return preprava()
        elif akce == "vylozit":
            mnozstvi = int(input("Kolik v kg chces vylozit?"))
            auto.vylozit(mnozstvi)
            return preprava()
        else:
            return "V nakladnnem aute je nalozeno",auto.vysledek(), "kg"

    else:
        return "Prekrocil si povolenu hmotnost 3 000 kg nebo si chtel vylozit co nemas"

print(preprava())
