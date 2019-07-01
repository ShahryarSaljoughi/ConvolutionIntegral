from FormulaSignal import FormulaSignal

from ConvolutionIntegralCalculator import ConvolutionIntegralCalculator

f = FormulaSignal(low_bound=0, high_bound=10, formula="{x0}**2")
g = FormulaSignal(low_bound=0, high_bound=10, formula="{x0}")
result = f.get_value_at(5)

calculator = ConvolutionIntegralCalculator(dt=0.05)
res2 = calculator.calculate_integral_at(f, g, 1)

res3 = calculator.calculate(f, g)
print(res3)


