import tkinter as tk
from tkinter import messagebox
import serial, time
from tkinter import ttk

__author__ = "Juan Bautista"
__version__ = "1.0.0"

class CalculatorFrame(ttk.Frame):
    """
    Class used to represent a calculator, which will be linked to an arduino uno, 
    which will be used to display the result.

    Attributes
    ----------
    container : str
        The conteiner where the calculator will be
    serial_port : str
        The serial port through which it communicates with the arduino uno (default 'COM1')
    speed : int
        The spped through which it comunicates with the  arduino uno (default 9600)

    Methods
    -------
    show_result ()
        Displays the result of the operation performed on the calculator
    convert_result ()
        Converts the result of the operation to a binary number
    delete_all ()
        Clears all data entered in the calculator
    delete_digit ()
        Clear the last digit entered in the calculator
    replace_text (text)
        Clear all data entered in the calculator and put the text passed as parameter
    write_symbol (symbol)
        Write one more digit on the calculator
    evaluate ()
        Evaluates the operation entered in the calculator
    """

    def __init__(self, container, serial_port='COM1', speed=9600):
        """
        create an object of type calculatorFrame

        Parameters
        ----------
        container : str
            The conteiner where the calculator will be
        serial_port : str
            The serial port through which it communicates with the arduino uno (default 'COM1')
        speed : int
            The spped through which it comunicates with the  arduino uno (default 9600)
        """

        super().__init__(container)

        self.serial_port = serial_port
        self.speed = speed

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        self.display_input = ttk.Entry(self,
                                       font=("Arial", 24),
                                       justify=tk.RIGHT)
        self.display_input.insert(0, "0")
        self.display_input.grid(row=1,
                                column=0,
                                columnspan=4,
                                rowspan=1,
                                sticky="nsew")

        ce_button = ttk.Button(self,
                               text='CE',
                               command=lambda: self.replace_text("0"))
        ce_button.grid(row=2, column=0, sticky=tk.NSEW)
        arrow_button = ttk.Button(self,
                                  text='<-',
                                  command=lambda: self.delete_digit())
        arrow_button.grid(row=2, column=1, columnspan=2, sticky=tk.NSEW)
        div_button = ttk.Button(self,
                                text='/',
                                command=lambda: self.write_symbol("/"))
        div_button.grid(row=2, column=3, sticky=tk.NSEW)

        button7 = ttk.Button(self,
                             text='7',
                             command=lambda: self.write_symbol("7"))
        button7.grid(row=3, column=0, sticky=tk.NSEW)
        button8 = ttk.Button(self,
                             text='8',
                             command=lambda: self.write_symbol("8"))
        button8.grid(row=3, column=1, sticky=tk.NSEW)
        button9 = ttk.Button(self,
                             text='9',
                             command=lambda: self.write_symbol("9"))
        button9.grid(row=3, column=2, sticky=tk.NSEW)
        mul_button = ttk.Button(self,
                                text='x',
                                command=lambda: self.write_symbol("*"))
        mul_button.grid(row=3, column=3, sticky=tk.NSEW)

        button4 = ttk.Button(self,
                             text='4',
                             command=lambda: self.write_symbol("4"))
        button4.grid(row=4, column=0, sticky=tk.NSEW)
        button5 = ttk.Button(self,
                             text='5',
                             command=lambda: self.write_symbol("5"))
        button5.grid(row=4, column=1, sticky=tk.NSEW)
        button6 = ttk.Button(self,
                             text='6',
                             command=lambda: self.write_symbol("6"))
        button6.grid(row=4, column=2, sticky=tk.NSEW)
        sub_button = ttk.Button(self,
                                text='-',
                                command=lambda: self.write_symbol("-"))
        sub_button.grid(row=4, column=3, sticky=tk.NSEW)

        button1 = ttk.Button(self,
                             text='1',
                             command=lambda: self.write_symbol("1"))
        button1.grid(row=5, column=0, sticky=tk.NSEW)
        button2 = ttk.Button(self,
                             text='2',
                             command=lambda: self.write_symbol("2"))
        button2.grid(row=5, column=1, sticky=tk.NSEW)
        button3 = ttk.Button(self,
                             text='3',
                             command=lambda: self.write_symbol("3"))
        button3.grid(row=5, column=2, sticky=tk.NSEW)
        add_button = ttk.Button(self,
                                text='+',
                                command=lambda: self.write_symbol("+"))
        add_button.grid(row=5, column=3, sticky=tk.NSEW)

        button0 = ttk.Button(self,
                             text='0',
                             command=lambda: self.write_symbol("0"))
        button0.grid(row=6, column=0, sticky=tk.NSEW)
        dot_button = ttk.Button(self,
                                text='.',
                                command=lambda: self.write_symbol("."))
        dot_button.grid(row=6, column=1, sticky=tk.NSEW)
        result_button = ttk.Button(self,
                                   text='=',
                                   command=lambda: self.evaluate())
        result_button.grid(row=6, column=2, columnspan=2, sticky=tk.NSEW)

    def show_result(self):
        """
        Transmitted the result of the operation performed on the calculator to the arduino.

        Said result will be transmitted in binary format to the linked arduino.
        To do this, it opens and closes the connection with the Arduino, 
        through its serial port and taking into account its transmission speed.
        """
        arduino = serial.Serial(self.serial_port, self.speed)
        time.sleep(2)
        arduino.write(self.convert_result().encode('utf-8'))
        arduino.close()

    def convert_result(self):
        """
        Converts the result of the operation to a binary number.

        This conversion makes sure that the result has a certain number of binary numbers.

        Returns
        -------
        str
            the result of the operation to a binary number, the result has a certain number of binary numbers.
        """
        text_content = format(int(self.display_input.get()), "b")
        return "{:>4}".format(text_content)

    def delete_all(self):
        """
        Clears all data entered in the calculator
        """
        self.display_input.delete('1.0', 'end')

    def delete_digit(self):
        """
        Clear the last digit entered in the calculator
        
        If there is only one digit left, this operation will always put a zero.
        """
        input_length = len(self.display_input.get())
        if input_length >= 1:
            self.display_input.delete(input_length - 1, tk.END)
        else:
            self.replace_text("0")

    def replace_text(self, text):
        """
        Clear all data entered in the calculator and put the text passed as parameter

        Parameters
        ----------
        text : str
            The text to put
        """
        self.display_input.delete(0, tk.END)
        self.display_input.insert(0, text)

    def write_symbol(self, symbol):
        """
        Write one more digit on the calculator

        If you only have the digit zero in the calculator, 
        this digit entered will take its place, 
        otherwise it will be concaned to the left of what 
        is in the calculator input.

        Parameters
        ----------
        symbol : str
            The symbol to enter
        """
        actualText = self.display_input.get()
        textLength = len(actualText)
        if actualText == "0":
            self.replace_text(symbol)
        else:
            self.display_input.insert(textLength, symbol)

    def evaluate(self):
        """
        Evaluates the operation entered in the calculator

        If an invalid operation is performed or what is entered does not make sense, exceptions are thrown.
        
        Raises
        ------
        SyntaxError
            if the entered expression does not make sense
        ZeroDivisionError
            if you divide by zero
        """
        try:
            result = eval(self.display_input.get())
            self.replace_text(result)
            self.show_result()
        except (SyntaxError, AttributeError):
            messagebox.showerror("Error", "Syntax Error")
            self.replace_text("0")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            self.replace_text("0")

