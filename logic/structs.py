from tkinter import *
import dill, json
from typing import List
from rich.console import Console
import rich as r


# helpers func
def returnDictInfo(dict, int, *option):
    buf = []
    for key in dict:
        buf.append(key)
    if option == "all" and option != "":
        return buf
    return buf[int]



def show(data):
    data = json.loads(data)
    print(json.dumps(data, indent=4, sort_keys=True))

def copyDictWithoutPointer(information):
    return dict(information)



# global staff


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
    #         self.allBuild.append(build_load

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


class ruleSet:
    def __init__(self):
        self.demandRule = {}
        self.prioRule = {}
        self.foodRule = {}
        self.basicRule = {}


    def changeRule(self, ruleType, rule):
        if ruleType == "f":  # food
            self.foodRule = rule
        if ruleType == "d":  # demand
            self.demandRule = rule
        if ruleType == "p":  # prio
            self.prioRule = rule
        if ruleType == "b":  # basic
            self.basicRule = rule

    def addRule(self, ruleType, ruleName, ruleBody):
        if ruleType == "f":  # food
            self.foodRule[ruleName] = ruleBody
        if ruleType == "d":  # demand
            self.demandRule[ruleName] = ruleBody
        if ruleType == "p":  # prio
            self.prioRule[ruleName] = ruleBody
        if ruleType == "b":  # basic
            self.basicRule[ruleName] = ruleBody

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
        self.stock[resource] = self.stock[resource] + much


class imp:
    def __init__(self):
        self.name = ""
        self.ture = 0
        self.rule = ruleSet()
        self.base = {}
        self.economies = {}
        self.store = storage()

    def calculateGoods(self, name):
        t = self.ture
        self.economies[name].calculateFillings(t)

    def updateTure(self, number):
        self.ture = number

    def appandResourceEmpty(self, resource):
        self.store.appandResourceEmpty(resource)

    def appandResourceEmptyBulk(self, map):
        for record in map:
            self.store.appandResourceEmpty(record)

    def updateVillagesWithImperioStorage(self):
        for record in self.economies:
            self.economies[record].store.stock = copyDictWithoutPointer(self.store.stock)

    def passRule(self, ruleType, rule):
        self.rule.changeRule(ruleType, rule)

    def addRule(self, ruleType, ruleName, ruleBody):
        self.rule.addRule(ruleType, ruleName, ruleBody)

    def updateRule(self):
        for record in self.economies:
            self.economies[record].rule.demandRule  = copyDictWithoutPointer(self.rule.demandRule)
            self.economies[record].rule.prioRule = copyDictWithoutPointer(self.rule.prioRule)
            self.economies[record].rule.foodRule = copyDictWithoutPointer(self.rule.foodRule)
            self.economies[record].rule.basicRule = copyDictWithoutPointer(self.rule.basicRule)

    def editNameImperio(self, name):
        self.name = name

    def addVillage(self, name):
        self.economies[name] = village()
        self.economies[name].updateName(name)

    def updateDB(self, db):
        self.base = db

    def updateName(self, name):
        self.name = name


class demand:
    def calculatePopDemand(self, pop, rule):
        bufor = {}
        for record in rule:
            bufor[record] = round(rule[record][0] / pop, 2) * rule[record][1]
        self.popDemand = bufor

    def calculateRationUsage(self, rule, pop, ration):
        popBufer = {}
        for record in pop:
            popBufer[record] = pop[record]*ration[record]

        agrPopRation = 0
        for record in popBufer:
            agrPopRation = agrPopRation+popBufer[record]


        demUnit = agrPopRation/len(rule)
        bufor = {}
        for record in rule:
            bufor[record] = demUnit/rule[record][0]
        return bufor


        # bufor = {}
        # for record in pop:
        #     bufor[record] = pop[record] * ration[record]
        #
        # b = 0
        # for record in bufor:
        #     b = bufor[record] + b
        # bufor = {}
        # for key in stock:
        #     if key in list(rule.keys()):
        #         bufor[key] = stock[key]
        #
        # le = len(bufor)
        # median = b / le
        # for record in bufor:
        #     bufor[record] = bufor[record] - median / rule[record][1]
        #
        # for key in stock:
        #     if key in list(bufor.keys()):
        #         stock[key] = bufor[key]
        #
        # return stock

        # bufor = 0
        # for record in pop:
        #     bufor = bufor + pop[record]*rule[record]
        #
        # self.popDemand = bufor

    def calculateConsumption(self, stock, rule, pop):
        b = 0
        for record in pop:
            b = b + pop[record]

        bufor = {}
        gain = 0
        for key in stock:
            if key in list(rule.keys()):
                gain = gain + (b / rule[key][0])
                bufor[key] = stock[key] - (b / rule[key][0])

        return bufor, gain

    def parseStorageFoodToRation(self, foodname, number, rule):
        if foodname in list(rule.keys()):
            return number * rule[foodname][1]
        else:
            print("that food don't exist in rule")


class village:

    def __init__(self):
        self.name = ""
        self.turnHappines = {}
        self.base = {}
        self.goodsRate = 1
        self.store = storage()
        self.production = production()
        self.production.updateDb(self.base)
        self.dem = demand()
        self.rule = ruleSet()
        self.health = 1.0  # 100%
        self.mood = 1.0
        self.grow = 0
        self.ground = {}
        self.livingarea = {}
        self.gain = 0
        self.pop = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}
        self.popRation = {"Wojownicy": 4, "chłop": 1, "rzemieślnik": 1}
        self.popMulti = {"Wojownicy": 0.5, "chłop": 0.5, "rzemieślnik": 0.5}
        self.popInWork = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}
        self.wage = {"Wojownicy": 0, "chłop": 0.1, "rzemieślnik": 1}  # działa
        self.costMoney = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}  # działa
        self.costSum = 0  # działa
        self.log = {}

    def returnBiznes(self, option):
        bufer = {}
        base = self.production.listOfBuildings
        if option != "":
            if option == "p":
                for record in base:
                    if base[record]["Private"]:
                        bufer[record] = base[record]
                return bufer
            if option == "n":
                for record in base:
                    if not base[record]["Private"]:
                        bufer[record] = base[record]
                return bufer

        for record in base:
            bufer[record] = base[record]
        return bufer


    def updatePrivateBiznes(self, name, array):
        self.production.updatePrivateBiznes(name, array)


    def updateName(self, name):
        self.name = name


    def updateProductionBase(self):
        self.production.base = self.base

    def updateBase(self, db):
        self.base = db
        self.updateProductionBase()


    def setGround(self, rule):
        for record in rule:
            self.ground[record] = rule[record]

    def calculateHealthAndMood(self, ture):
        log = copyDictWithoutPointer(self.log)
        avgBasic = log[ture]["basicNeeds"]["avg"]
        avgDem = log[ture]["popDemand"]["avg"]
        avgFood = log[ture]["foodDem"]["avg"]
        health = round((((avgBasic + avgFood)/2)-0.5), 2)
        mood = round((((avgBasic + avgDem + avgFood)/3)-0.5), 2)
        self.grow = (mood+health)/2
        self.health = health
        self.mood = mood

    def calculateFillings(self, ture):

        moneyFromDem = 0

        agragetePop = 0
        for record in self.pop:
            agragetePop = agragetePop+self.pop[record]

        mapOfDemand = {}
        for record in self.rule.demandRule:
            mapOfDemand[record] = agragetePop/(self.rule.demandRule[record][0]*self.goodsRate)

        bufor = {}
        for record in mapOfDemand:
            if record in list(self.store.stock.keys()):
                store = self.store.stock[record]
                if (store-mapOfDemand[record]) >= 0 :
                    bufor[record] = store - mapOfDemand[record]

                if (store - mapOfDemand[record]) < 0:
                    p = mapOfDemand[record] + (store - mapOfDemand[record])
                    bufor[record] = p
        # moneyFromDem = moneyFromDem + (p * self.rule.demandRule[record][2])

        toStock = bufor
        rule = copyDictWithoutPointer(self.rule.demandRule)
        bufor = {}
        for record in mapOfDemand:
            if record in list(self.store.stock.keys()):
                store = self.store.stock[record]
                if (store-mapOfDemand[record]) >= 0:
                    bufor[record] = 1*rule[record][1]
                    moneyFromDem = moneyFromDem + (1 * rule[record][2])
                if (store - mapOfDemand[record]) < 0:
                    p = mapOfDemand[record] + (store - mapOfDemand[record])
                    bufor[record] = round( (p / mapOfDemand[record])*rule[record][1], 2)
                    moneyFromDem = moneyFromDem + (round(p / mapOfDemand[record],2) * rule[record][2])
                    if bufor[record] < 0:
                        moneyFromDem = moneyFromDem + 0
                        bufor[record] = 0
        temp = 0
        for record in bufor:
            temp = temp+bufor[record]

        temp = temp/len(bufor)
        bufor["avg"] = round(temp,2)
        self.log[ture] = {"popDemand" : bufor}
        stock = copyDictWithoutPointer(self.store.stock)
        for record in toStock:
            if not stock[record]-toStock[record] <= 0:
                stock[record] = round(stock[record]-toStock[record],2)
            else:
                stock[record] = 0
        self.store.stock = stock
        pop = copyDictWithoutPointer(self.pop)
        ration = copyDictWithoutPointer(self.popRation)
        rule = copyDictWithoutPointer(self.rule.foodRule)
        rations = self.dem.calculateRationUsage(rule, pop, ration)
        bufor = {}
        for record in rations:
            if record in list(self.store.stock.keys()):
                store = self.store.stock[record]
                if (store-rations[record]) >= 0:
                    bufor[record] = 1*rule[record][1]
                    moneyFromDem = moneyFromDem + (1 * rule[record][2])
                if (store - rations[record]) < 0:
                    p = rations[record] + (store - rations[record])
                    bufor[record] = round( (p / rations[record])*rule[record][1], 2)
                    test = (round(p / rations[record], 2) * rule[record][2])
                    moneyFromDem = moneyFromDem + test
                    if bufor[record] < 0:
                        moneyFromDem = moneyFromDem + 0
                        bufor[record] = 0
            if not record in list(self.store.stock.keys()):
                bufor[record] = 0
                moneyFromDem = moneyFromDem + 0
        temp = 0
        for record in bufor:
            temp = temp+bufor[record]

        for record in rations:
            if not stock[record]-rations[record] <= 0:
                stock[record] = round(stock[record]-rations[record],2)
            else:
                stock[record] = 0

        temp = temp / len(bufor)
        bufor["avg"] = round(temp, 2)
        self.log[ture]["foodDem"] = bufor
        rule = copyDictWithoutPointer(self.rule.basicRule)
        mapOfDemand = {}
        for record in rule:
            mapOfDemand[record] = agragetePop/rule[record][0]

        bufor = {}
        stock = copyDictWithoutPointer(self.store.stock)
        for record in mapOfDemand:
            if record in list(self.store.stock.keys()):
                store = self.store.stock[record]
                if (store - mapOfDemand[record]) >= 0:
                    bufor[record] = 1 * rule[record][1]
                    stock[record] = stock[record] - mapOfDemand[record]
                    moneyFromDem = moneyFromDem + (1 * rule[record][2])
                if (store - mapOfDemand[record]) < 0:
                    p = mapOfDemand[record] + (store - mapOfDemand[record])
                    stock[record] = stock[record] - mapOfDemand[record]
                    bufor[record] = round((p / mapOfDemand[record]) * rule[record][1], 2)
                    moneyFromDem = moneyFromDem + (round((p / mapOfDemand[record])) * rule[record][2])
                    if bufor[record] < 0:
                        bufor[record] = 0
                        stock[record] = 0
            if not record in list(self.store.stock.keys()):
                bufor[record] = 0

        self.gain = moneyFromDem
        if not agragetePop <= 0:
            stock["złote_monety"] = stock["złote_monety"] + round(moneyFromDem,2 )
            sum = self.costSum
            if (stock["złote_monety"] - sum) >= 0:
                bufor["złote_monety"] = 1
                stock["złote_monety"] = stock["złote_monety"] - sum
            else:
                p = sum + (stock["złote_monety"]-sum)
                bufor["złote_monety"] = round(p/sum,2)
                stock["złote_monety"] = p
        else:
            stock["złote_monety"] = 0
            bufor["złote_monety"] = 0

        for record in stock:
            if stock[record] < 0:
                self.store.stock[record] = 0
            else:
                self.store.stock[record] = stock[record]


        temp = 0
        for record in bufor:
            temp = temp + bufor[record]



        temp = temp / len(bufor)
        bufor["avg"] = round(temp, 2)
        self.log[ture]["basicNeeds"] = bufor


    def calculatePopGrow(self):
        popBufer = {}
        pop = copyDictWithoutPointer(self.pop)
        mood = self.mood
        health = self.health
        popMulti = copyDictWithoutPointer(self.popMulti)
        for record in pop:
            popBufer[record] = round(pop[record]*(((mood + health)/2) + popMulti[record]))
        self.pop = popBufer

    def calculateTurn(self, ture):
        buforMAX = 0
        buforMIN = 100000
        rule = copyDictWithoutPointer(self.rule.prioRule)
        self.production.setPrioBulk(rule)
        for record in rule:

            if buforMIN > rule[record]:
                buforMIN = rule[record]

            if buforMAX < rule[record]:
                buforMAX = rule[record]

        prioListGen = list(range(buforMIN,buforMAX + 1))

        bufor = {}
        for record in prioListGen:

            listBuff = []
            for key in self.production.prioList:
                if record == self.production.prioList[key]["Prio"]:
                    listBuff.append(key)
            if listBuff:
                bufor[record] = listBuff


        popBuffer = {}
        for record in self.pop:
            popBuffer[record] = 0
        for record in bufor:
            for key in bufor[record]:
                self.production.calculateProductionNeeds(key)
                self.production.calculateWorker(key)
                buildme = copyDictWithoutPointer(self.production.listOfBuildings[key])
                stock = copyDictWithoutPointer(self.store.stock)
                pop = copyDictWithoutPointer(self.pop)
                temporary = {}
                if buildme["ProductionNeeded"]:
                    for needs in buildme["ProductionNeeded"]:
                                    buf = {}
                                    if (stock[needs] - buildme["ProductionNeeded"][needs]) >= 0:
                                        stock[needs] = (stock[needs] - buildme["ProductionNeeded"][needs])
                                        temporary[needs] = buildme["ProductionNeeded"][needs]


                                    if (stock[needs] - buildme["ProductionNeeded"][needs]) < 0:
                                        buf[needs] = stock[needs] - (stock[needs] % buildme["ProductionNeeded"][needs])
                                        temporary[needs] = (stock[needs] % buildme["ProductionNeeded"][needs])
                                        stock[needs] = buf[needs]

                buildme["ProductionSupplied"] = temporary
                temporary = {}
                for needs in buildme["Needed"]:
                    if (pop[needs] - buildme["Needed"][needs]) >= 0:
                        pop[needs] = (pop[needs] - buildme["Needed"][needs])
                        temporary[needs] = buildme["Needed"][needs]

                    if (pop[needs] - buildme["Needed"][needs]) < 0:
                        pop[needs] = pop[needs] - (pop[needs] % buildme["Needed"][needs])
                        temporary[needs] = (pop[needs] % buildme["Needed"][needs])
                buildme["Supplied"] = temporary
                self.production.listOfBuildings[key] = buildme
                for record in temporary:
                    popBuffer[record] = popBuffer[record]+temporary[record]

                self.production.calculateEffectProd(key)
                self.production.calculateEffectPop(key)
                self.production.calculateEffect(key)
                self.production.calculateProduction(key)

                self.store.stock = stock

        output = self.production.calculateStorage()
        for record in output:
            self.store.stock[record] = self.store.stock[record] + output[record]
        self.popInWork = popBuffer
        self.calculateCost()
        self.summaryCost()
        self.returnCost()
        self.calculateFillings(ture)
        self.calculateHealthAndMood(ture)

        self.calculatePopGrow()



    def updateStorage(self):
        bufor = self.production.calculateStorage()
        for record in bufor:
            self.store.modifyResource(record, bufor[record])


    def changeStorage(self, stock):
        self.store = stock

    def summaryPopInWork(self):
        summPop = {"Wojownicy": 0, "chłop": 0, "rzemieślnik": 0}

        for record in self.production.listOfBuildings:
            buildInRecord = self.production.listOfBuildings[record]
            for supPopKey in buildInRecord["Supplied"]:
                notemploy = (buildInRecord["Supplied"][supPopKey] - buildInRecord["Needed"][supPopKey])
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
        self.costSum = 0
        for cast in self.costMoney:
            self.costSum = self.costSum + self.costMoney[cast]

    def summaryCost(self):
        self.costMoney = {}
        for record in self.pop:
            self.costMoney[record] = 0
        for bulding in self.production.listOfBuildings:
            dict = self.production.listOfBuildings[bulding]["Cost"]
            if not self.production.listOfBuildings[bulding]["Private"]:
                for recordKey in dict:
                    self.costMoney[recordKey] = self.costMoney[recordKey] + dict[recordKey]

    def suspectedFuture(self):
        self.popInFuture = {"Wojownicy": 0,
                            "Chłopi": round(self.pop["Chłopi"] * (self.popMulti["Chłopi"])),
                            "Rzemieślnicy": round(self.pop["Rzemieślnicy"] * (self.popMulti["Rzemieślnicy"])),
                            }

    def popSummary(self):
        self.pop = {"Wojownicy": self.popInFuture["Wojownicy"] + self.pop["Wojownicy"],
                    "Chłopi": self.popInFuture["Chłopi"] + self.pop["Chłopi"],
                    "Rzemieślnicy": self.popInFuture["Rzemieślnicy"] + self.pop["Rzemieślnicy"]
                    }

    def popModify(self, caste, value):
        self.pop[caste] = value

    def addRecord(self, name, much):
        self.production.addRecord(name, much)


class production:
    def __init__(self):
        self.base = {}
        self.listOfBuildings = {}
        self.prioList = {}
        self.cost = {}

    def updatePrivateBiznes(self, name, bool):
        self.editRecord(name,"Private", bool)

    def updateDb(self, db):
        self.base = db

    def setPrioBulk(self, listWithInfo):
        for record in listWithInfo:
            self.prioList[record] = {
                "Prio": listWithInfo[record],
                "SILOB": self.listOfBuildings[record]
            }

    def updatePrio(self):
        for record in self.prioList:
            self.prioList[record] = {
                "Prio": self.prioList[record]["Prio"],
                "SILOB": self.listOfBuildings[record]
            }

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
                    buforCost[recordKey] = round(costDict[recordKey] * status["Supplied"][recordKey])
            status["Cost"] = buforCost
            self.listOfBuildings[building] = status

    def addRecord(self, name, much):
            build = self.base.allBuild[name]
            self.listOfBuildings[name] = {
                "Much": much,
                "Supplied": {"chłop": 0, "rzemieślnik": 0},
                "Needed": {"chłop": 0, "rzemieślnik": 0},
                "EffectPop": 0,
                "EffectProd": 0,
                "ProductionSupplied": 0,
                "ProductionNeeded": 0,
                "Production": 0,
                "Cost": 0,
                "Raw": build,
                "Effect": 0,
                "Private" : False,
            }


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
            bufor[recordkey] = build.input[recordkey] * buildInProd["Much"]
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
        if not "empty" in list(buildInProd["ProductionNeeded"].keys()):
            if buildInProd["ProductionNeeded"]:
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
            if not buildInProd["ProductionNeeded"]:
                mini = 1
                buildInProd["EffectProd"] = mini
        else:
            buildInProd["EffectProd"] = 1
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
            bufer[record] = round(build.output[record] * buildInProd["Much"] * buildInProd["Effect"], 3)
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

        return bufer


    # def prodToStore(self, resName, value):
    #     self.store.modifyResource(resName, value)

# buildMap = [
#         # [
#         #     "Chata Procarza",
#         #     {"drewno" : 1, "garbowana_skóra" : 1},
#         #     {"proce" : 15},{"drewno" : 15},
#         #     {"chłop" : 10},
#         #     1.0
#         # ],
#         # [
#         #     "Domcio Addosa",
#         #     {"drewno" : 1, "garbowana_skóra" : 1},
#         #     {"proce" : 15},
#         #     {"drewno" : 15},
#         #     {"chłop" : 20, "rzemieślnik" : 1},
#         #     1.0
#         # ],
#         # [
#         #     "Chata Drewala",
#         #     {"narzędzia" : 4},
#         #     {"drewno" : 4},
#         #     {"drewno" : 1},
#         #     {"chłop" : 10},
#         #     1.0
#         # ],
#         # [
#         #     "Farma Pszenicy",
#         #     {"narzędzia" : 0.1},
#         #     {"pszenica" : 200},
#         #     {"drewno" : 1},
#         #     {"chłop" : 10},
#         #     1.0
#         # ],
#         # [
#         #     "Manufaktoria ubran lnianych",
#         #     {"narzędzia": 0.1, "len": 1},
#         #     {"proste_ubrania_len": 2},
#         #     {"drewno": 1},
#         #     {"chłop": 10},
#         #     1.0
#         # ],
#         [
#             "Chata Drwali",
#            {"empty" : 0},
#            {"drewno": 5},
#            {"drewno": 1},
#            {"chłop": 50},
#            1.0
#         ],
#         [
#             "Chata Popielnika",
#             {"drewno": 8},
#             {"potaż": 2},
#             {"drewno": 1},
#             {"chłop": 50},
#             1.0
#         ],
#         [
#             "Mielerz",
#             {"drewno": 6},
#             {"węgiel": 2},
#             {"drewno": 1},
#             {"chłop": 50},
#             1.0
#         ],
#         [
#             "Uprawa Warzyw",
#             {"empty": 0},
#             {"warzywa": 6},
#             {"drewno": 1},
#             {"chłop": 200},
#             1.0
#         ],
#         [
#             "Uprawa Zboża",
#             {"empty": 0},
#             {"zboże": 8},
#             {"drewno": 1},
#             {"chłop": 200},
#             1.0
#         ],
#         [
#             "Port Rybacki",
#             {"empty": 0},
#             {"łodzie": 0}, #limity dodać
#             {"drewno": 1},
#             {"chłop": 150},
#             1.0
#         ],
#         [
#             "Wytwórca Taniny",
#             {"empty": 0},
#             {"tanina": 4},
#             {"drewno": 1},
#             {"chłop": 50},
#             1.0
#         ],
#         [
#             "Garbarnia",
#             {
#                 "tanina": 1,
#                 "potaż": 1,
#                 "tłuszcz":2,
#                 "surowa_skóra":2
#              },
#             {"garbowana_skóra": 2},
#             {"drewno": 1},
#             {"chłop": 50},
#             1.0
#         ],
#         [
#             "Warsztat Narzędzi",
#             {
#                 "żelazo": 1,
#                 "drewno": 1,
#                 "węgiel":2,
#              },
#             {"narzędzia": 4},
#             {"drewno": 1},
#             {"rzemieślnik": 10},
#             1.0
#         ],
#         [
#             "Tkacz",
#             {"len": 5},
#             {"tkaniny": 5},
#             {"drewno": 1},
#             {"chłop": 20},
#             1.0
#         ]
#
#
#
#
#
#
#
#
#
#
# ]
#
#
# for record in buildMap:
#     file = build()
#     file.createBuild(record[0],record[1],record[2],record[3],record[4],record[5])
#     db.add(file)
#
#
# vill = village()
#
#
#
# vill.production.addRecord("Chata Drwali", 18)
# vill.production.addRecord("Chata Popielnika", 2)
# vill.production.addRecord("Mielerz", 3)
# vill.production.addRecord("Uprawa Warzyw", 1)
# vill.production.addRecord("Uprawa Zboża", 1)
# vill.production.addRecord("Port Rybacki", 1)
# vill.production.addRecord("Wytwórca Taniny", 1)
# vill.production.addRecord("Garbarnia", 2)
# vill.production.addRecord("Warsztat Narzędzi", 2)
# vill.production.addRecord("Tkacz", 4)
#
#
# listMaterial = [
#     "zboże",
#     "warzywa",
#     "drewno",
#     "garbowana_skóra",
#     "len",
#     "łodzie",
#     "narzędzia",
#     "potaż",
#     "proste_ubrania_len",
#     "surowa_skóra",
#     "smoła",
#     "tanina",
#     "tkaniny",
#     "tłuszcz",
#     "węgiel",
#     "żelazo",
#     "proce",
#     "złote_monety"
# ]
#
# for record in listMaterial:
#     vill.store.appandResourceEmpty(record)
#
#
#
# listMaterial = {
#     "zboże" : 1000,
#     "warzywa" : 1000,
#     "drewno"  : 1000,
#     "garbowana_skóra"  : 1000,
#     "len"  : 1000,
#     "łodzie"  : 1000,
#     "narzędzia"  : 1000,
#     "potaż"  : 1000,
#     "proste_ubrania_len"  : 1000,
#     "surowa_skóra"  : 1000,
#     "smoła"  : 1000,
#     "tanina"  : 1000,
#     "tkaniny"  : 1000,
#     "tłuszcz"  : 1000,
#     "węgiel"  : 1000,
#     "żelazo"  : 1000,
#     "proce"  : 1000,
#     "złote_monety" : 10000,
# }
#
# for record in listMaterial:
#     vill.store.appandResource(record, listMaterial[record])
#
#
# vill.popModify("chłop",3000)
# vill.popModify("rzemieślnik",100)
# vill.popModify("Wojownicy",0)
#

#
#
# # vill.dem.calculatePopDemand(vill.pop, vill.popRation)
# # print(vill.dem.popDemand)
# #
# # print(vill.production.prioList)
# #
# #
# # print(vill.production.cost)
#
# def popMod():
#     while True:
#         con.print("setValue : 1")
#         con.print("Exit : 5")
#         choose = input()
#         if int(choose) == 1:
#             con.print("Key")
#             key = input()
#             con.print("Value")
#             value = int(input())
#             vill.popModify(key, value)
#
#
#         if int(choose) == 5:
#             break
#         pass
#
# def interface():
#     while True:
#         con.print("PopMod : 1")
#         con.print("Exit : 5")
#         choose = input()
#         if int(choose) == 1:
#                 popMod()
#
#         if int(choose) == 5:
#             break
#         pass
#
#
# con = Console()
# for i in range(10):
#     interface()
#
#
#
#
#     con.print("tura :", i+1)
#     vill.calculateTurn()
#     con.print(list(vill.production.listOfBuildings.keys()))
#     con.print(vill.store.stock)
#     con.print(vill.pop)
#     con.print(vill.popInWork)
#

# vill.production.editRecord("Farma Pszenicy", "Supplied", {"chłop" : 1000})
# vill.production.editRecord("Farma Pszenicy", "ProductionSupplied", {"narzędzia" : 20})
#
# vill.production.editRecord("Chata Drewala", "Supplied", {"chłop" : 24})
# vill.production.editRecord("Chata Drewala", "ProductionSupplied", {"narzędzia" : 92})
#
# vill.production.editRecord("Domcio Addosa", "Supplied", {"chłop" : 800, "rzemieślnik" : 40})
# vill.production.editRecord("Domcio Addosa", "ProductionSupplied", {"drewno" : 2, "garbowana_skóra" : 2})

# # vill.production.summaryProduction()
# # vill.production.autofill("Domcio Addosa")
# # vill.production.autofill("Chata Drewala")
# vill.production.autoFill(vill.wage)
# vill.production.costSummary()
# vill.calculateCost()
# vill.returnCost()
# vill.summaryPopInWork()
# vill.updateStorage()


# {"Wojownicy": 0, "chłop": 1000, "rzemieślnik": 10}


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

# usystematyzować


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


# input = {"Drewno" : 0}
#
#
# systemInfo = {"geometry" : "640x300", "actualTitle" : "Śmietnik"}
# prepareList = {"villageName" : "value", "popSize" : 21}
#
# root = Tk()
# root.geometry(systemInfo["geometry"])
# root.title(systemInfo["actualTitle"])
#
#
#
#
# systemInfo = {"geometry" : "640x300", "actualTitle" : "Śmietnik"}
# prepareList = {"villageName" : "value", "popSize" : 21}
#
# root = Tk()
# root.geometry(systemInfo["geometry"])
# root.title(systemInfo["actualTitle"])
#
#
# cellBoard = [
#     ["","q","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""],
#     ["","","","","","","","","",""]
# ]
#
# for r in range(10):
#     for c in range(10):
#         if cellBoard[r][c] == "":
#             Label(root, text=cellBoard[r][c], padx=10, pady=5, justify=CENTER, relief="groove").grid(row=r, column=c)
#         if cellBoard[r][c] != "":
#             #base (10)- letters*(-3)
#             Label(root, text=cellBoard[r][c],padx=7, pady=5, justify=CENTER, relief="groove").grid(row=r, column=c)
# #padx=10, pady=5,
# root.mainloop()
#
