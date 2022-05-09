import logic.structs as s


class world:
    def __init__(self):
        self.turn = 0
        self.imperius = {}
        self.base = s.base()

    def returnBiznes(self, imperio, name, option):
        return self.imperius[imperio].economies[name].returnBiznes(option)


    def updateBiznesLogic(self, imperio, name, build, bool):
            self.imperius[imperio].economies[name].updatePrivateBiznes(build, bool)

    def typeStockone(self, imperio, nameVillage, stock):
        self.imperius[imperio].economies[nameVillage].changeStorage(stock)

    def typeStockAddEtycsOne(self, imperio, ethics):
        self.imperius[imperio].appandResourceEmpty(ethics)
        self.imperius[imperio].updateVillagesWithImperioStorage()

    def typeStockAddEtycs(self, imperio, ethics):
        self.imperius[imperio].appandResourceEmptyBulk(ethics)

    def addResourceToVillage(self, imperio, village, resource, much):
        self.imperius[imperio].economies[village].store.appandResource(resource, much)


    def updateVillagesWithImperioStorage(self):
        for record in self.imperius:
            self.imperius[record].updateVillagesWithImperioStorage()

    def showMyVillage(self, imperio, name):
        base = self.imperius[imperio].economies[name]
        print("Village Name:", base.name)
        print("Growrate:", base.grow + 0.5)
        print("Happines:", base.mood + 0.5)
        print("Health:", base.health + 0.5)
        print("Store: ", base.store.stock)
        print("Money: ", base.costMoney)
        print("Money Sum: ", base.costSum)
        print("Pop:", base.pop)
        print("Rynek wewnętrzny:", base.gain)
        print("#---------------------#")
        print("log:", base.log)
        print("test: ", base.production.listOfBuildings)








    def addImperium(self, name):
        self.imperius[name] = s.imp()
        self.imperius[name].updateName(name)

    def editImperiumName(self, name, newname):
        self.imperius[name].editNameImperio(newname)

    def addVillage(self, imperio, nameVillage):
        self.imperius[imperio].addVillage(nameVillage)

    def addTobase(self, record):
        file = s.build()
        file.createBuild(record[0], record[1], record[2], record[3], record[4], record[5])
        self.base.add(file)

    def updateAllImperiusBase(self):
        for record in self.imperius:
            base = self.base
            self.imperius[record].updateDB(base)
            for key in self.imperius[record].economies:
                self.imperius[record].economies[key].updateBase(base)

    def showRule(self, imperio):
        print(
            self.imperius[imperio].rule.demandRule,
            self.imperius[imperio].rule.prioRule,
            self.imperius[imperio].rule.foodRule,
            self.imperius[imperio].rule.basicRule
        )

    def addRule(self, imperio, ruleType, ruleName, ruleBody):
        print(imperio, ruleType, ruleName, ruleBody)
        self.imperius[imperio].addRule(ruleType, ruleName, ruleBody)

    def passRule(self, ruletype, rule, imperio):
        self.imperius[imperio].passRule(ruletype, rule)

    def updateAllImperiusRule(self):
        for record in self.imperius:
            self.imperius[record].updateRule()

    def parsePopSpec(self, imperio, village, caste, number):
        self.imperius[imperio].economies[village].pop[caste] = 0
        self.imperius[imperio].economies[village].pop[caste] = number

    def parsePopbulk(self, imperio, village, map):
        self.imperius[imperio].economies[village].pop = map


    def addRecord(self, imperio, village, name, much):
        self.imperius[imperio].economies[village].addRecord(name, much)


    def calculateTurn(self, imperio, village):
        self.imperius[imperio].economies[village].calculateTurn(self.turn)

    def globalTurn(self):
        t = self.turn
        t = t+1
        self.turn = t
        for record in self.imperius:
            self.imperius[record].updateTure(t)
            for key in self.imperius[record].economies:
                self.imperius[record].economies[key].calculateTurn(self.turn)


    def calculateFillings(self, record, key):
        self.imperius[record].calculateGoods(key)

    def appandResource(self, imperio, village, name, much):
        self.imperius[imperio].economies[village].store.appandResource(name, much)

    def appandResourceBulk(self, imperio, village, map):
        for record in map:
            self.imperius[imperio].economies[village].store.appandResource(record, map[record])
