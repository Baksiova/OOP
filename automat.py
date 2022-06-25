
def calculation():
    round =input("New operation Y/N?")
    if round == "Y":
        class Kalkulacka:
            def __init__(self):
                self.number1= int(input("Choose number 1"))
                self.number2 = int(input("Choose number 2"))
            def sum(self):
                return self.number1+self.number2
            def substract(self):
                return self.number1-self.number2
            def divission(self):
                return self.number1/self.number2
            def multiply(self):
                return self.number1 * self.number2

        kalk = Kalkulacka()

        operation = input("Which operation you want to execute? Choose one:sum,substract,divission,multiply")
        if operation == "sum":
            print( kalk.sum())
        elif operation == "substract":
            print( kalk.substract())
        elif operation =="divission":
            print(kalk.divission())
        elif operation =="multiply":
            print(kalk.multiply())
        else:
            ("Bad input, try again")


        return calculation()
    else:
        return "Finish"



print(calculation())



