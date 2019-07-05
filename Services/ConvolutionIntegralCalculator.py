from Entities.TimeContinuesNumericSignal import TimeContinuesNumericSignal
import numpy as np


class ConvolutionIntegralCalculator:

    def __init__(self, dt=0.001):
        self.dt = dt

    def calculate(self, f, g) -> TimeContinuesNumericSignal:
        """

        :param f: first Signal of type FormulaSignal
        :param g: second Signal of type NumericSignal
        :return: NumericSignal
        """
        output_low_bound = f.low_bound + g.low_bound   # min(f.low_bound, g.low_bound)
        output_high_bound = f.high_bound + g.high_bound
        signal_values = [
            (
                self.calculate_integral_at(f, g, t)
                , t
            ) for t in np.arange(output_low_bound, output_high_bound, self.dt)
        ]
        return TimeContinuesNumericSignal(low_bound=output_low_bound, high_bound=output_high_bound, values=signal_values)

    def calculate_integral_at(self, f, g, t):
        current_element_position = f.low_bound
        result = 0
        while current_element_position < f.high_bound:
            result += f.get_value_at(current_element_position) * g.get_value_at(t - current_element_position) * self.dt
            current_element_position += self.dt

        return result



