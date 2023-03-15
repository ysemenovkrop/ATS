# task for classes, inheritance & polymorphism
import math
from statistics import mean, stdev

# parent class -> Calc
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

    def Subtract(self, *args):
        get_sub = args[0]
        for arg in args[1:]:
            get_sub = get_sub - arg
        print("sub:", get_sub)
        self.memList.append(get_sub)

    def Divide(self, *args):
        get_div = args[0]
        for arg in args[1:]:
            get_div = get_div / arg
        print("div:", get_div)
        self.memList.append(get_div)

    def Multiply(self, *args):
        get_mult = 1
        for arg in args:
            get_mult = get_mult * arg
        print("mult:", get_mult)
        self.memList.append(get_mult)

    def PrintResults(self):
        print("memory list:", self.memList)

# Scientific calculator -> child class_1
class ScientificCalc(Calc):
    # constructor of the child class_1
    def __init__(self, name, producer, color, memList, version):
        # reference to the parent class
        Calc.__init__(self, name, producer, color, memList)
        # extra attribute for child class
        self.version = version

    # methods for the child class_1
    def Log(self, a):
        log_calc = math.log(a)
        print("log: ", log_calc)
        self.memList.append(log_calc)

    def Pow(self, *args):
        get_pow = args[0]
        for arg in args[1:]:
            get_pow = get_pow ** arg
        print("pow: ", get_pow)
        self.memList.append(get_pow)


# Extra Calculator -> child class_2
class ExtraCalc(Calc):
    # constructor of the child class_2
    def __init__(self, name, producer, color, memList, ownerName):
        # reference to the parent class
        Calc.__init__(self, name, producer, color, memList)
        # extra attribute for child class_2
        self.ownerName = ownerName

    # methods for the child class_2
    def GetMinRes(self, *args):
        for arg in args:
            min(arg)
            get_min = min(arg)
        print("Min value: ", get_min)
        self.memList.append(get_min)

    def GetMeanRes(self, *args):
        for arg in args:
            mean(arg)
            get_mean = mean(arg)
        print("Average value: ", get_mean)
        self.memList.append(get_mean)

    def GetStdRes(self):
        get_sd = stdev(self.memList)
        print("Standard deviation", get_sd)
        self.memList.append(get_sd)

# checking the code
# parent class
calc1 = Calc("calc1", "Yurii", "Na", "dynamic")
calc1.Add([2, 3])
calc1.Subtract(10, 5, 3, 4)
calc1.Divide(4, 2, 5)
calc1.Multiply(2, 3, 2, 2)
calc1.PrintResults()
# child class_1
calc2 = ScientificCalc("calc2", "Yurii", "Na", "lol1", "ScientificCalc")
calc2.Log(2)
calc2.Pow(3, 2, 2)
calc2.Add([3, 2])
calc2.PrintResults()
# child class_2
calc3 = ExtraCalc("calc3", "Yurii", "Na", "Na", "Exta")
calc3.GetMinRes([2, 3, 5, 0.5])
calc3.Add([2, 4, 6])
calc3.GetMeanRes([1, 2, 3, 4])
calc3.GetStdRes()
calc3.PrintResults()
