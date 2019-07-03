import abc
from abc import ABCMeta


class Signal(metaclass=ABCMeta):
    """
    Represents a Time-continued, Real-valued signal
    """
    def __init__(self, low_bound: float, high_bound: float):
        self.low_bound = low_bound
        self.high_bound = high_bound

    @abc.abstractmethod
    def get_value_at(self, t):
        return

