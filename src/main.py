import tkinter as tk
import os

from calculatorFrame import CalculatorFrame

__author__ = "Juan Bautista"
__version__ = "1.0.0"

class App(tk.Tk):
    """
    Class to create a calculator with fixed size and a dafault tittle.
    """
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('200x350')
        self.iconbitmap(os.path.abspath('../images/linux96.ico'))


if __name__ == "__main__":
    """
    Main method from which the application is executed
    """
    app = App()
    CalculatorFrame(app, "COM3", 9600).pack(fill=tk.BOTH, expand=True)
    app.mainloop()