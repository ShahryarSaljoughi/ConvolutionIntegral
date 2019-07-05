from Entities.Signal import Signal
from math import *


class TimeContinuesFormulaSignal(Signal):

    def __init__(self, low_bound, high_bound, formula="(x0)**2"):
        self.low_bound = low_bound
        self.high_bound = high_bound
        self.formula = formula

    def get_value_at(self, index):
        result = eval(self.formula.format(x0=index)) if self.high_bound > index > self.low_bound else 0
        return result
