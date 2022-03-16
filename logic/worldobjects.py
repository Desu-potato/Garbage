import logic.structs as s


class world:
    def __init__(self):
        self.imperius = {}
        self.base = s.base()

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
            self.imperius[record].updateDB(self.base)
            for key in self.imperius[record].economies:
                self.imperius[record].economies[key].updateBase(self.base)

    def passRule(self, ruletype, rule, imperio):
        self.imperius[imperio].passRule(ruletype, rule)

    def updateAllImperiusRule(self):
        for record in self.imperius:
            self.imperius[record].updateRule()
