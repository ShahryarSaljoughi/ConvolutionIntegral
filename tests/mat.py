import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

window = tk.Tk()

fig = Figure(figsize=(5, 4))
t = np.arange(0, 3, 0.1)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))


canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
window.mainloop()
