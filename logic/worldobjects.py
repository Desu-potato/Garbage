import logic.structs as s


class world:
    def __init__(self):
        self.imperius = {}
        self.base = s.base()

    def typeStockone(self, imperio, nameVillage, stock):
        self.imperius[imperio].economies[nameVillage].changeStorage(stock)

    def typeStockAddEtycs(self, imperio, ethics):
        self.imperius[imperio].appandResourceEmptyBulk(ethics)

    def updateVillagesWithImperioStorage(self):
        for record in self.imperius:
            self.imperius[record].updateVillagesWithImperioStorage()

    def addImperium(self, name):
        self.imperius[name] = s.imp()
        self.imperius[name].updateName(name)

    def editImperiumName(self, name):
        self.imperius[name].editNameImperio(name)

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
        self.imperius[imperio].economies[village].calculateTurn()