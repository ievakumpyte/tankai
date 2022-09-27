import random
from sqlalchemy.orm import sessionmaker
from modules.duombaze import Highscores, engine
from modules.tankas import Tankas
Session = sessionmaker(bind=engine)
session = Session()

def gen_taikini():
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    taikinio_koord = [x,y]
    return  taikinio_koord

tankas1 = Tankas(krypties_sk=0,kryptis="S", suviu_sk=0)
taikiniu_numusta = []
krypties_sk = {"P":0,"S":0,"V":0, "R": 0}

def zaidimas(krypties_sk):
    taikinys = [2, 0]
    v = 0
    p = 0
    r = 0
    s = 0
    while True:
        try:
            ivestis = input(
                "Iveskit krypti: 'A'-kairen, 'S'-atgal, 'W'-pirmyn, 'D'-desinen. Sauti-'M'. Mygtukas 'Enter'-baigt. 'H'-high scores: \n")
        except ValueError:
            print("Netinkama reiksme")
        except TypeError:
            print("Netinkama reiksme")

        if ivestis == "a":
            print('You Pressed left!')
            tankas1.kairen()
            print(tankas1.koord)
            print("Kryptis", tankas1.kryptis)
            tankas1.taskai -= 10
            tankas1.ar_mire()
            print(tankas1.taskai)

        elif ivestis == "w":
            print('You Pressed up!')
            tankas1.pirmyn()
            print(tankas1.koord)
            print("Kryptis", tankas1.kryptis)
            tankas1.taskai -= 10
            print(tankas1.taskai)
            tankas1.ar_mire()

        elif ivestis == "d":
            print('You Pressed right!')
            tankas1.desinen()
            print(tankas1.koord)
            print("Kryptis", tankas1.kryptis)
            tankas1.taskai -= 10
            print(tankas1.taskai)
            tankas1.ar_mire()

        elif ivestis == "s":
            print('You Pressed down!')
            tankas1.atgal()
            print(tankas1.koord)
            print("Kryptis", tankas1.kryptis)
            tankas1.taskai -= 10
            print(tankas1.taskai)
            tankas1.ar_mire()
            
        elif ivestis == "m":
            print('You shot!')
            tankas1.suvis()
            tankas1.ar_pataikei(taikinys)
            if tankas1.kryptis == "P":
                p+=1
                krypties_sk["P"] = p
            if tankas1.kryptis == "S":
                s+=1
                krypties_sk["S"] = s
            if tankas1.kryptis == "R":
                r+=1
                krypties_sk["R"] = r
            if tankas1.kryptis == "V":
                v+=1
                krypties_sk["V"] = v
            print(krypties_sk)
            print(tankas1.suviu_sk)
            if tankas1.ar_pataikei(taikinys) == False:
                pass
            else:

                del taikinys
                taikiniu_numusta.append("|")
                taikinys = gen_taikini()
                print("Kitas taikinys", taikinys)
            tankas1.taskai -= 10
            print(tankas1.taskai)
            tankas1.ar_mire()
        elif ivestis == "h":
            pass
            highscores = session.query(Highscores).order_by(Highscores.taskai.desc()).limit(10).all()
            for highscore in enumerate(highscores,start=1):
                print(highscore)
        elif ivestis == "":
            break
        else:
            print("Nera tokios krypties. Veskite is naujo")

        if tankas1.ar_mire() == True:
            print("Game over")
            vardas = input("Iveskite savo varda:\n")
            pavarde = input("Iveskite savo pavarde:\n")
            irasas = Highscores(vardas,pavarde,len(taikiniu_numusta))
            session.add(irasas)
            session.commit()
            highscores2 = session.query(Highscores).all()
            break

zaidimas(krypties_sk)
while True:
    try:
        ar_dar = int(input("Zaisti dar karta? 1-Taip. 2-Ne"))
    except ValueError:
        print("Netinkama reiksme")
    except TypeError:
        print("Netinkama reiksme")

    if ar_dar == 1:
        tankas1.taskai = 100
        tankas1.kryptis = "S"
        tankas1.koord = [0,0]
        tankas1.x = 0
        tankas1.y = 0
        krypties_sk = {"P": 0, "S": 0, "V": 0, "R": 0}
        zaidimas(krypties_sk)
    if ar_dar == 2:
        print("Taikiniu numusta",len(taikiniu_numusta))
        tankas1.info(krypties_sk)
        break