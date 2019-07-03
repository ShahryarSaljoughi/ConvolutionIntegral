from Entities.Signal import Signal
from math import *


class TimeContinuesNumericSignal(Signal):

    def __init__(self, low_bound, high_bound, values=None):
        Signal.__init__(self, low_bound, high_bound)
        if values is None:
            values = []
        self.values = values

    def get_value_at(self, t: float):
        if t < self.low_bound or t > self.high_bound:
            return 0
        dt = self.values[1][1] - self.values[0][1] if len(self.values) > 1 else 0
        result = [x[0] for x in self.values if x[1] == t or fabs(x[1] - t) < dt/2]
        return 0 if len(result) == 0 else result[0]
