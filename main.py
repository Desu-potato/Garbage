import logic.worldobjects as wo

def initial():
    zawarudo = wo.world()

    list = [
                    [
                        "Chata Popielnika",
                        {"drewno": 8},
                        {"potaż": 2},
                        {"drewno": 1},
                        {"chłop": 50},
                        1.0
                    ],
                    [
                        "Mielerz",
                        {"drewno": 6},
                        {"węgiel": 2},
                        {"drewno": 1},
                        {"chłop": 50},
                        1.0
                    ],
                    [
                        "Uprawa Warzyw",
                        {"empty": 0},
                        {"warzywa": 6},
                        {"drewno": 1},
                        {"chłop": 200},
                        1.0
                    ],
                    [
                        "Chata Drewala",
                        {"empty": 0},
                        {"drewno": 4},
                        {"drewno": 1},
                        {"chłop": 10},
                        1.0
                    ],
                    [
                        "Uprawa Zboża",
                        {"empty": 0},
                        {"zboże": 8},
                        {"drewno": 1},
                        {"chłop": 200},
                        1.0
                    ],
                    [
                        "Przetwarzanie Zboża",
                        {"zboże": 1},
                        {"pasza": 2},
                        {"drewno": 1},
                        {"chłop": 10},
                        1.0
                    ],
                    [
                        "hodowla bydła",
                        {"pasza": 1},
                        {"bydło": 2},
                        {"drewno": 1},
                        {"chłop": 20},
                        1.0
                    ],
                    [
                        "Rzeźnik",
                        {"bydło": 1},
                        {
                            "mięso": 5000,
                            "surowe_skóry": 10,
                         },
                        {"drewno": 1},
                        {"chłop": 100},
                        1.0
                    ],
                    [
                        "Uprawa Lnu",
                        {"empty": 0},
                        {"len": 8},
                        {"drewno": 1},
                        {"chłop": 200},
                        1.0
                    ],
                    [
                        "Port Rybacki",
                        {"empty": 0},
                        {"łodzie": 0}, #limity dodać
                        {"drewno": 1},
                        {"chłop": 150},
                        1.0
                    ],
                    [
                        "Wytwórca Taniny",
                        {"empty": 0},
                        {"tanina": 4},
                        {"drewno": 1},
                        {"chłop": 50},
                        1.0
                    ],
                    [
                        "Garbarnia",
                        {
                            "tanina": 1,
                            "potaż": 1,
                            "tłuszcz":2,
                            "surowa_skóra":2
                         },
                        {"garbowana_skóra": 2},
                        {"drewno": 1},
                        {"chłop": 50},
                        1.0
                    ],
                    [
                        "Warsztat Narzędzi",
                        {
                            "żelazo": 1,
                            "drewno": 1,
                            "węgiel": 2,
                         },
                        {"narzędzia": 4},
                        {"drewno": 1},
                        {"rzemieślnik": 10},
                        1.0
                    ],
                    [
                        "Tkacz",
                        {"len": 5},
                        {"tkaniny": 5},
                        {"drewno": 1},
                        {"chłop": 20},
                        1.0
                    ]
    ]
    for record in list:
        zawarudo.addTobase(record)


    zawarudo.addImperium("Tymuridzi")
    zawarudo.addVillage("Tymuridzi", "Nowa Armacja")
    zawarudo.updateAllImperiusBase()

    map = {
        "drewno": [300, 3, 1],
        "potaż": [300, 2, 1],
        "węgiel": [300, 1, 1]
    }
    zawarudo.passRule("d", map, "Tymuridzi")
    map = {
        "Chata Drewala": 0,
        "Chata Popielnika": 1,
        "Uprawa Warzyw": 1,
        "Uprawa Zboża": 1,
        "hodowla bydła": 1,
        "Rzeźnik": 1,
        "Przetwarzanie Zboża": 1,
    }

    zawarudo.passRule("p", map, "Tymuridzi")
    map = {
        "zboże": [10, 2, 1],
        "warzywa": [10, 1, 1],
        "mięso": [10, 3, 1],
        "owoce": [10, 1, 1],
        "nabiał": [10, 1, 1],
    }
    zawarudo.passRule("f", map, "Tymuridzi")
    map = {
        "opał": [100, 2, 1],
        "proste_ubrania": [100, 1, 1],
        "domy": [100, 4, 100],
        "narzędzia" : [100, 1, 1],
        "smoła": [100, 1, 1],
        "alkohol": [100, 1, 1],
    }
    zawarudo.passRule("b", map, "Tymuridzi")
    zawarudo.updateAllImperiusRule()

    listMaterial = [
        "złote_monety",
        "empty",
        "pasza",
        "bydło",
        "mięso",
        "owoce",
        "nabiał",
        "zboże",
        "warzywa",
        "alkohol",
        "narzędzia",
        "domy",
        "opał",
        "zboże",
        "warzywa",
        "drewno",
        "garbowana_skóra",
        "len",
        "łodzie",
        "narzędzia",
        "potaż",
        "proste_ubrania",
        "surowa_skóra",
        "smoła",
        "tanina",
        "tkaniny",
        "tłuszcz",
        "węgiel",
        "żelazo",
        "proce",
        "złote_monety"
    ]

    zawarudo.typeStockAddEtycs("Tymuridzi", listMaterial)
    zawarudo.updateVillagesWithImperioStorage()
    zawarudo.parsePopbulk("Tymuridzi", "Nowa Armacja",
        {
            "Wojownicy": 0,
            "chłop": 3000,
            "rzemieślnik": 100
        }
    )

    zawarudo.addRecord("Tymuridzi", "Nowa Armacja", "Chata Drewala", 2)
    zawarudo.addRecord("Tymuridzi", "Nowa Armacja", "Chata Popielnika", 2)
    zawarudo.addRecord("Tymuridzi", "Nowa Armacja", "Uprawa Warzyw", 1)
    zawarudo.addRecord("Tymuridzi", "Nowa Armacja", "Uprawa Zboża", 1)
    zawarudo.addRecord("Tymuridzi", "Nowa Armacja", "hodowla bydła", 1)
    zawarudo.addRecord("Tymuridzi", "Nowa Armacja", "Rzeźnik", 1)
    zawarudo.addRecord("Tymuridzi", "Nowa Armacja", "Przetwarzanie Zboża", 1)
    listMaterial = {
        "mięso": 400,
        "bydło" : 400,
        "pasza" : 400,
        "owoce": 400,
        "nabiał": 400,
        "zboże": 400,
        "warzywa": 400,
        "alkohol": 400,
        "narzędzia": 400,
        "domy": 400,
        "opał": 400,
        "drewno": 400,
        "garbowana_skóra": 400,
        "len": 400,
        "łodzie": 400,
        "potaż": 400,
        "proste_ubrania": 400,
        "surowe_skóry": 400,
        "smoła": 400,
        "tanina": 400,
        "tkaniny": 400,
        "tłuszcz": 400,
        "węgiel": 400,
        "żelazo": 400,
        "proce": 400,
        "złote_monety": 400,
    }

    zawarudo.appandResourceBulk("Tymuridzi", "Nowa Armacja", listMaterial)
    #

   #parse informacji o ilości i przygotowanie produkcji.
   #może lepszy interface
    # zawarudo.globalTurn()

    for record in range(10):
        # zawarudo.calculateFillings("Tymuridzi", "Nowa Armacja")

        print("\n")
        print("turn :",zawarudo.turn)
        print("#---------------------#")
        for record in zawarudo.imperius:
            print("Imp Name:",zawarudo.imperius[record].name)
            print("Rule:",zawarudo.imperius[record].rule)
            print("Base:",zawarudo.imperius[record].base)
            print("Store: ", zawarudo.imperius[record].store.stock)
            print("#---------------------#")
            for key in zawarudo.imperius[record].economies:
                print("Village Name:",zawarudo.imperius[record].economies[key].name)
                print("Growrate:", zawarudo.imperius[record].economies[key].grow+0.5)
                print("Happines:", zawarudo.imperius[record].economies[key].mood+0.5)
                print("Health:", zawarudo.imperius[record].economies[key].health+0.5)
                print("Store: ",zawarudo.imperius[record].economies[key].store.stock)
                print("Money: ", zawarudo.imperius[record].economies[key].costMoney)
                print("Money Sum: ", zawarudo.imperius[record].economies[key].costSum)
                print("Pop:",zawarudo.imperius[record].economies[key].pop)
                print("Rynek wewnętrzny:", zawarudo.imperius[record].economies[key].gain)
                print("#---------------------#")

        zawarudo.globalTurn()

if __name__ == '__main__':
    initial()





