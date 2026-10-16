import tkinter as tk
import math
from tkinter import *


def click(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def back():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])


def calculate(event=None):
    try:
        result = eval(entry.get())
        result = round(result, 4)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def sqrt():
    try:
        result = math.sqrt(int(entry.get()))
        result = round(result, 4)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def factorial():
    try:

        if int(entry.get()) <= 18:
            fuc1 = int(entry.get())
            result = fuc1
            while fuc1 > 1:
                result = result * (fuc1 - 1)
                fuc1 = fuc1 - 1
            result = round(result, 4)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        else:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def sin():
    try:
        result = math.sin(math.radians(int(entry.get())))
        result = round(result, 4)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def cos():
    try:
        result = math.cos(math.radians(int(entry.get())))
        result = round(result, 4)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def tan():
    try:
        result = math.tan(math.radians(int(entry.get())))
        result = round(result, 3
                       )
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def one_divided_by_x():
    try:
        result = 1 / int(entry.get())
        result = round(result, 4)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Artin Calculator")
entry = tk.Entry(window, width=17, font=("Arial", 20), borderwidth=1, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4
           , padx=4, pady=8)
entry.focus_set()
buttons = [("√", 1, 0), ("sin", 1, 1), ("cos", 1, 2), ("tan", 1, 3)
    , ("^", 2, 0), ("1/x", 2, 1), ("(", 2, 2), (")", 2, 3)
    , ("C", 3, 0), ("⌫", 3, 1), ("!", 3, 2), ("÷", 3, 3)
    , ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("×", 4, 3)
    , ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("-", 5, 3)
    , ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("+", 6, 3)
    , ("π", 7, 0), ("0", 7, 1), (".", 7, 2), ("=", 7, 3)]

# ⌫
# π
# √
# ÷
# ×
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=calculate).grid(row=row, column=col)
    elif text == "C":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=clear).grid(row=row, column=col)
    elif text == "√":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=sqrt).grid(row=row, column=col)
    elif text == "⌫":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=back).grid(row=row, column=col)
    elif text == "!":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=factorial).grid(row=row, column=col)
    elif text == "sin":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=sin).grid(row=row, column=col)
    elif text == "cos":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=cos).grid(row=row, column=col)
    elif text == "tan":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=tan).grid(row=row, column=col)
    elif text == "1/x":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=one_divided_by_x).grid(row=row,
                                                                                                           column=col)
    elif text == "π":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=lambda t="3.14": click(t)).grid(
            row=row, column=col)
    elif text == "×":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=lambda t="*": click(t)).grid(
            row=row, column=col)
    elif text == "÷":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=lambda t="/": click(t)).grid(
            row=row, column=col)
    elif text == "^":
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=lambda t="**": click(t)).grid(
            row=row, column=col)
    else:
        tk.Button(window, font=("Arial", 15), text=text, width=5, height=1, command=lambda t=text: click(t)).grid(
            row=row, column=col)
window.bind("<Return>", calculate)
window.mainloop()
