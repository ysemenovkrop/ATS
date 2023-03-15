# write code below
import math
from statistics import mean, stdev

# parent class -> calculator
class Calc:
    # constructor
    def __init__(self, name, producer, color, memList):
        # attributes definition
        self.name = name
        self.producer = producer
        self.color = color
        self.memList = []

    # methods definition
    def Add(self, *args):
        for arg in args:
            get_sum = sum(arg)
        print("sum:", get_sum)
        self.memList.append(get_sum)

    def Subtract(self, a, b):
        sub_calc = a - b
        print("sub:", sub_calc)
        self.memList.append(sub_calc)

    def Divide(self, a, b):
        div_calc = a / b
        print("div:", div_calc)
        self.memList.append(div_calc)

    def Multiply(self, *args):
        get_mult = 1
        for arg in args:
            get_mult = get_mult * arg
        print("mult:", get_mult)
        self.memList.append(get_mult)

    def PrintResults(self):
        print("memory list:", self.memList)


# Scientific calcualtor -> child class_1
class ScientificCalc(Calc):
    # constructor of the child class
    def __init__(self, name, producer, color, memList, version):
        # reference to the initial class
        Calc.__init__(self, name, producer, color, memList)
        # extra attribute for child class
        self.version = version

    # method for the new attribute
    def Log(self, a):
        log_calc = math.log(a)
        print("log: ", log_calc)
        self.memList.append(log_calc)

    def Pow(self, a, b):
        pow_calc = a ** b
        print("pow: ", pow_calc)
        self.memList.append(pow_calc)


# Extra Calculator -> child class_2
class ExtraCalc(Calc):
    # constructor of the child class
    def __init__(self, name, producer, color, memList, ownerName):
        # reference to the initial class
        Calc.__init__(self, name, producer, color, memList)
        # extra attribute for child class
        self.ownerName = ownerName

    # method for the new attribute
    def GetMinRes(self, *args):
        for arg in args:
            min(arg)
            get_min = min(arg)
        print("Min value: ", get_min)
        self.memList.append(get_min)

    def GetMeanRes(self, *args):
        # print("Numbers should be provided in the square brackets")
        for arg in args:
            mean(arg)
            get_mean = mean(arg)
        print("Average value: ", get_mean)
        self.memList.append(get_mean)

    def GetStdRes(self):
        get_sd = stdev(self.memList)
        print("Standard deviation", get_sd)
        self.memList.append(get_sd)




# name, producer, color, memList
calc1 = Calc("calc1", "Yurii", "Na", "dynamic")
calc1.Add([2, 3])
calc1.Subtract(2, 3)
calc1.Divide(4, 2)
calc1.Multiply(2, 3, 2)
calc1.PrintResults()

# name, producer, color, memList, version
calc2 = ScientificCalc("calc2", "Yurii", "Na", "lol1", "ScientificCalc")
calc2.Log(2)
calc2.Pow(3, 2)
calc2.Add([3, 2])
calc2.PrintResults()

calc3 = ExtraCalc("calc3", "Yurii", "Na", "Na", "Exta")
calc3.GetMinRes([2, 3, 5, 0.5])
calc3.Add([2, 4, 6])
calc3.GetMeanRes([1, 2, 3, 4])
calc3.GetStdRes()
calc3.PrintResults()



