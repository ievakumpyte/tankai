class Tankas:
    def __init__(self, suviu_sk,krypties_sk, kryptis="", koord="", x=0, y=0, taskai=100):
        self.taskai = taskai
        self.kryptis = kryptis
        self.krypties_sk = krypties_sk
        self.suviu_sk = suviu_sk
        self.koord = [x, y]
        self.x = x
        self.y = y


    def pirmyn(self):
        if self.kryptis == "S":
            self.y += 1
            self.koord[1] = self.y
            return self.kryptis
        if self.kryptis == "V":
            self.x -= 1
            self.koord[0] = self.x
            return self.kryptis
        if self.kryptis == "R":
            self.x += 1
            self.koord[0] = self.x
            return self.kryptis
        if self.kryptis == "P":
            self.y -= 1
            self.koord[1] = self.y
            return self.kryptis

    def atgal(self):
        if self.kryptis == "S":
            self.y -= 1
            self.koord[1] = self.y
            self.kryptis = "P"
            return self.kryptis
        if self.kryptis == "V":
            self.x += 1
            self.koord[0] = self.x
            self.kryptis = "R"
            return self.kryptis
        if self.kryptis == "R":
            self.x -= 1
            self.koord[0] = self.x
            self.kryptis = "V"
            return self.kryptis
        if self.kryptis == "P":
            self.y += 1
            self.koord[1] = self.y
            self.kryptis = "S"
            return self.kryptis

    def kairen(self):
        if self.kryptis == "S":
            self.y += 1
            self.koord[1] = self.y
            self.kryptis = "V"
            return self.kryptis
        if self.kryptis == "V":
            self.x -= 1
            self.koord[0] = self.x
            self.kryptis = "P"
            return self.kryptis
        if self.kryptis == "R":
            self.x += 1
            self.koord[0] = self.x
            self.kryptis = "S"
            return self.kryptis
        if self.kryptis == "P":
            self.y -= 1
            self.koord[1] = self.y
            self.kryptis = "R"
            return self.kryptis

    def desinen(self):
        if self.kryptis == "S":
            self.x += 1
            self.koord[0] = self.x
            self.kryptis = "R"
            return self.kryptis
        if self.kryptis == "V":
            self.y += 1
            self.koord[1] = self.y
            self.kryptis = "S"
            return self.kryptis
        if self.kryptis == "R":
            self.y -= 1
            self.koord[1] = self.y
            self.kryptis = "P"
            return self.kryptis
        if self.kryptis == "P":
            self.x -= 1
            self.koord[0] = self.x
            self.kryptis = "V"
            return self.kryptis

    def ar_mire(self):
        if self.taskai <= 0:
            return True
        else:
            return False

    def info(self, pusiu_suviai):
        print("Koordinates", self.koord)
        print("Kryptis", self.kryptis)
        print("Suviu skaicius", self.suviu_sk)
        print("Suviu skaicius i kiekviena puse", pusiu_suviai)

    def suvis(self):
        self.suviu_sk +=1

        return self.suviu_sk

    def ar_pataikei(self, taikinys):
        if self.kryptis == "V" and self.koord[0] > taikinys[0] and self.koord[1] == taikinys[1]:
            print("Pataikei")
            self.taskai += 100
            return self.taskai
        elif self.kryptis == "S" and self.koord[1] < taikinys[1] and self.koord[0] == taikinys[0]:
            print("Pataikei")
            self.taskai += 100
            return self.taskai
        elif self.kryptis == "R" and self.koord[0] < taikinys[0] and self.koord[1] == taikinys[1]:
            print("Pataikei")
            self.taskai += 100
            return self.taskai
        elif self.kryptis == "P" and self.koord[1] > taikinys[1] and self.koord[0] == taikinys[0]:
            print("Pataikei")
            self.taskai += 100
            return self.taskai
        else:
            return False