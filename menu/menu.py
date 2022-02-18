from tkinter import *
import dill, json

#helpers func
def returnDictInfo(dict, int, *option):
    buf = []
    for key in dict:
        buf.append(key)
    if option == "all" and option != "":
        return buf
    return buf[int]

def save(obj):
    dill.dump(obj, open("save.pickle", "wb+"))

def load():
    file = dill.load(open("save.pickle", "rb"))
    return file

def show(data):
    data = json.loads(data)
    print(json.dumps(data, indent=4, sort_keys=True))


#global staff
class imp:
    def __init__(self):
        self.name = ""
        self.pop = ""
        self.finans = ""
        self.villages = {}

class base:
    def __init__(self):
        self.peasantBuild = {}
        self.craftsmanBuild = {}
        self.advanceBuild = {}
        self.allBuild = {}
    # def load(self):
    #     base_load = load()
    #     for build_load in base_load:
    #         if returnDictInfo(build_load.popNeeded, 0) == "chłop":
    #             self.peasantBuild.append({ buildbuild_load})
    #         if returnDictInfo(build_load.popNeeded, 0) == "rzemieślnik":
    #             self.craftsmanBuild.append(build_load)
    #         if "chłopi" and "rzemieślnik" in returnDictInfo(build_load.popNeeded, 0, "all"):
    #             self.advanceBuild.append(build_load)
    #         self.allBuild.append(build_load)

    def add(self, obj):
        if returnDictInfo(obj.popNeeded, 0) == "chłop":
            self.peasantBuild[obj.name] = obj
        if returnDictInfo(obj.popNeeded, 0) == "rzemieślnik":
            self.craftsmanBuild[obj.name] = obj
        if "chłopi" and "rzemieślnik" in returnDictInfo(obj.popNeeded, 0, "all"):
            self.advanceBuild[obj.name] = obj
        self.allBuild[obj.name] = obj

class build:
    def __init__(self):
        self.name = ""
        self.cost = {}
        self.popNeeded = {}
        self.input = {}
        self.output = {}
        self.effective = 0.0

    def createBuild(self, name, input, output, cost, popNeeded, effective):
        self.name = name
        self.effective = effective
        self.cost = cost
        self.popNeeded = popNeeded
        self.input = input
        self.output = output

#local staff
class demand:
    def __init__(self):
        self.mapDemand = {}
        self.popDemand = {}
        self.buildDemand = {}

    def calculatePopDemand(self, base, pop):
        pass


class village:

    def __init__(self, base):
        self.base = base
        self.store = storage()
        self.production = production()
        self.dem = demand()
        self.pop = {"Wojownicy": 0, "chłop": 1000, "rzemieślnik": 10}
        self.popMulti = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}
        self.popInWork = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}
        self.wage = {"Wojownicy": 0, "chłop": 0.1, "rzemieślnik": 1}
        self.costMoney = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}
        self.costSum = 0

    def updateStorage(self):
        self.store = self.production.store

    def summaryPopInWork(self):
        summPop = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}

        for record in self.production.listOfBuildings:
            buildInRecord = self.production.listOfBuildings[record]
            for supPopKey in buildInRecord["Supplied"]:
                notemploy = ( buildInRecord["Supplied"][supPopKey] - buildInRecord["Needed"][supPopKey])
                summPop[supPopKey] = summPop[supPopKey] + buildInRecord["Supplied"][supPopKey] - notemploy

        self.popInWork = summPop


    def updateDemand(self, resource, value):
        self.demand[resource] = value

    def addDemand(self, resource):
        self.demand[resource] = 0

    def changeDemand(self, variable):
        self.demand = variable

    def diagnosis(self):
        print(
            self.pop,
            self.popMulti,
            self.popInWork,
            self.wage,
            self.costMoney,
            self.costSum
        )

    def updateCostMoney(self):
        for record in self.production.cost:
            self.costMoney[record] = self.costMoney[record] + self.production.cost[record]

    def calculateCost(self):
        self.production.fillCosts(self.wage)
        self.updateCostMoney()


    def returnCost(self):
        for cast in self.costMoney:
            self.costSum = self.costSum + self.costMoney[cast]
    
    def summaryCost(self):
        for bulding in self.production.listOfBuildings:
            dict = self.production.listOfBuildings[bulding]["Cost"]
            for recordKey in dict:
                self.costMoney[recordKey] = self.costMoney[recordKey]+dict[recordKey]
    
    
    def suspectedFuture(self):
        self.popInFuture = {"Wojownicy": 0,
                            "Chłopi":   round(self.pop["Chłopi"] * (self.popMulti["Chłopi"])),
                            "Rzemieślnicy": round(self.pop["Rzemieślnicy"] * (self.popMulti["Rzemieślnicy"])),
                           }

    def popSummary(self):
        self.pop = {"Wojownicy" : self.popInFuture["Wojownicy"] + self.pop["Wojownicy"],
                    "Chłopi" : self.popInFuture["Chłopi"] + self.pop["Chłopi"],
                    "Rzemieślnicy" : self.popInFuture["Rzemieślnicy"] + self.pop["Rzemieślnicy"]
                    }

    def popModify(self, caste, value):
        self.pop[caste] = value

class storage:
            def __init__(self):
                self.stock = {}
                self.production = {}
                self.resourceFuture = {}

            def appandResource(self, resource, much):
                self.stock[resource] = much
            def appandResourceEmpty(self, resource):
                self.stock[resource] = 0
            def modifyResource(self, resource, much):
                self.stock[resource] = self.stock[resource]+much

class production:
    def __init__(self):
        self.base = db
        self.store = storage()
        self.listOfBuildings = {}
        self.productionFuture = {}
        self.cost = {}

    def costSummary(self):
        bufor = {}
        for building in self.listOfBuildings:
            buildInProd = self.listOfBuildings[building]
            for cost in buildInProd["Cost"]:
                bufor[cost] = 0
        for building in self.listOfBuildings:
            buildInProd = self.listOfBuildings[building]
            for cost in buildInProd["Cost"]:
                bufor[cost] = bufor[cost] + buildInProd["Cost"][cost]
        self.cost = bufor

    def fillCosts(self, costs):
        for building in self.listOfBuildings:
            costDict = costs
            status = self.listOfBuildings[building]
            buforCost = {}
            for recordKey in costDict:
                if recordKey in status["Supplied"] or recordKey in status["Needed"]:
                    buforCost[recordKey] = round(costDict[recordKey]*status["Supplied"][recordKey])
            status["Cost"] = buforCost
            self.listOfBuildings[building] = status

    def addRecord(self, name, much):
        try:
            build = db.allBuild[name]
            self.listOfBuildings[name] = {
                                          "Much": much,
                                          "Supplied": {"chłop" : 0, "rzemieślnik" : 0},
                                          "Needed": {"chłop" : 0, "rzemieślnik" : 0},
                                          "EffectPop" : 0,
                                          "EffectProd" : 0,
                                          "ProductionSupplied" : 0,
                                          "ProductionNeeded": 0,
                                          "Production" : 0,
                                          "Cost" : 0,
                                          "Raw" : build,
                                          "Effect" : 0}
        except:
            return "Brak w bazie"

    def editRecord(self, name, param, value):
        try:
            bufer = self.listOfBuildings[name]
            bufer[param] = value
            self.listOfBuildings[name] = bufer
        except:
            return "Brak w bazie"

    def returnRecord(self, name):
        try:
            build = self.listOfBuildings[name]
            return build

        except:
            return "Brak w bazie"

    def calculateProductionNeeds(self, name):
        build = self.base.allBuild[name]
        buildInProd = self.listOfBuildings[name]
        bufor = {}
        for recordkey in build.input:
            bufor[recordkey] = build.input[recordkey]*buildInProd["Much"]
        buildInProd["ProductionNeeded"] = bufor
        self.listOfBuildings[name] = buildInProd

    def calculateWorker(self, name):
        build = self.base.allBuild[name]
        buildInProd = self.listOfBuildings[name]
        bufor = {}
        for recordkey in build.popNeeded:
            bufor[recordkey] = build.popNeeded[recordkey] * buildInProd["Much"]
        buildInProd["Needed"] = bufor
        self.listOfBuildings[name] = buildInProd

    def calculateEffectPop(self, name):
        build = self.base.allBuild[name]
        buildInProd = self.listOfBuildings[name]
        bufer = {}
        for value in build.popNeeded:
            bufer[value] = 0
        for value in buildInProd["Supplied"]:
                bufer[value] = bufer[value] + buildInProd["Supplied"][value]
        for value in buildInProd["Needed"]:
            bufer[value] = bufer[value] / buildInProd["Needed"][value]
        mini = 1
        for value in bufer:
            if mini > bufer[value]:
                mini = round(bufer[value], 2)
            if mini > 1:
                mini = 1
        buildInProd["EffectPop"] = mini
        self.listOfBuildings[name] = buildInProd

    def calculateEffectProd(self, name):
        build = self.base.allBuild[name]
        buildInProd = self.listOfBuildings[name]
        bufer = {}
        for value in buildInProd["ProductionNeeded"]:
            bufer[value] = 0
        for value in buildInProd["ProductionSupplied"]:
                bufer[value] = bufer[value] + buildInProd["ProductionSupplied"][value]
        for value in buildInProd["ProductionNeeded"]:
            bufer[value] = bufer[value] / buildInProd["ProductionNeeded"][value]
        mini = 1
        for value in bufer:
            if mini > bufer[value]:
                mini = round(bufer[value], 2)
            if mini > 1:
                mini = 1
        buildInProd["EffectProd"] = mini
        self.listOfBuildings[name] = buildInProd

    def calculateEffect(self, name):
        buildInProd = self.listOfBuildings[name]

        mini = 1
        for value in [buildInProd["EffectPop"], buildInProd["EffectProd"]]:
            if mini > value:
                mini = value
        buildInProd["Effect"] = mini
        self.listOfBuildings[name] = buildInProd

    def calculateProduction(self, name):
        build = self.base.allBuild[name]
        buildInProd = self.listOfBuildings[name]
        bufer = {}
        for record in build.output:
            bufer[record] = round(build.output[record]*buildInProd["Much"]*buildInProd["Effect"],3)
        buildInProd["Production"] = bufer
        self.listOfBuildings[name] = buildInProd

    def autoFill(self, cost):
        for record in self.listOfBuildings:
            self.calculateProductionNeeds(record)
            self.calculateWorker(record)
            self.calculateEffectPop(record)
            self.calculateEffectProd(record)
            self.calculateEffect(record)
            self.calculateProduction(record)
        self.fillCosts(cost)

    def calculateStorage(self):
        bufer = {}
        for record in self.listOfBuildings:
            buildInProd = self.listOfBuildings[record]
            for prodKey in buildInProd["Production"]:
                bufer[prodKey] = 0

        for record in self.listOfBuildings:
            buildInProd = self.listOfBuildings[record]

            for prodKey in buildInProd["Production"]:
                bufer[prodKey] = bufer[prodKey] + buildInProd["Production"][prodKey]

        for record in bufer:
            self.prodToStore(record, bufer[record])

    def prodToStore(self, resName, value):
        self.store.modifyResource(resName, value)




db = base()
file = build()
file.createBuild("Chata Procarza",{"drewno" : 1, "garbowana_skóra" : 1}, {"proce" : 15},{"drewno" : 15},{"chłop" : 10}, 1.0)
db.add(file)
file = build()
file.createBuild("Domcio Addosa",{"drewno" : 1, "garbowana_skóra" : 1}, {"proce" : 15},{"drewno" : 15},{"chłop" : 20, "rzemieślnik" : 1}, 1.0)
db.add(file)
file = build()
file.createBuild("Chata Drewala",{"narzędzia" : 4}, {"drewno" : 4},{"drewno" : 1},{"chłop" : 10}, 1.0)
db.add(file)
prod = production()


vill = village(db)

map = {
    "drewno" : [100, 1],
    "ubrania" : [100, 1],
    "narzędzia" : [100, 1],
}
vill.changeDemand(map)


#dodać automatyczne dodawanie obiektu z bazy
vill.production.addRecord("Domcio Addosa", 40)
vill.production.addRecord("Chata Drewala", 2)
vill.production.editRecord("Chata Drewala", "Supplied", {"chłop" : 24})
vill.production.editRecord("Chata Drewala", "ProductionSupplied", {"narzędzia" : 92})

vill.production.editRecord("Domcio Addosa", "Supplied", {"chłop" : 800, "rzemieślnik" : 40})
vill.production.editRecord("Domcio Addosa", "ProductionSupplied", {"drewno" : 2, "garbowana_skóra" : 2})
vill.production.store.appandResourceEmpty("drewno")
vill.production.store.appandResourceEmpty("garbowana_skóra")
vill.production.store.appandResourceEmpty("proce")
# vill.production.summaryProduction()
# vill.production.autofill("Domcio Addosa")
# vill.production.autofill("Chata Drewala")
vill.production.autoFill(vill.wage)
vill.production.calculateStorage()
vill.production.costSummary()
vill.calculateCost()
vill.returnCost()
vill.summaryPopInWork()
vill.updateStorage()
print(vill.costSum)
print(vill.popInWork)
print(vill.store.stock)
print(vill.production.returnRecord("Chata Drewala"))
print(vill.production.returnRecord("Domcio Addosa"))
print(vill.production.store.stock)
# vill.production.addCost)
# vill.production.fill()
# vill.production.fillCosts(vill.wage)
#
# # dict = vill.production.retWorkPopAll()
# print(vill.production.returnRecord("Chata Drewala"))
#
# print(vill.production.store.stock)
# vill.summaryCost()
# print(vill.costMoney)
# vill.returnCost()
# print(vill.costSum)

#usystematyzować 


# print(prod.returnRecord("Domcio Addosa"))
# rsp, i, key, err = prod.findRecord("Domcio Addosa")
# err = prod.addRecord(rsp, key, i, 2)
# if err != "":
#     print(err)
#
# rsp, i, key, err = prod.findRecord("Chata Procarza")
# err = prod.addRecord(rsp, key, i, 2)
# if err != "":
#     print(err)
# prod.buildSupply()
# print(prod.buildSupplied)
# print(prod.popSupplied)
# vill.feedProduction(prod)
# print(vill.production.listOfBuildingsForPeasant)
# print(prod.listOfBuildingsForPeasant)
# print(prod.findObjectBuild(i).name)


''' 
input = {"Drewno" : 0}


systemInfo = {"geometry" : "640x300", "actualTitle" : "Śmietnik"}
prepareList = {"villageName" : "value", "popSize" : 21}

root = Tk()
root.geometry(systemInfo["geometry"])
root.title(systemInfo["actualTitle"])




systemInfo = {"geometry" : "640x300", "actualTitle" : "Śmietnik"}
prepareList = {"villageName" : "value", "popSize" : 21}

root = Tk()
root.geometry(systemInfo["geometry"])
root.title(systemInfo["actualTitle"])


cellBoard = [
    ["","q","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""]
]

for r in range(10):
    for c in range(10):
        if cellBoard[r][c] == "":
            Label(root, text=cellBoard[r][c], padx=10, pady=5, justify=CENTER, relief="groove").grid(row=r, column=c)
        if cellBoard[r][c] != "":
            #base (10)- letters*(-3)
            Label(root, text=cellBoard[r][c],padx=7, pady=5, justify=CENTER, relief="groove").grid(row=r, column=c)
#padx=10, pady=5,
root.mainloop()
'''
