import dill
import logic.worldobjects as wo

def save(obj):
    dill.dump(obj, open("savefile/save.pickle", "wb+"))


def load():
    file = dill.load(open("savefile/save.pickle", "rb"))
    return file


class interface:

    def buildCreator(self):

        class templateBuild:
            def __init__(self):
                self.name = ""
                self.input = {}
                self.output = {}
                self.cost = {}
                self.workForce = {}
                self.effect = 1.0

            def showme(self):
                print(
                    self.name, "\n",
                    self.input,"\n",
                    self.output,"\n",
                    self.cost, "\n",
                    self.workForce, "\n",
                    self.effect, "\n",
                )

        temp = templateBuild()
        while True:

            print(temp.showme())
            print(
                "nazwa: 1\n",
                "setInput: 2\n",
                "delInput: 3\n",
                "setOutput: 4\n",
                "delOutput: 5\n",
                "setCost: 6\n",
                "delCost: 7\n",
                "setWorkForce: 8\n",
                "delWorkForce: 9\n",
                "exit: 10\n",
                "Push to the base: 11\n",
            )

            inp = int(input())
            if inp == 1:
                inp = input(">>")
                temp.name = inp

            if inp == 2:
                res = input("res>>")
                much = input(">>")
                temp.input[res] = much

            if inp == 3:
                res = input("res>>")
                temp.input[res].pop()

            if inp == 4:
                res = input("res>>")
                much = input(">>")
                temp.output[res] = much

            if inp == 5:
                res = input("res>>")
                temp.output[res].pop()

            if inp == 6:
                res = input("res>>")
                much = input(">>")
                temp.cost[res] = much

            if inp == 7:
                res = input("res>>")
                temp.cost[res].pop()

            if inp == 8:
                res = input("res>>")
                much = input(">>")
                temp.workForce[res] = much

            if inp == 9:
                res = input("res>>")
                temp.workForce[res].pop()

            if inp == 11:
                record = [temp.name, temp.input, temp.output, temp.cost, temp.workForce]
                self.world.addTobase(record)
                self.world.updateAllImperiusBase()

            if inp == 10:
                break

    def updateBiznesRule(self, imperio, name, build, bool):
        self.world.updateBiznesLogic(imperio, name, build, bool)

    def returnBiznes(self, imperio, name, option):
        return self.world.returnBiznes(imperio, name, option)

    def addResourceToVillage(self, imperio, name, resource, much):
        self.world.addResourceToVillage(imperio, name, resource, much)

    def saveWorld(self):
        save(self.world)

    def loadWorld(self):
        self.world = load()

    def createVillage(self, imperio, name):
        self.world.addVillage(imperio, name)

    def addrecord(self, imperio, name, build, much):
        self.world.addRecord(imperio, name, build, much)

    def addEtic(self, imperio, resource):
        self.world.imperius[imperio].typeStockAddEtycsOne(resource)



    def initialProtokol(self):
        self.world = wo.world()
        self.ledger = {}
        self.log = {}

    def fullMyLedger(self):
        self.ledger = { "Imperia" : list(self.world.imperius.keys())}


    def setImperio(self,name):
        self.world.addImperium(name)
        self.fullMyLedger()

    def changeNameImperio(self,name, newname):
        self.world.editImperiumName(name, newname)
        bufor = self.world.imperius[name]
        self.deleteNameImperio(name)
        self.world.imperius[newname] = bufor
        self.fullMyLedger()

    def globalTurn(self):
        self.world.globalTurn()

    def deleteNameImperio(self, name):
        self.world.imperius.pop(name)
        self.fullMyLedger()

    def setVillagePopulation(self, name, village, cast, much):
        self.world.imperius[name].economies[village].popModify(cast, much)
        print(self.world.imperius[name].economies[village].pop)

    def showMyShit(self, imperius, name):
        self.world.showMyVillage(imperius, name)

    def showRule(self, imperio):
        self.world.showRule(imperio)

    def addRule(self, imperio, ruleType, ruleName, ruleBody):
        self.world.addRule(imperio, ruleType, ruleName, ruleBody)

    def passRule(self, ruletype, rule, imperio):
        self.world.passRule(ruletype, rule, imperio)

    def passResource(self, imperio, village, resource, much):
        self.word.addResourceToVillage(imperio, village, resource, much)

    def fillBaseProtocol(self):
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
                {"łodzie": 0},  # limity dodać
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
                    "tłuszcz": 2,
                    "surowa_skóra": 2
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
            self.world.addTobase(record)
        self.world.updateAllImperiusBase()

    def fillRuleProtocol(self, imperio):
        map = {
            "drewno": [100, 3, 1],
            "potaż": [100, 2, 1],
            "węgiel": [100, 1, 1]
        }
        self.world.passRule("d", map, imperio)
        map = {
            "Chata Drewala": 0,
        }

        self.world.passRule("p", map, imperio)
        map = {
            "zboże": [10, 2, 1],
            "warzywa": [10, 1, 1],
            "mięso": [10, 3, 1],
            "owoce": [10, 1, 1],
            "nabiał": [10, 1, 1],
        }
        self.world.passRule("f", map, imperio)
        map = {
            "opał": [100, 2, 1],
            "proste_ubrania": [100, 1, 1],
            "domy": [100, 4, 100],
            "narzędzia": [100, 1, 1],
            "smoła": [100, 1, 1],
            "alkohol": [100, 1, 1],
        }
        self.world.passRule("b", map, imperio)
        self.world.updateAllImperiusRule()

    def fillEthicsProtocol(self, imperio):
        listMaterial = [
            "materiały_konstrukcyjne",
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

        self.world.typeStockAddEtycs(imperio, listMaterial)
        self.world.updateVillagesWithImperioStorage()

    def initialProtokol_Example(self):
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
                {"łodzie": 0},  # limity dodać
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
                    "tłuszcz": 2,
                    "surowa_skóra": 2
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
            "drewno": [100, 3, 1],
            "potaż": [100, 2, 1],
            "węgiel": [100, 1, 1]
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
            "narzędzia": [100, 1, 1],
            "smoła": [100, 1, 1],
            "alkohol": [100, 1, 1],
        }
        zawarudo.passRule("b", map, "Tymuridzi")
        zawarudo.updateAllImperiusRule()

        listMaterial = [
            "materiały_konstrukcyjne",
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
            "materiały_konstrukcyjne": 400,
            "mięso": 400,
            "bydło": 400,
            "pasza": 400,
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

        # parse informacji o ilości i przygotowanie produkcji.
        # może lepszy interface
        # zawarudo.globalTurn()

        for record in range(10):
            # zawarudo.calculateFillings("Tymuridzi", "Nowa Armacja")
            if record == 3:
                map = {
                    "materiały_konstrukcyjne": [100, 7, 1],
                    "drewno": [100, 1, 1],
                    "potaż": [100, 2, 1],
                    "węgiel": [100, 1, 1]
                }
                zawarudo.passRule("d", map, "Tymuridzi")
                zawarudo.updateAllImperiusRule()

            print("\n")
            print("turn :", zawarudo.turn)
            print("#---------------------#")
            for record in zawarudo.imperius:
                print("Imp Name:", zawarudo.imperius[record].name)
                print("Rule:", zawarudo.imperius[record].rule)
                print("Base:", zawarudo.imperius[record].base)
                print("Store: ", zawarudo.imperius[record].store.stock)
                print("#---------------------#")
                for key in zawarudo.imperius[record].economies:
                    print("Village Name:", zawarudo.imperius[record].economies[key].name)
                    print("Growrate:", zawarudo.imperius[record].economies[key].grow + 0.5)
                    print("Happines:", zawarudo.imperius[record].economies[key].mood + 0.5)
                    print("Health:", zawarudo.imperius[record].economies[key].health + 0.5)
                    print("Store: ", zawarudo.imperius[record].economies[key].store.stock)
                    print("Money: ", zawarudo.imperius[record].economies[key].costMoney)
                    print("Money Sum: ", zawarudo.imperius[record].economies[key].costSum)
                    print("Pop:", zawarudo.imperius[record].economies[key].pop)
                    print("Rynek wewnętrzny:", zawarudo.imperius[record].economies[key].gain)
                    print("#---------------------#")
                    print("log:", zawarudo.imperius[record].economies[key].log)
            zawarudo.globalTurn()

    def fillMeWithStaffProtocol(self, imperio, village):
        listMaterial = {
            "materiały_konstrukcyjne" : 400,
            "empty" : 0,
            "pasza" : 400,
            "bydło" : 400,
            "mięso" : 400,
            "owoce" : 400,
            "nabiał" : 400,
            "alkohol" : 400,
            "domy" : 400,
            "opał" : 400,
            "zboże" : 400,
            "warzywa" : 400,
            "drewno" : 400,
            "garbowana_skóra" : 400,
            "len" : 400,
            "łodzie" : 400,
            "narzędzia" : 400,
            "potaż" : 400,
            "proste_ubrania" : 400,
            "surowa_skóra" : 400,
            "smoła" : 400,
            "tanina" : 400,
            "tkaniny" : 400,
            "tłuszcz" : 400,
            "węgiel" : 400,
            "żelazo" : 400,
            "proce" : 400,
            "złote_monety" : 400
        }
        for record in listMaterial:
             b = listMaterial[record]
             self.addResourceToVillage(imperio, village, record, b)

    def initialNewProtokol(self):
        imperio = "Słowanie"
        village = "Jaromar"
        self.setImperio(imperio)
        self.createVillage(imperio, village)
        self.fillBaseProtocol()
        self.addrecord(imperio, village, "Chata Drewala", 2)
        self.fillRuleProtocol(imperio)
        self.fillEthicsProtocol(imperio)
        self.world.updateVillagesWithImperioStorage()
        self.addrecord(imperio, village, "Chata Popielnika", 2)
        self.updateBiznesRule(imperio, village, "Chata Popielnika", True)
        self.addRule(imperio, "p", "Chata Popielnika", 0)
        self.setVillagePopulation(imperio, village, "chłop", int(4000))
        self.world.updateAllImperiusRule()
        map = self.returnBiznes(imperio, village, "")
        self.fillMeWithStaffProtocol(imperio, village)

