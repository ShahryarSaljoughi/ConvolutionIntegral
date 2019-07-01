from Signal import Signal


class FormulaSignal(Signal):

    def __init__(self, low_bound, high_bound, formula="(x0)**2"):
        self.low_bound = low_bound
        self.high_bound = high_bound
        self.formula = formula

    def get_value_at(self, index):
        result = eval(self.formula.format(x0=index))
        return result
