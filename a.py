from Entities.TimeContinuesFormulaSignal import TimeContinuesFormulaSignal
from Services.ConvolutionIntegralCalculator import ConvolutionIntegralCalculator
from GUI.Gui import MainWindow


f = TimeContinuesFormulaSignal(low_bound=0, high_bound=10, formula="{x0}**2")
g = TimeContinuesFormulaSignal(low_bound=0, high_bound=10, formula="{x0}")
result = f.get_value_at(5)

calculator = ConvolutionIntegralCalculator(dt=0.05)
res2 = calculator.calculate_integral_at(f, g, 1)

# res3 = calculator.calculate(f, g)
# valueAt3 = res3.get_value_at(3.01)
# print(res3)

window = MainWindow()
window.start()


