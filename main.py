import logic.worldobjects as wo
import menu.menu as menu
def initial():
    pass

def initialInterface():
    interface = menu.interface()
    interface.initialProtokol()

    while True:
        inp = -1
        print(
            "Zaimplementowane warunki:\n",

            "Utworzenie imperium: 1\n",
            "Usunięcie imperium: 2\n",
            "Pokaż istniejące imperia: 3\n",
            "Zmiana nazwy imperium: 4\n",
            "Dodawnie wioski: 5\n",
            "Dodawnie Zasad: 6\n",
            "Turowe podsumowanie: 7\n",
            "Protokół inicjacji bazy: 8\n",
            "Dodaj populacje do wioski 10\n",
            "Dodanie budynku do wioski 11\n",
            "Zapis: 12\n",
            "Wczytaj: 13\n",
            "Dodaj zasób: 14\n",
            "Kreator zasad: 15\n",
            "Protokół zasad dla danego imperium: 16\n",
            "Globalna tura: 17\n",
            "Uzupełnił Etykietki Magazynu Protokól: 18\n",
            "Pełne tworzenie: 19\n",
            "Creator: 22\n",
            "Wyjście: 9\n",
        )
        # try:
        if True:
            inp = int(input())

            if inp == 1:
                inp = input(">>")
                interface.setImperio(inp)


            if inp == 2:
                inp = input(">>")
                interface.deleteNameImperio(inp)

            if inp == 3:
                interface.fullMyLedger()
                print(interface.ledger)

            if inp == 4:
                inp = input("From >>")
                inp2 = input("To >>")
                interface.changeNameImperio(inp, inp2)

            if inp == 5:
                inp = input("Imperio >>")
                Name = input("Name >>")
                interface.createVillage(inp, Name)

            if inp == 7:
                inp = input("Imperio >>")
                Name = input("Name >>")
                interface.showMyShit(inp, Name)
                # print(interface.world.imperius[inp].economies[Name].production.listOfBuildings)

            if inp == 8:
                interface.fillBaseProtocol()

            if inp == 10:
                inp = input("Imperio >>")
                Name = input("Name >>")
                cast = input("Cast >>")
                much = input("Much >>")
                interface.setVillagePopulation(inp, Name, cast, int(much))

            if inp == 11:
                inp = input("Imperio >>")
                Name = input("Name >>")
                print(interface.world.base.allBuild)
                b = input("Build >>")
                m = input("Much >>")
                interface.addrecord(inp, Name, b, int(m))

            if inp == 12:
                interface.saveWorld()
            if inp == 13:
                interface.loadWorld()

            if inp == 14:
                b = input("Imperio >>")
                m = input("Resource >>")
                interface.addEtic(b, m)

            if inp == 15:
                inp = input("Imperio>>")
                type = input("Type>>")
                etic = input("Etic>>")
                b1 = input("Optionnr1>>")
                b2 = input("Optionnr2>>")
                b3 = input("Optionnr3>>")
                bufer = []
                if b1 != "":
                    bufer.append(int(b1))
                if b2 != "":
                    bufer.append(int(b2))
                if b3 != "":
                    bufer.append(int(b3))
                interface.addRule(inp, type, etic, bufer)
                interface.showRule(inp)

            if inp == 16:
                inp = input("Imperio>>")
                interface.fillRuleProtocol(inp)

            if inp == 17:
                interface.globalTurn()

            if inp == 18:
                inp = input("Imperio>>")
                interface.fillEthicsProtocol(inp)

            if inp == 19:
                #debug protocole
                interface.initialNewProtokol()

            if inp == 20:
                #updateBizneslogic
                inp = input("Imperio>>")
                type = input("Village>>")
                etic = input("Build>>")
                b1 = input("Optionnr1>>")
                b2 = input("Optionnr2>>")
                bufer = []
                if b1 != "":
                    bufer.append(bool(int(b1)))
                if bufer[0] != False:
                    bufer.append(int(b2))
                interface.updateBiznesRule(inp, type, etic, bufer)

            if inp == 21:
                inp = input("Imperio>>")
                type = input("Village>>")
                option = input("Village>>")
                interface.returnBiznes(inp, type, option)

            if inp == 22:
                interface.buildCreator()

            if inp == 9:
                break

        # except:
        #     continue

if __name__ == '__main__':
    initialInterface()
    # b = menu.interface()
    # b.initialProtokol_Example()





