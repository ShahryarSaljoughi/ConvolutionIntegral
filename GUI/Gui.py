from tkinter import *
from tkinter.ttk import *
from math import *

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Entities.TimeContinuesFormulaSignal import TimeContinuesFormulaSignal
from Entities.TimeContinuesNumericSignal import TimeContinuesNumericSignal
from Services.ConvolutionIntegralCalculator import  ConvolutionIntegralCalculator

matplotlib.use("TkAgg")

class MainWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title("Convolution Integral Calculator")
        self.window['padx'] = 10
        self.window['pady'] = 10

        self.x_signal: TimeContinuesFormulaSignal = None  # x(t) signal
        self.h_signal: TimeContinuesFormulaSignal = None  # h(t) signal
        self.output_signal: TimeContinuesNumericSignal = None  # output(t)=h(t)*x(t)

        self.fig = Figure(figsize=(5, 4))
        # self.x_input = None
        # self.x_from = None
        # self.x_to = None
        #
        # self.h_input = None
        # self.h_from = None
        # self.h_to = None

        self.create_widgets()

    def create_widgets(self):
        # -------------------
        # - x(t) frame:
        input_frame = Frame(self.window, borderwidth=1, relief=RAISED)
        # input_frame.grid(row=0, column=0, sticky=E + W, ipadx=50, pady=10, ipady=10)
        input_frame.pack(side="top", fill="x", expand=True)

        #  first row:
        x_label: Label = Label(input_frame, text="x(t)= ") \
            .grid(row=0, column=0)
        x_input = Entry(input_frame)
        x_input.grid(row=0, column=1)
        x_from_label = Label(input_frame, text="from:"). \
            grid(row=0, column=2)
        x_from = Entry(input_frame, width=5)
        x_from.grid(row=0, column=3)
        x_to_label = Label(input_frame, text="to:") \
            .grid(row=0, column=4)
        x_to = Entry(input_frame, width=5)
        x_to.grid(row=0, column=5)

        # second row:
        h_label: Label = Label(input_frame, text="h(t)= ") \
            .grid(row=1, column=0)
        h_input = Entry(input_frame)
        h_input.grid(row=1, column=1)
        h_from_label = Label(input_frame, text="from:") \
            .grid(row=1, column=2)
        h_from = Entry(input_frame, width=5)
        h_from.grid(row=1, column=3)
        h_to_label = Label(input_frame, text="to:") \
            .grid(row=1, column=4)
        h_to = Entry(input_frame, width=5)
        h_to.grid(row=1, column=5)

        calculate_button = Button(input_frame, text="calculate convolution")
        calculate_button.grid(row=3, column=1)
        calculate_button['command'] = lambda: self.calculate(
            x_input, h_input, x_from, h_from, x_to, h_to
        )

        #  ---------------------------
        #  output frame:
        output_frame = Frame(master=self.window,)
        output_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.update_output_signal_values()
        canvas = FigureCanvasTkAgg(self.fig, master=output_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def create_signal_objects(self, x: Entry, h: Entry, x_from: Entry, h_from: Entry, x_to: Entry, h_to: Entry):
        x_formula: str = x.get().replace('t', '{x0}')
        x_low_bound = float(x_from.get())
        x_high_bound = float(x_to.get())
        self.x_signal = TimeContinuesFormulaSignal(low_bound=x_low_bound, high_bound=x_high_bound, formula=x_formula)

        h_formula = h.get().replace('t', '{x0}')
        h_high_bound = float(h_to.get())
        h_low_bound = float(h_from.get())
        self.h_signal = TimeContinuesFormulaSignal(low_bound=h_low_bound, high_bound=h_high_bound, formula=h_formula)

    def calculate(self, x: Entry, h: Entry, x_from: Entry, h_from: Entry, x_to: Entry, h_to: Entry):
        self.create_signal_objects(x, h, x_from, h_from, x_to, h_to)
        calculator = ConvolutionIntegralCalculator(dt=0.05)
        self.output_signal = calculator.calculate(self.x_signal, self.h_signal)
        self.update_output_signal_values()

    def start(self):
        self.window.mainloop()

    def update_output_signal_values(self):
        self.fig.clear()
        if self.output_signal is not None:
            self.fig.add_subplot(111).plot(
                [point[1] for point in self.output_signal.values],
                [point[0] for point in self.output_signal.values]
            )




