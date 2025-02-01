import tkinter as tk
from tkinter import ttk, messagebox
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Theme variables
        self.theme = "light"
        self.light_bg = "#F7F7F7"
        self.dark_bg = "#2C3E50"
        self.light_fg = "#000000"
        self.dark_fg = "#FFFFFF"
        
        self.root.configure(bg=self.light_bg)
        
        # Menu Bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        theme_menu = tk.Menu(menu_bar, tearoff=0)
        theme_menu.add_command(label="Light Mode", command=self.light_mode)
        theme_menu.add_command(label="Dark Mode", command=self.dark_mode)
        
        menu_bar.add_cascade(label="Theme", menu=theme_menu)
        menu_bar.add_command(label="About", command=self.show_about)
        menu_bar.add_command(label="Exit", command=self.root.quit)
        
        # Input Field
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)
        
        input_field = ttk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), justify='right')
        input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)
        
        # Buttons
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('C', 'sin', 'cos', 'tan'),
            ('log', '^', '(', ')')
        ]
        
        for i, row in enumerate(buttons):
            frame = ttk.Frame(self.root)
            frame.pack()
            for j, btn_text in enumerate(row):
                btn = ttk.Button(frame, text=btn_text, command=lambda text=btn_text: self.on_button_click(text))
                btn.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
    
    def on_button_click(self, text):
        if text == "C":
            self.expression = ""
        elif text == "=":
            try:
                self.expression = self.expression.replace('^', '**')
                self.expression = str(eval(self.expression))
            except Exception:
                messagebox.showerror("Error", "Invalid input")
                self.expression = ""
        elif text in ('sin', 'cos', 'tan', 'log'):
            try:
                if self.expression:
                    value = float(eval(self.expression))
                    if text == 'sin':
                        self.expression = str(math.sin(math.radians(value)))
                    elif text == 'cos':
                        self.expression = str(math.cos(math.radians(value)))
                    elif text == 'tan':
                        self.expression = str(math.tan(math.radians(value)))
                    elif text == 'log':
                        self.expression = str(math.log10(value))
            except Exception:
                messagebox.showerror("Error", "Calculation not possible")
                self.expression = ""
        else:
            self.expression += text
        self.input_text.set(self.expression)
    
    def light_mode(self):
        self.theme = "light"
        self.root.configure(bg=self.light_bg)
    
    def dark_mode(self):
        self.theme = "dark"
        self.root.configure(bg=self.dark_bg)
    
    def show_about(self):
        messagebox.showinfo("About", "Ultimate Calculator\nCreated with Tkinter & ttk.")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = AdvancedCalculator(root)
    root.mainloop()

