class Monster:

    def __init__(self, name,monsterType = 'UnknownType'):
        self.monsterType = monsterType
        self.name = name
        self.weaponsDict = {}

    def GetInfo (self):
        print('This is the {0} monster that goes by the name {1}'.format(self.monsterType,self.name))

    def Fight(self):
        output = sum(self.weaponsDict.values())
        return output

    def AddWeapon(self,weaponName,weaponPower):
        self.weaponsDict[weaponName] = weaponPower


class Yeti(Monster):
    def __init__(self, name, isHappy):
        Monster.__init__(self, "Yeti", name)
        self.name = name
        self.isHappy = isHappy

    def ChangeMood(self, isHappy):
        if self.isHappy == True:
            self.isHappy = False
        elif isHappy == False:
            self.isHappy = True

    def Fight(self):
        if self.isHappy == True:
            return 0
        else:
            return 10


monster1 = Monster("Jack")
monster1.AddWeapon("Knife", 30)

monster2 = Monster("Tom")
yeti1 = Yeti("Jack", True)
yeti2 = Yeti("bicaq", False)

print("fight:", yeti1.Fight())

################################################################################################################

class Soldier:
    def __init__(self, soldierType_="UnknownType", name_=""):
        self.soldierType = soldierType_
        self.name = name_
        self.weaponsDict = {}

    def GetInfo(self):
        print("soldierType = {0}\nname = {1}\nweapons = {2}".format(self.soldierType, self.name, self.weaponsDict))

    def Fight(self):
        print("Method is not implemented")

    def AddWeapon(self, weaponName, weaponPower):
        self.weaponsDict[weaponName] = weaponPower


class Marine(Soldier):
    def __init__(self, name_="", agressivnessLevel_=5):
        Soldier.__init__(self, "Marine", name_)
        self.agressivnessLevel = agressivnessLevel_

    def ChangeAgressivnesLevel(self, newAgressivnessLevel):
        self.agressivnessLevel = newAgressivnessLevel

    def Fight(self):
        s = 0
        for weapon in self.weaponsDict.keys():
            print("\nweapon key", weapon)
            self.weaponsDict[weapon] = self.weaponsDict[weapon] ^ (self.agressivnessLevel)
            s += self.weaponsDict[weapon]
        return s


# soldier
s = Soldier("UnknownType", "John")
s.GetInfo()
s.Fight()
s.AddWeapon("x", 2)
s.GetInfo()

# marine
m = Marine("Greg", 10)
m.AddWeapon("y", 5)
m.GetInfo()
m.Fight()
m.GetInfo()

########################################################

class Car:
    def __init__(self, brandA, modelA, maxSpeedA, passengersDictA={"Max_Great": 30}):
        self.brand = brandA
        self.model = modelA
        self.maxSpeed = maxSpeedA
        self.passengersDict = passengersDictA

    def PrintInfo(self):
        print("Car brand={0},Model={1},MaxSpeed={2}".format(self.brand, self.model, self.maxSpeed))
        print("Passengers:")
        for key, value in self.passengersDict.items():
            print("Name: {0} \n Age:{1} \n".format(key, value))
        print("\n\n")

    def GetOldestPassenger(self):
        return max(self.passengersDict, key=self.passengersDict.get)

    def __sub__(self, other):
        brand = self.brand
        model = "mini-" + self.model
        maxSpeed = min(self.maxSpeed, other.maxSpeed)
        new_passengerDict = {}
        for key, value in self.passengersDict.items():
            if (key not in other.passengersDict.keys()):
                new_passengerDict[key] = value
        return Car(brand, model, maxSpeed, new_passengerDict)


car1 = Car("Volvo", "civic", 200, {"Ann": 11, "Sevinj": 23, "George": 40})
car2 = Car("Hyundai", "s40", 250, {"Mark": 12, "Jack": 8, "Murad": 33})

car1.PrintInfo()
car2.PrintInfo()
print("Oldest passenger in car1", car1.GetOldestPassenger(), "\n")
print("Oldest passenger in car2", car2.GetOldestPassenger(), "\n")

car3 = car1 - car2
car3.PrintInfo()

#####################################

class University:

    def __init__(self, name_, rector_, numberofStudents_, researchersDict_={}):
        self.name = name_
        self.rector = rector_
        self.numberofStudents = numberofStudents_
        self.researchersDict = researchersDict_

    def PrintInfo(self):
        print(
            "name = {0}, rector = {1}, number of students = {2}".format(self.name, self.rector, self.numberofStudents))

    def getTotalNumberOfPublications(self):
        return sum(self.researchersDict.values())

    def __add__(self, other):
        new_name = self.name + "_" + other.name
        new_rector = self.rector if self.numberofStudents > other.numberofStudents else other.rector
        new_numberofStudents = self.numberofStudents + other.numberofStudents

        new_researchersDict = other.researchersDict

        for key, value in self.researchersDict.items():
            if (key not in other.researchersDict.keys()):
                new_researchersDict[key] = value
            else:
                new_researchersDict[key] = self.researchersDict[key] + other.researchersDict[key]

        return University(new_name, new_rector, new_numberofStudents, new_researchersDict)


uni1 = University("uni1", "rec1", 100, {"r1": 10, "r2": 20})
uni1.PrintInfo()
print(uni1.getTotalNumberOfPublications())
uni2 = University("uni2", "rec2", 300, {"r2": 10, "r3": 50})
uni2.PrintInfo()
print(uni2.getTotalNumberOfPublications())
uni3 = uni1 + uni2
uni3.PrintInfo()
print(uni3.getTotalNumberOfPublications())


##################

# A)

class ExtremeIndicator:

    def __init__(self, prices, windowSize, upperTreshold=0.3, downTreshold=-0.3):
        self.prices = prices
        self.windowSize = windowSize
        self.upperTreshold = upperTreshold
        self.downTreshold = downTreshold
        self.signalList = []
        self.logReturnsAfterSignals = []

    def getLogReturns(self, valueList):
        print("Function is already implemented.")

    def logReturnsAfterSignals(self, logReturns, signals):
        print("Function is already implemented.")

    def getNegStd(self, logReturns):
        standard_dev = []
        negativeReturn = []
        meanLogReturn = sum(logReturns) / len(logReturns)
        for item in logReturns:
            if item < meanLogReturn:
                negativeReturn.append(item)

        for i in negativeReturn:
            standard_dev.append((i - meanLogReturn) ** 2)
        return (sum(standard_dev) / len(standard_dev)) ** 0.5

    def getSignals(self):
        self.signalList = [0] * (self.windowSize - 1)
        for i in range(window, len(self.prices)):
            value = (self.prices[i] - self.prices[i - window]) / self.prices[i - window]
            if value < self.upperTreshold:
                self.signalList.append(1)
            elif value > self.downTreshold:
                self.signalList.append(-1)
            else:
                self.signalList.append(0)


# B)
prices = [12, 13, 12.5, 11, 10, 9, 11, 12, 13]

negativeStdList = []
windowsList = [2, 6, 8, 10]
for window in windowsList:
    extremeInd = ExtremeIndicator(prices, window)
    signals = extremeInd.getSignals()
    logRet = extremeInd.getLogReturns(prices)
    logRetAfterSignals = extremeInd.logReturnsAfterSignals(logRet, signals)
    negativeStdList.append(extremeInd.getNegStd(logRetAfterSignals))

print(min(negativeStdList))
print(windows[negativeStdList.index(min(negStdList))])
########################

class MagicIndicator:

    def __init__(self, closePrices_, highPrices_, lowPrices_, logReturnsAfterSignals_, treshold_=0.1, signalList_=[]):
        self.closePrices = closePrices_
        self.highPrices = highPrices_
        self.lowPrices = lowPrices_
        self.treshold = treshold_
        self.signalList = signalList_
        self.magicNumbersList = []
        self.logReturnsAfterSignals = logReturnsAfterSignals_

        def getLogReturns(valuesList):
            print("Function implemented")

        def getLogReturnsAfterSignals(logReturns, signals):
            print("Function implemented")

        def SMA(valueList, window):
            print("Function implemented")

        def getMagicNumbers(self, closePrices, highPrices, lowPrices):
            mList = 0
            for i in range(2, len(highPrices)):
                m = 0.5 * (max([highPrices[i], highPrices[i - 1], highPrices[i - 2]]) + min(
                    [lowPrices[i], lowPrices[i - 1], lowPrices[i - 2]]))
                mList.append(m)
            self.magicNumbersList = self.SMA(mList, 3)

        def getSignals(self):
            self.signalList = []
            for i in range(len(self.magicNumbersList)):
                if self.closePrice[i + 2] < (self.magicNumbersList[i] * (1 - self.treshold)):
                    self.signalList.append(1)
                elif self.closePrice[i + 2] > (self.magicNumbersList[i] * (1 + self.treshold)):
                    self.signalList.append(-1)
                else:
                    self.signalList.append(0)

########################

import numpy as np
import math


class Norm2Test:

    def __init__(self, valueListA, nA, criticalValueA=5.91):
        self.valueList = valueListA
        self.n = nA
        self.criticalValue = criticalValueA

    def getMean(self, values):
        sumA = 0
        for i in values:
            sumA += i
        return sumA / len(values)

    def getStd(self, values):
        m = self.getMean(values)
        std = 0
        for item in values:
            std = std + math.pow(item - m, 2)
        return (std / (len(values) - 1)) ** (0.5)

    def getNMoment(self, values, k):
        suma = 0
        xm = self.getMean(values)
        for i in range(self.n - 1):
            suma = suma + pow(values[i] - xm, k)
        return suma / self.n

    def ifNormalDistr(self):
        std = self.getStd(self.valueList)
        moment3 = self.getNMoment(self.valueList, 3)
        s = moment3 / pow(std, 3)
        moment4 = self.getNMoment(self.valueList, 4)
        k = moment4 / pow(std, 4)
        XB = self.n / 6 * (s * s + 0.25 * (k - 3) * (k - 3))

        if (XB > self.criticalValue):
            print("Data do not come from Normal Distribution.")
        else:
            print("Data come from Normal Distribution")


######################

#librarys
import pandas as pd
import math
import numpy as np
from scipy.optimize import minimize

def GetSimpleReturns(valuesList):
    ReturnList=[]
    for i in range(len(valuesList)-1):
        ReturnList.append((valuesList[i+1]-valuesList[i])/valuesList[i])
    return ReturnList

def GetMean(valuesList):
    sumA=0
    for i in valuesList:
        sumA+=i
    return sumA/len(valuesList)

def GetSimpleReturnsStd(valuesList):
    m=GetMean(valuesList)
    std=0;
    for item in valuesList:
        std=std+math.pow(item-m, 2)
    return (std/(len(valuesList)-1))**(1/2)

def GetExpectedSimpleReturn(simpleReturns):
    ret=1
    for i in range(len(simpleReturns)):
        ret=ret*(1+simpleReturns[i])
    return pow(ret,1/len(simpleReturns))-1

def GetCovariance(simpleReturns1,simpleReturns2):
    sumA=0
    mean1=GetMean(simpleReturns1)
    mean2=GetMean(simpleReturns2)
    for i in range(len(simpleReturns1)):
        sumA+=(simpleReturns1[i]-mean1)*(simpleReturns2[i]-mean2)
    return sumA/(len(simpleReturns1)-1)

def  GetCorrelationCoeff(simpleReturns1,simpleReturns2):
    covar=GetCovariance(simpleReturns1,simpleReturns2)
    std1=GetSimpleReturnsStd(simpleReturns1)
    std2=GetSimpleReturnsStd(simpleReturns2)
    return covar/(std1*std2)

XList=[0,0]

def GetSharpRatio (XList):
    #Data
    df1=pd.read_csv('fb.csv')
    df2=pd.read_csv('goog.csv')
    pricesasset1=df1['Close'].values.tolist()
    pricesasset2=df2['Close'].values.tolist()

    simpleReturns1=GetSimpleReturns(pricesasset1)
    simpleReturns2=GetSimpleReturns(pricesasset2)
    expectedReturnAsset1=GetExpectedSimpleReturn(simpleReturns1)
    expectedReturnAsset2=GetExpectedSimpleReturn(simpleReturns2)
    stdAsset1=GetSimpleReturnsStd(simpleReturns1)
    stdAsset2=GetSimpleReturnsStd(simpleReturns2)
    correlationCoeff=GetCorrelationCoeff(simpleReturns1,simpleReturns2)
    portfolioExpectedReturn=(-1)*(XList[0]*expectedReturnAsset1+XList[1]*expectedReturnAsset2)
    portfolioVariance=math.pow(XList[0]*stdAsset1, 2)+math.pow(XList[1]*stdAsset1, 2)+2*XList[0]*XList[1]*stdAsset1*stdAsset2*correlationCoeff
    return portfolioExpectedReturn/pow(portfolioVariance,0.5)

##################

x0 = np.array([0.3, 0.7])

# bounds
b = (-1, 1)
bnds = np.array([b, b])

cons = []

# constraints ( #sum of xList values equals 1)
cons = ({'type': 'eq', 'fun': lambda weightList: np.sum(weightList) - 1})

results = minimize(GetSharpRatio, x0, method='SLSQP', constraints=cons, bounds=bnds)

print("\nPrint all results:")
print(results)

print("\nSelected results:")
print("x:", results["x"])  # optimal weights for given portfolio
print("f(x):", results["fun"])