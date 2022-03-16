import logic.worldobjects as wo

def initial():
    zawarudo = wo.world()

    list = [
                    "Chata Drwali",
                   {"empty" : 0},
                   {"drewno": 5},
                   {"drewno": 1},
                   {"chłop": 50},
                   1.0
    ]

    zawarudo.addTobase(list)
    zawarudo.addImperium("Tymuridzi")
    zawarudo.addVillage("Tymuridzi", "Nowa Armacja")
    zawarudo.updateAllImperiusBase()

    map = {
        "drewno": [200, 1],
        "pszenica": [1, 1],
        #    "len" : [100, 1],
        "potaż": [100, 1],
        "proste_ubrania_len": [100, 1],
        "węgiel": [100, 1]
    }
    zawarudo.passRule("d", map, "Tymuridzi")
    map = {
        "Chata Drwali": 0,
        "Chata Popielnika": 1,
        "Mielerz": 0,
        "Uprawa Warzyw": 0,
        "Uprawa Zboża": 0,
        "Port Rybacki": 0,
        "Wytwórca Taniny": 0,
        "Garbarnia": 0,
        "Warsztat Narzędzi": 0,
        "Tkacz": 0
    }
    zawarudo.passRule("p", map, "Tymuridzi")
    map = {
        "zboże": [1, 50],
        "warzywa": [1, 50],
    }
    zawarudo.passRule("f", map, "Tymuridzi")
    zawarudo.updateAllImperiusRule()

    for record in zawarudo.imperius:
        print("Imp Name:",zawarudo.imperius[record].name)
        print("Rule:",zawarudo.imperius[record].rule)
        print("Base:",zawarudo.imperius[record].base)
        print("#---------------------#")
        for key in zawarudo.imperius[record].economies:
            print("Village Name:",zawarudo.imperius[record].economies[key].name)
            print("Store: ",zawarudo.imperius[record].economies[key].store.stock)
            print("Pop:",zawarudo.imperius[record].economies[key].pop)
            print("#---------------------#")



if __name__ == '__main__':
    initial()





