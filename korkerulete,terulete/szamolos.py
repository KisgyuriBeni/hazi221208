from terulet import Rest02
from kerulet import Rest01

class kor:
    def __init__(self):
        self.radius = 0
        self.result01 = 0
        self.resutl02 = 0
        self.choose = 0
        
    def getData(self):
        self.radius = float(input("Kör Sugara:"))
    
    def getResult01(self):
        self.rest01 = Rest01().getKeruletResult(self.radius)
        print("Kör Kerülete:{:.3f}".format(self.rest01))
    
    def getResult02(self):
        self.rest02 = Rest02().getTeruletResult(self.radius)
        print("Kör Területe:{:.3f}".format(self.rest02))

    def chooseResult(self):
        print("Terület[1] Kerület[2]")
        self.choose = int(input("Válassz:"))

        if self.choose == 1:
            Kor.getData
            Kor.getResult01()

        elif self.choose == 2:
            Kor.getData
            Kor.getResult02()

        else:
            print("1 vagy 2! TEGECI")
            Kor.chooseResult()  


Kor = kor()
Kor.getData()
Kor.chooseResult()

