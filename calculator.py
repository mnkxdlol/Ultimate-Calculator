import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import ttkthemes
import qrcode
import random
from scipy.integrate import odeint

class UltimateCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Calculator - :D")
        self.root.geometry("700x900")
        self.root.resizable(False, False)
        self.expression = ""
        self.history = []

        # for the theme :p
        self.style = ttkthemes.ThemedStyle(root)
        self.style.set_theme("breeze")

        # this is the display fields
        self.input_text = tk.StringVar()
        self.input_field = ttk.Entry(self.root, textvariable=self.input_text, font=('Arial', 20), justify='right', state='readonly')
        self.input_field.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)

        # to create buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('C', '⌫', '(', ')'),
            ('sin', 'cos', 'tan', '√'),
            ('log', '^', '!', 'π'),
            ('e', '1/x', 'fact', 'rand'),
            ('x²', 'x³', 'xⁿ', 'mod'),
            ('Graph', 'frac', 'solve', 'convert'),
            ('bin', 'hex', 'ascii', 'qr'),
            ('derive', 'integrate', 'matrix', 'finance'),
            ('limit', 'taylor', 'ODE', 'stats')
        ]

        for row in buttons:
            frame = ttk.Frame(self.root)
            frame.pack(fill="both", expand=True)
            for btn_text in row:
                btn = ttk.Button(frame, text=btn_text, command=lambda text=btn_text: self.on_button_click(text))
                btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)

    def on_button_click(self, text):
        if text == "C":
            self.expression = ""
        elif text == "⌫":
            self.expression = self.expression[:-1]
        elif text == "=":
            try:
                result = eval(self.expression.replace("^", "**").replace("π", str(np.pi)).replace("e", str(np.e)))
                self.history.append(f"{self.expression} = {result}")
                self.expression = str(result)
            except:
                messagebox.showerror("Error", "Invalid expression")
                self.expression = ""
        elif text == "derive":
            x = sp.Symbol('x')
            expr = sp.sympify(self.expression)
            self.expression = str(sp.diff(expr, x))
        elif text == "integrate":
            x = sp.Symbol('x')
            expr = sp.sympify(self.expression)
            self.expression = str(sp.integrate(expr, x))
        elif text == "bin":
            self.expression = bin(int(self.expression))[2:]
        elif text == "hex":
            self.expression = hex(int(self.expression))[2:]
        elif text == "ascii":
            self.expression = chr(int(self.expression))
        elif text == "qr":
            self.generate_qr_code()
        elif text == "matrix":
            self.matrix_operations()
        elif text == "finance":
            self.finance_operations()
        elif text == "limit":
            x = sp.Symbol('x')
            expr = sp.sympify(self.expression)
            self.expression = str(sp.limit(expr, x, 0))
        elif text == "taylor":
            x = sp.Symbol('x')
            expr = sp.sympify(self.expression)
            self.expression = str(sp.series(expr, x, 0, 5))
        elif text == "ODE":
            self.solve_ode()
        elif text == "stats":
            self.stats_operations()
        else:
            self.expression += text
        self.input_text.set(self.expression)

    def generate_qr_code(self):
        qr = qrcode.make(self.expression)
        qr.show()

    def matrix_operations(self):
        messagebox.showinfo("Matrix Mode", "Feature to be implemented")
    
    def finance_operations(self):
        messagebox.showinfo("Finance Mode", "Feature to be implemented")
    
    def solve_ode(self):
        messagebox.showinfo("ODE Solver", "Feature to be implemented")
    
    def stats_operations(self):
        messagebox.showinfo("Statistics Mode", "Feature to be implemented")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = UltimateCalculator(root)
    root.mainloop()
